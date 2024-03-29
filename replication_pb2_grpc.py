# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import replication_pb2 as replication__pb2


class SequenceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Write = channel.unary_unary(
                '/replication.Sequence/Write',
                request_serializer=replication__pb2.WriteRequest.SerializeToString,
                response_deserializer=replication__pb2.WriteResponse.FromString,
                )


class SequenceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Write(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SequenceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Write': grpc.unary_unary_rpc_method_handler(
                    servicer.Write,
                    request_deserializer=replication__pb2.WriteRequest.FromString,
                    response_serializer=replication__pb2.WriteResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'replication.Sequence', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Sequence(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Write(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/replication.Sequence/Write',
            replication__pb2.WriteRequest.SerializeToString,
            replication__pb2.WriteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
