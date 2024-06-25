from interfacePrintServer import IPrint
from abc import ABC, abstractmethod
import socket
import multiprocessing as mp



def run_fun_cons(servicer):
    print("[Server - Consumer] Start...")
    servicer.cons()

def run_fun(conn, servicer):
    msg = conn.recv(servicer.buffsize).decode('utf-8')
    msg = msg.split('-')
    print(f"[Server - Prod] Recived msg: {msg}")

    servicer.print(msg[0],msg[1])

    conn.close()



class PrintServer(IPrint, ABC):
    def __init__(self):
        self.buffsize = 1024
    

    @abstractmethod
    def print(self, path, tipo):
        pass

    @abstractmethod
    def cons(self):
        pass


    def run(self):
        consumer_proc = mp.Process(target=run_fun_cons, args=(self,))
        consumer_proc.start()

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("localhost", 0))

        print(f"[Server] Start at port: {s.getsockname()[1]}")
        s.listen(5)

        while True:
            conn, addr = s.accept()

            proc = mp.Process(target=run_fun, args=(conn, self))
            proc.start()

        s.close()
            

