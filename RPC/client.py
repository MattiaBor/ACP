import stomp
import random, time

class MyListner(stomp.ConnectionListener):

    def __init__(self, conn):
        self.conn = conn
    
    def on_message(self, frame):

        print ('[CLIENT]: Ho ricevuto il messaggio "%s" ', frame.body)
        
    
    

if __name__ == "__main__":
    conn = stomp.Connection([('localhost', 61613)])
    conn.set_listener('', MyListner(conn))

    conn.connect(wait=True)

    conn.subscribe('/queue/response',  id= 1, ack='auto')

    for i in range(16):
        if (i<=10):
            if random.randint(0,1):
                messagge = 'deposita-' + str(random.randint(0,50)) + '-smartphone'
            else:
                messagge = 'deposita-' + str(random.randint(0,50)) + '-laptop'
        elif (i>10 and i<=15):
            messagge = 'preleva'
        else:
            messagge = 'svuota'
            
        conn.send('/queue/request', messagge)

    while True:
        time.sleep(60)

    conn.disconnect()


