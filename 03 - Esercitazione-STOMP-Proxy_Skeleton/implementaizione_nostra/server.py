from interface import Service
import sys
import multiprocess as mp
import socket

def proc_fun(c, service):

    data = c.recv(1024)

    if  str(data)== "preleva":

        result = service.preleva()
    
    else: 
        id = str(data.decode()).split('-')[1]
        result = service.deposita(id)

    c.send(str(result).encode("utf-8"))

    c.close()


class Skeleton(Service):

    def __init__(self, port, queue):
        self.port = port
        self.queue = queue

    def deposita(self, message):
        pass
    
    def preleva(self):
        pass

    def run_skeleton(self):
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sk.bind(('localhost', self.port))

        sk.listen(5)
        
        while True:
            conn, addr= sk.accept()
        
            p = mp.Process(target=proc_fun, args=(conn, self))
            p.start()

        sk.close()    

class ServiceImpl(Skeleton):

    def deposita(self , data):
        self.queue.put(data)
        print("[SERVER-IMP] depositato", data)

        return "deposited"
    
    def preleva(self):
        self.queue.get()
        print("[Server-IMPL] PRELEVATO", result)

        return result



if __name__ == "__main__":

    try: 
        port = sys.argv[1]
    except IndexError:
        print ("Inserire un porto")

    print("server attivo ...")
    
    q = mp.Queue(5)

    si = ServiceImpl(int(port),q)
    si.run_skeleton()