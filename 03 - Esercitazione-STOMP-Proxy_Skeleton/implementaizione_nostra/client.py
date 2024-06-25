import stomp, random , time

class Mylistener(stomp.ConnectionListener):

    def __init__(self, conn):
        self.conn = conn

    def on_message(self , frame):
        print('[CLIENT] Il messaggio ricevuto è : "%s"' % frame.body)


if __name__ == "__main__":

    conn = stomp.Connection([('127.0.0.1',61613)])
    conn.set_listener('', Mylistener(conn))
    conn.connect(wait=True)

    conn.subscribe(destination='/queue/risposta', id=1 , ack='auto')

    for i in range(10):
        if random.randint(0,1):
            Msg= 'preleva'
        else:
            id_art = random.randint(1,50)
            Msg='deposita' + '-' + str(id_art)

        conn.send('/queue/richiesta', Msg)

        print("[CLIENT] Request: ", Msg)

    while(True):
        time.sleep(30)

    conn.disconnect()