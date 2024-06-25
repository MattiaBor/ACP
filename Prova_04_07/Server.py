import stomp
import socket, sys, time
import multiprocessing as mp
from ILogging import ILogging

class Consumatore(mp.Process):
    def __init__(self, conn, queue ):
        super().__init__()
        self.conn  = conn
        self.queue = queue

    def run(self):
        while True:
            if not self.queue.empty():

                msg = self.queue.get()
                print("[SERVER:] Messaggio ottenuto: " + msg)
                tipo = msg.split("-")[1]

                if tipo == '2':
                    conn.send('/queue/error',msg)
                else: 
                    conn.send('/queue/info', msg)


class Produttore(mp.Process):
    def __init__(self,  queue, messaggioLog, tipo):
        super().__init__()
        self.queue = queue
        self.mess  = messaggioLog
        self.tipo = tipo

    
    def run(self):
        msg  = self.mess + "-" + self.tipo
        print("[]")
        self.queue.put(msg)


class Skeleton(ILogging):

    def __init__(self,conn, port, queue):
        self.port = port
        self.conn = conn
        self.queue = queue

    def  log(self, messaggioLog, tipo):
        pass

    def runSkeleton(self):
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sk.bind(('127.0.0.1', int(self.port)))
        sk.listen(5)

        while True: 
            c, addr = sk.accept()
            data = c.recv(1024)
            msg = data.decode().split(",")
            self.log(msg[0], msg[1])
            c.close()

class ServiceImpl(Skeleton):

    def log(self,messaggioLog, tipo):
        p = Produttore(self.queue, messaggioLog, tipo)
        p.start()


if __name__=="__main__":
    
    try:
        PORT = sys.argv[1]
    except IndexError:
        print("specify port...")

    q = mp.Queue(4)
    lock_p = mp.Lock()
    lock_c = mp.Lock()

    conn = stomp.Connection([('127.0.0.1', 61613)])
    conn.connect(wait=True)

    p = Consumatore(conn, q)
    p.start()

    service = ServiceImpl(conn, PORT, q)
    service.runSkeleton()
    
