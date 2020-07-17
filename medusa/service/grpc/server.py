import logging
import os
import sys
import time
from collections import defaultdict
from concurrent import futures
from datetime import datetime
from pathlib import Path

import grpc
import grpc_health.v1.health
from grpc_health.v1 import health_pb2_grpc

import medusa.backup
import medusa.config
import medusa.purge
from medusa.service.grpc import medusa_pb2
from medusa.service.grpc import medusa_pb2_grpc
from medusa.storage import Storage

TIMESTAMP_FORMAT = '%Y-%m-%d %H:%M:%S'


class MedusaService(medusa_pb2_grpc.MedusaServicer):

    def __init__(self, config):
        logging.info("Init service")
        self.config = config
        self.storage = Storage(config=self.config.storage)

    def Backup(self, request, context):
        logging.info("Performing backup {}".format(request.name))
        # TODO pass the staggered and mode args
        try:
            medusa.backup.main(self.config, request.name, None, "differential")
            return medusa_pb2.BackupResponse()
        except Exception:
            resp = medusa_pb2.BackupResponse()
            logging.exception("backup failed")
            return resp

    def BackupStatus(self, request, context):
        response = medusa_pb2.BackupStatusResponse()
        try:
            backup = self.storage.get_cluster_backup(request.backupName)

            # TODO how is the startTime determined?
            response.startTime = datetime.fromtimestamp(backup.started).strftime(TIMESTAMP_FORMAT)
            response.finishedNodes = [node.fqdn for node in backup.complete_nodes()]
            response.unfinishedNodes = [node.fqdn for node in backup.incomplete_nodes()]
            response.missingNodes = [node.fqdn for node in backup.missing_nodes()]

            if backup.finished:
                response.finishTime = datetime.fromtimestamp(backup.finished).strftime(TIMESTAMP_FORMAT)
            else:
                response.finishTime = ""

            return response
        except KeyError:
            context.set_details("backup <{}> does not exist".format(request.backupName))
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return response

    def DeleteBackup(self, request, context):
        logging.info("Deleting backup {}".format(request.name))
        resp = medusa_pb2.DeleteBackupResponse()
        try:
            medusa.purge.delete_backup(self.config, request.name, True)
            return resp
        except Exception:
            logging.exception("Deleting backup {} failed".format(request.name))
            return resp


def create_config(config_file_path):
    config_file = Path(config_file_path)
    args = defaultdict(lambda: None)

    return medusa.config.load_config(args, config_file)


def configure_console_logging(config):
    root_logger = logging.getLogger('')
    root_logger.setLevel(logging.DEBUG)

    log_format = logging.Formatter('[%(asctime)s] %(levelname)s: %(message)s')

    console_handler = logging.StreamHandler()
    console_handler.setLevel(getattr(logging, config.level))
    console_handler.setFormatter(log_format)
    root_logger.addHandler(console_handler)

    if console_handler.level > logging.DEBUG:
        # Disable debugging logging for external libraries
        for logger_name in 'urllib3', 'google_cloud_storage.auth.transport.requests', 'paramiko', 'cassandra':
            logging.getLogger(logger_name).setLevel(logging.WARN)


if len(sys.argv) > 2:
    config_file_path = sys.argv[2]
else:
    config_file_path = "/etc/medusa/medusa.ini"

config = create_config(config_file_path)
configure_console_logging(config.logging)

sleep_time = int(os.getenv("DEBUG_SLEEP", "0"))
logging.debug("sleeping for {} sec".format(sleep_time))
time.sleep(sleep_time)

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

medusa_pb2_grpc.add_MedusaServicer_to_server(MedusaService(config), server)
health_pb2_grpc.add_HealthServicer_to_server(grpc_health.v1.health.HealthServicer(), server)

logging.info('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
