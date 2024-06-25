import sys, time, grpc
import service_pb2_grpc
import service_pb2
from concurrent import futures
import multiprocessing as mp


class ServerImpl(service_pb2_grpc.ServiceServicer):

    def __init__(self, queue):
        self.queue = queue

    def preleva(self, request, context):
        
        result = self.queue.get()
        print ("[SERVER]: mess prelevato")

        return service_pb2.Item(id=result[0], message=result[1])

    def deposita(self, request, context):

        self.queue.put([request.id, request.message])

        print ("[SERVER]: mess depositato")

        return service_pb2.Stringmessage(message='depositato')


    def svuota(self, request, context):
        
        while not self.queue.empty():
            result = self.queue.get()
            print('[SERVER] messaggio: ' + str(result[1]))

            yield service_pb2.Item(id=result[0], message=result[1])


if __name__=='__main__':

    q = mp.Queue(5)


    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10),options=(('grpc.os_reuseport',0),))
    service_pb2_grpc.add_ServiceServicer_to_server(ServerImpl(q), server)

    port =0

    port = server.add_insecure_port('[::]:'+ str(port))

    print ('[SERVER] In ascolto su porto: ' + str(port))

    server.start()

    server.wait_for_termination()

