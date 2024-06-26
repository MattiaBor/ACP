import socket,sys
from Interface import IService

class Proxy(IService):

    def __init__(self,port) :
        self.port = port

    def Service(self, msg):
        sk=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sk.connect(('127.0.0.1',int(self.port)))
        sk.send(msg.encode())
        print("[CLIENT] Messaggio inviato : " + msg)

        sk.close()

if __name__ == "__main__":
    try:
        PORT=sys.argv[1]
    except IndexError:
        print("Specify port ...")

    proxy = Proxy(PORT)
    
    for i in range(10):
        proxy.Service("Messaggio,"+1)
    