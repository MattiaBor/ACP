from Interface import IService
import socket,sys

class Skeleton(IService):

    def __init__(self,port):
        self.port = port
        self.impl = ServerImpl()

    def Service(self, msg):
        pass

    def runSkeleton(self):
        sk=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sk.bind(('127.0.0.1',int(self.port)))
        sk.listen(5)
        
        while True:
            c,_=sk.accept()
            data=c.recv()
            self.impl.Service(data.decode())
            c.close()

        sk.close()

class ServerImpl(IService):
    
    def Service(self, msg):
        print("[SERVER] Implementazione servizio - " + str(msg))

if __name__ == "__main__":
    try:
        PORT = sys.argv[1]
    except IndexError:
        print("Specify port ...")

    Skel = Skeleton(PORT)
    Skel.runSkeleton()

    