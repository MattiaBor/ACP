import service_pb2_grpc
import stomp, sys, time
import multiprocessing as mp
import grpc
import service_pb2

class myProcess(mp.Process):
    def __init__(self, port, mess, qconn):
        mp.Process.__init__(self)
        self.port = port
        self.mess = mess
        self.qconn = qconn

    def run(self):
        
        channel = grpc.insecure_channel("localhost:"+str(self.port))
        stub = service_pb2_grpc.ServiceStub(channel)

        richiesta = str(self.mess).split('-')[0]

        if richiesta == 'deposita':
            result = stub.deposita(service_pb2.Item(id=int(str(self.mess).split('-')[1]), prodotto=str(self.mess).split('-')[2]))
            conn.send('/queue/response', str(result.messagge))
        elif richiesta == 'preleva':
            result = stub.preleva(service_pb2.Empty())
            conn.send('/queue/response', str(result.id)+"-"+str(result.prodotto))
        elif richiesta == 'svuota':
            for result in stub.svuota(service_pb2.Empty()):
                conn.send('/queue/response', str(result.id)+"-"+str(result.prodotto))
            



class MyListner(stomp.ConnectionListener):
    def __init__ (self,conn, port):
        self.conn = conn
        self.port = port

    def on_message(self, frame):
        print ("[DISPATCHER]:inizializzo i thread")
        p = myProcess(self.port, frame.body, self.conn)
        p.start()
         
        
        

    

if __name__ == "__main__":
    try:
        port = sys.argv[1]
    except IndexError:
        print("Specify port...")

    conn = stomp.Connection([('localhost', 61613)])
    conn.set_listener('', MyListner(conn))
    conn.connect(wait=True)
    conn.subscribe('/queue/response', id=1, ack='auto')

    while True:
        time.sleep(60)

    conn.disconnect()

