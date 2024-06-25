import stomp,time
import multiprocess as mp
import socket
import sys
from interface import Service

class SkeletonProcess(mp.Process):

    def __init__(self, conn, mess, proxy):
        mp.Process.__init__(self)
        self.conn = conn
        self.mess = mess
        self.proxy = proxy

    def run(self):
        ricchiesta = self.mess.split('-')[0]

        if richiesta == "deposita":
            id = self.mess.split('-')[1]
            result = self.proxy.deposita(id)
        else:
            result = self.proxy.preleva()
        
        self.conn.send('/queue/risposta', result)

class ServiceProxy(Service):

    def __init__(self, port):
        self.port = port


    def preleva (self):
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sk.connect(('localhost', self.port))
        sk.send('preleva'.encode("utf-8"))

        data = sk.recv(1024)
        sk.close()
        return data

    def deposita (self,id):
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sk.connect(('localhost', self.port))
        message = "deposita-" + str(id)
        sk.send(message.encode("utf-8"))

        data = sk.recv(1024)
        sk.close()
        return data


class Mylistener(stomp.ConnectionListener):

    def __init__(self, conn, port):
        self.conn = conn
        self.port = port

    def on_message(self , frame):
        print('[DISPATCHER] Il messaggio ricevuto è : "%s"' % frame.body)

        proxy = ServiceProxy(int(self.port))

        p = SkeletonProcess(conn, frame.body ,proxy)
        p.start()

if __name__=="__main__":

    try:
        port = sys.argv[1]
    except IndexError:
        print("Please, specify PORT arg...")
    assert port != "", 'specify port'

    conn = stomp.Connection([('127.0.0.1',61613)])
    conn.set_listener('', Mylistener(conn, port))
    conn.connect(wait=True)
    conn.subscribe('/queue/richieste',id=1,ack='auto')

    while(True):
        time.sleep(30)