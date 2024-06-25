from Interface import IPrinter
import socket, sys, stomp, time, random
import multiprocessing as mp


def produttore(queue, path, tipo):

    messaggio = path + '-' + tipo
    queue.put(str(messaggio))

def consumatore(queue):

    conn  = stomp.Connection([('127.0.0.1',61613)])
    conn.connect(wait=True)

    while True:
        while not queue.empty():
            msg = queue.get()
            print(msg)
            if msg.split('-')[1] == 'color':
                conn.send('/queue/color', msg)
            else:
                conn.send('/queue/bw', msg)

    conn.disconnect()


class Skeleton(IPrinter):

    def __init__(self, port, queue):
        self.port = port
        self.queue = queue
        

    def print(self, path, tipo):
        pass

    def run_skeleton(self):
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sk.bind(('127.0.0.1', int(self.port)))
        sk.listen(5)

        while True:
            c,_=sk.accept()
            data = c.recv(1024)
            c.send('ricevuto'.encode())
            msg = data.decode()
            self.print(msg.split(',')[0], msg.split(',')[1])
        
class serverImpl(Skeleton):

    def print(self, path, tipo):

        p = mp.Process(target=produttore, args=(self.queue, path,tipo))
        p.start()

if __name__ == "__main__":
    try:
        PORT = sys.argv[1]
    except IndexError:
        print("Specify a port...")

    q = mp.Queue(5)

    consumatore = mp.Process(target=consumatore, args=(q,))
    consumatore.start()

    s = serverImpl(PORT, q)
    s.run_skeleton()

