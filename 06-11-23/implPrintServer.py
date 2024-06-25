from printServer import PrintServer
import multiprocessing as mp
import stomp


class ImplPrintServer(PrintServer):
    def __init__(self):
        super().__init__()
        self.process_safe = mp.Queue()

    def print(self, path, tipo):
        msg = '-'.join([path, tipo])
        self.process_safe.put(msg)
    
    def stomp_connect(self):
        self.conn = stomp.Connection([('localhost', 61613)])
        self.conn.connect(wait= True)

    def send_to_queue(self, queue, msg):
        self.conn.send(f"/queue/{queue}", msg)
        print(f"[Server - Consumer] Messaggio <{msg}> inviato alla queue <{queue}>")

    def cons(self):
        self.stomp_connect()
        while True:
            if not self.process_safe.empty():
                msg = self.process_safe.get()
                msg_split = msg.split('-')
                print(f"[Server - Consumer] messaggio prelevato: {msg}")
                if msg_split[1] == 'color':
                    self.send_to_queue('color', msg)
                else:
                    self.send_to_queue('bw', msg)