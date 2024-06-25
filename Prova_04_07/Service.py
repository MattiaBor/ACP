import socket
import random, time, sys
from ILogging import ILogging

class Proxy(ILogging):
    def __init__(self, port):
        self.port = port
    
    def log(self, messaggioLog, tipo):

        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sk.connect(('localhost',int(self.port)))
        data = messaggioLog +","+ str(tipo)
        sk.send(str(data).encode())
        sk.close()


if __name__ == "__main__":

    try:
        PORT = sys.argv[1]
    except IndexError:
        print("specify port...")

    proxy = Proxy(PORT)

    #genera le richieste iterativamente tramite un for e le chiamate a proy.log(",")
    
    for i in range(10):

        tipo = random.randint(0,2)
        messaggio = random.randint(0,1)
        messaggio_1 = ["success", "checking"]
        messaggio_2 = ["fatal", "exception"]

        #print("[SERVICE]: Messaggio: " + str(messaggio))

        if tipo < 2:
            proxy.log(messaggio_1[messaggio], tipo)
        else:
            proxy.log(messaggio_2[messaggio], tipo)
        
        time.sleep(1)
