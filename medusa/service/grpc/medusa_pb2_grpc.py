# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import medusa.service.grpc.medusa_pb2 as medusa__pb2


class MedusaStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Backup = channel.unary_unary(
            '/Medusa/Backup',
            request_serializer=medusa__pb2.BackupRequest.SerializeToString,
            response_deserializer=medusa__pb2.BackupResponse.FromString,
        )
        self.BackupStatus = channel.unary_unary(
            '/Medusa/BackupStatus',
            request_serializer=medusa__pb2.BackupStatusRequest.SerializeToString,
            response_deserializer=medusa__pb2.BackupStatusResponse.FromString,
        )
        self.DeleteBackup = channel.unary_unary(
            '/Medusa/DeleteBackup',
            request_serializer=medusa__pb2.DeleteBackupRequest.SerializeToString,
            response_deserializer=medusa__pb2.DeleteBackupResponse.FromString,
        )
        self.GetBackups = channel.unary_unary(
            '/Medusa/GetBackups',
            request_serializer=medusa__pb2.GetBackupsRequest.SerializeToString,
            response_deserializer=medusa__pb2.GetBackupsResponse.FromString,
        )


class MedusaServicer(object):
    """Missing associated documentation comment in .proto file"""

    def Backup(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BackupStatus(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteBackup(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBackups(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MedusaServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'Backup': grpc.unary_unary_rpc_method_handler(
            servicer.Backup,
            request_deserializer=medusa__pb2.BackupRequest.FromString,
            response_serializer=medusa__pb2.BackupResponse.SerializeToString,
        ),
        'BackupStatus': grpc.unary_unary_rpc_method_handler(
            servicer.BackupStatus,
            request_deserializer=medusa__pb2.BackupStatusRequest.FromString,
            response_serializer=medusa__pb2.BackupStatusResponse.SerializeToString,
        ),
        'DeleteBackup': grpc.unary_unary_rpc_method_handler(
            servicer.DeleteBackup,
            request_deserializer=medusa__pb2.DeleteBackupRequest.FromString,
            response_serializer=medusa__pb2.DeleteBackupResponse.SerializeToString,
        ),
        'GetBackups': grpc.unary_unary_rpc_method_handler(
            servicer.GetBackups,
            request_deserializer=medusa__pb2.GetBackupsRequest.FromString,
            response_serializer=medusa__pb2.GetBackupsResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'Medusa', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class Medusa(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def Backup(request,
               target,
               options=(),
               channel_credentials=None,
               call_credentials=None,
               compression=None,
               wait_for_ready=None,
               timeout=None,
               metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Medusa/Backup',
                                             medusa__pb2.BackupRequest.SerializeToString,
                                             medusa__pb2.BackupResponse.FromString,
                                             options, channel_credentials,
                                             call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BackupStatus(request,
                     target,
                     options=(),
                     channel_credentials=None,
                     call_credentials=None,
                     compression=None,
                     wait_for_ready=None,
                     timeout=None,
                     metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Medusa/BackupStatus',
                                             medusa__pb2.BackupStatusRequest.SerializeToString,
                                             medusa__pb2.BackupStatusResponse.FromString,
                                             options, channel_credentials,
                                             call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteBackup(request,
                     target,
                     options=(),
                     channel_credentials=None,
                     call_credentials=None,
                     compression=None,
                     wait_for_ready=None,
                     timeout=None,
                     metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Medusa/DeleteBackup',
                                             medusa__pb2.DeleteBackupRequest.SerializeToString,
                                             medusa__pb2.DeleteBackupResponse.FromString,
                                             options, channel_credentials,
                                             call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBackups(request,
                   target,
                   options=(),
                   channel_credentials=None,
                   call_credentials=None,
                   compression=None,
                   wait_for_ready=None,
                   timeout=None,
                   metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Medusa/GetBackups',
                                             medusa__pb2.GetBackupsRequest.SerializeToString,
                                             medusa__pb2.GetBackupsResponse.FromString,
                                             options, channel_credentials,
                                             call_credentials, compression, wait_for_ready, timeout, metadata)
