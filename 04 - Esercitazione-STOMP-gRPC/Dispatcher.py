import stomp, sys, time
import service_pb2
import service_pb2_grpc
import grpc
import multiprocessing as mp

class MyProcess(mp.Process):

    def __init__(self, conn, port, msg):
        super().__init__()
        self.port = port
        self.msg = msg
        self.conn = conn

    def run(self):

        channel = grpc.insecure_channel('127.0.0.1:'+str(self.port))
        stub = service_pb2_grpc.ServiceStub(channel)

        richiesta = str(self.msg).split('-')[0]

        if richiesta == 'preleva':
            result = stub.preleva(service_pb2.Empty())
            conn.send('queue/richiesta', str(result.id)+'-'+str(result.message))
        elif richiesta == 'deposita':
            result = stub.deposita(service_pb2.Item(id=int(self.msg.split('-')[1]), message=str(self.msg.split('-')[2])))
            conn.send('/queue/richiesta', str(result.message))
        elif richiesta == 'svuota':
            for result in stub.svuota(service_pb2.Empty()):
                conn.send('/queue/richiesta', str(result.id)+'-'+str(result.message))


class MyListener(stomp.ConnectionListener):
    def __init__(self, port, conn):
        self.port = port
        self.conn = conn

    def on_message(self, frame):
        p = MyProcess(self.conn, self.port, frame.body)
        p.start()


if __name__ == '__main__':


    try:
        PORT = sys.argv[1]
    except IndexError:
        print('Specify a port...')

    conn = stomp.Connection([('127.0.0.1', 61613)])
    conn.set_listener('', MyListener(PORT, conn))
    conn.connect(wait=True)
    conn.subscribe('/queue/richiesta', id=1, ack='auto')

    while True:
        time.sleep(60)

    conn.disconnect()
