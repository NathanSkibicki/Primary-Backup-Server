
import grpc
import replication_pb2
import replication_pb2_grpc

def main():
    try:
        channel = grpc.insecure_channel('localhost:50051')
        stub = replication_pb2_grpc.SequenceStub(channel)
        request = replication_pb2.WriteRequest(key='1', value='book')
        response = stub.Write(request)
        
        print("Received acknowledgment:", response.ack)
    except grpc.RpcError as e:
        print("Error:", e)

if __name__ == '__main__':
    main()
