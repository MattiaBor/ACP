import grpc
import service_pb2
import service_pb2_grpc
import multiprocessing as mp
import sys
from concurrent import futures

class ServiceImpl(service_pb2_grpc.ServiceServicer):

    def __init__(self, queue, lock_d, lock_p):
        self.queue = queue
        self.lock_d = lock_d
        self.lock_p = lock_p
    
    def deposita(self, request, context):
        
        with self.lock_d:
            self.queue.put([request.id,request.prodotto])
        print ("[SERVER]: sono nel lock_d e depoposito il dato")

        return service_pb2.Stringmessage(message='depositato')

    def preleva(self, request, context):
        
        with self.lock_p:
            result=self.queue.get()
        print ("[SERVER]: sono nel lock_d e prelevo il dato"+ str(result[1]))

        return service_pb2.Item(id=result[0], prodotto=result[1])

    def svuota(self, request, context):
        
        self.lock_p.acquire()
        self.lock_d.acquire()

        while not self.queue.empty(): 
            result=self.queue.get()
            print ("[SERVER]: sono nel lock_d e prelevo il dato"+ str(result[1]))

            yield service_pb2.Item(id=result[0], prodotto=result[1])

        self.lock_d.release()
        self.lock_p.release()



if __name__ == "__init__":

    q = mp.Queue(5)
    lock_d = mp.Lock()
    lock_p = mp.Lock()
    
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), options=(("grpc.so_reuseport",0),))

    service_pb2_grpc.add_ServiceServicer_to_server(ServiceImpl(queue, lock_d, lock_p), server)

    port = 0

    port = server.add_insecure_port('[::]'+str(port))
    print("Start server Listening on port" + str(port))

    server.start()

    server.wait_for_termination()
    
