import service_pb2,service_pb2_grpc,grpc
from concurrent import futures

class ServiceImpl(service_pb2_grpc.ServiceServicer):
    
    def Servizio1(self, request, context):
        msg = str(request.id)+"-"+request.msg
        return service_pb2.Msg2(msg=msg)
    
    def Servizio2(self, request, context):
        msg = "ack-" + request.msg
        return service_pb2.Msg1(id=1,msg=msg)
    
    
if __name__ == "__main__":

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10),options=(("grpc.os_reuseport",0),))
    service_pb2_grpc.add_ServiceServicer_to_server(ServiceImpl(),server)

    port = 0
    port = server.add_insecure_port("[::]:"+str(port))
    print("[Server] In ascolto sul porto : " + str(port))

    server.start()

    server.wait_for_termination()