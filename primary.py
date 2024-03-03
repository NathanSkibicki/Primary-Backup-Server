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
        backup_channel = grpc.insecure_channel('localhost:50052')
        backup_stub = replication_pb2_grpc.SequenceStub(backup_channel)
        backup_response = backup_stub.Write(request)
        
        print("Received write request:", request)
        
        return replication_pb2.WriteResponse(ack="Write applied successfully")

def main():
    thread_pool = concurrent.futures.ThreadPoolExecutor()

    server = grpc.server(thread_pool)
    replication_pb2_grpc.add_SequenceServicer_to_server(SequenceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Primary server started...")
    server.wait_for_termination()

if __name__ == '__main__':
    main()
