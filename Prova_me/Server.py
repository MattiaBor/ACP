from Interface import Service
import sys
import multiprocessing as mp
import socket

def proc_fun(c, service):
    data = c.recv(1024)

    if str(data) == 'preleva':
        result = service.preleva()
    
    else:
        id = str(data.decode()).split('-')[1]
        result = service.deposita(id)
    
    c.send(str(result).encode())
    c.close()

class Skeleton(Service):

    def __init__(self, port, queue):
        self.port = port
        self.queue = queue
    
    def preleva(self):
        pass

    def deposita(self, message):
        pass

    def run_skeleton(self):
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sk.bind(('127.0.0.1', self.port))

        sk.listen(5)

        while True:
            conn, addr = sk.accept()
            p = mp.Process(target=proc_fun, args=(conn, self))
            p.start()
        
        sk.close()

class ServiceImpl(Skeleton):

    def deposita(self, data):
        self.queue.put(data)
        print("[SERVER-IMPL] datao depositato ", data)
    def preleva(self):
        result = self.queue.get()
        print("[SERVER-IMPL] dato prelevato", result)

        return result


if __name__=="__main__":
    try:
        PORT = sys.argv[1]
    except IndexError:
        print ("Specify port ...")

    print("server in ascolto")
    
    q = mp.Queue(5)
    ser = ServiceImpl(int(PORT), q)
    ser.run_skeleton()

