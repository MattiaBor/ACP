import stomp,time

class MyListener(stomp.ConnectionListener):

    def __init__(self,port):
        self.port = port

    def on_message(self, frame):
        print(f"[SERVER] Messaggio ricevuto {frame.body}")
        conn.send("/queue/response", "ack"+frame.body)


if __name__ == "__main__":
    
    conn = stomp.Connection([('127.0.0.1',61613)])
    conn.set_listener("",MyListener(conn))
    conn.connect(wait=True)
    conn.subscribe("/queue/request",1)

    while True:
        time.sleep(50)