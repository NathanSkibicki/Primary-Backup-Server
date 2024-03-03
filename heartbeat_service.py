import grpc
import heartbeat_service_pb2_grpc
import heartbeat_service_pb2
import concurrent.futures
import time
from google.protobuf import empty_pb2

class ViewServiceServicer(heartbeat_service_pb2_grpc.ViewServiceServicer):
    def __init__(self):
        self.primary_last_heartbeat = time.time()
        self.backup_last_heartbeat = time.time()

    def Heartbeat(self, request, context):
        service_identifier = request.service_identifier
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        
        if service_identifier == "Primary":
            self.primary_last_heartbeat = time.time()
            print(f"Primary is alive. Latest heartbeat received at {current_time}")
        elif service_identifier == "Backup":
            self.backup_last_heartbeat = time.time()
            print(f"Backup is alive. Latest heartbeat received at {current_time}")
        
        return empty_pb2.Empty()

    def check_servers(self):
        while True:
            current_time = time.time()

            if current_time - self.primary_last_heartbeat > 5:
                print(f"Primary might be down. Latest heartbeat received at {time.strftime('%Y-%m-%d %H:%M:%S')}")
            
            if current_time - self.backup_last_heartbeat > 5:
                print(f"Backup might be down. Latest heartbeat received at {time.strftime('%Y-%m-%d %H:%M:%S')}")

            time.sleep(1)

def main():
    thread_pool = concurrent.futures.ThreadPoolExecutor()
    server = grpc.server(thread_pool=thread_pool)
    heartbeat_service_pb2_grpc.add_ViewServiceServicer_to_server(ViewServiceServicer(), server)
    server.add_insecure_port('[::]:50053')
    server.start()
    print("Heartbeat server started...")

    vs_servicer = ViewServiceServicer()
    check_servers_thread = thread_pool.submit(vs_servicer.check_servers)
    
    server.wait_for_termination()

if __name__ == '__main__':
    main()
