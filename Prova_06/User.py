import socket, random, time, sys
from Interface import IPrinter


class Proxy(IPrinter):

    def __init__ (self, port):
        self.port = port

    def print(self, path, tipo):
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sk.connect(('127.0.0.1', int(self.port)))
        message  = path + "," + tipo
        sk.send(str(message).encode())
        print("[USER] messaggio inviato: " + str(message))

        data = sk.recv(1024)
        print("[USER] " + data.decode())
        sk.close()


if __name__ == "__main__":
    try:
        PORT = sys.argv[1]
    except IndexError:
        print("specify a port...")

    proxy = Proxy(PORT)
    
    tipo_t = ['gs', 'bw', 'color']
    estensione = ['doc', 'txt']

    for i in range(10):
        NUM = random.randint(0,100)
        pathFile =f"/user/file_{NUM}.{estensione[random.randint(0,1)]}"
        tipo =  tipo_t[random.randint(0,2)]

        proxy.print(pathFile, tipo)

        time.sleep(1)
    
