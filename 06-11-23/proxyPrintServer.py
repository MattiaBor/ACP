from interfacePrintServer import IPrint
import socket

class ProxyPrintServer(IPrint):
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def print(self, path, tipo):
        msg = '-'.join([path, tipo])
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.host,self.port))

        s.send(msg.encode('utf-8'))
        s.close()
