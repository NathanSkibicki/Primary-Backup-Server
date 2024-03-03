import grpc
import concurrent.futures
import replication_pb2
import replication_pb2_grpc
import heartbeat_service_pb2_grpc

HEARTBEAT_ADDRESS = 'localhost:50053'

class SequenceServicer(replication_pb2_grpc.SequenceServicer):

    def __init__(self):
        self.heartbeat_channel = grpc.insecure_channel(HEARTBEAT_ADDRESS)
        self.heartbeat_stub = heartbeat_service_pb2_grpc.ViewServiceStub(self.heartbeat_channel)

    def Write(self, request, context):
        print("Received write request on backup:", request)
        return replication_pb2.WriteResponse(ack="Write applied successfully on backup")

def main():
    thread_pool = concurrent.futures.ThreadPoolExecutor()
    server = grpc.server(thread_pool=thread_pool)
    replication_pb2_grpc.add_SequenceServicer_to_server(SequenceServicer(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    print("Backup server started...")
    server.wait_for_termination()

if __name__ == '__main__':
    main()
