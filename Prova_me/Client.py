import stomp
import sys, random, time

class MyListener(stomp.ConnectionListener):

    def __init__(self, conn):
        self.conn = conn
    
    def on_message(self, frame):
        print ('[CLIENT] Il messaggio ricevuto  è: "%s"' % frame.body)


if __name__=="__main__":
    try:
        PORT = sys.argv[1]
    except IndexError:
        print("Specify port ... ")

    conn = stomp.Connection([('127.0.0.1',61613)])
    conn.set_listener('', MyListener(conn))
    conn.connect(wait=True)

    for i in range(10):
        if random.randint(0,1):
            Msg = 'preleva'
        else:
            art = random.randint(1,50)
            Msg = 'deposita' + '-' + str(art) 
    
    conn.send('/queue/richiesta', Msg)

    print ("[CLIENT] Request: ", Msg)

    while True:
        time.sleep(60)
    
    conn.disconnect()
    

        