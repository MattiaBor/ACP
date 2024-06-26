import stomp,time

class MyListener(stomp.ConnectionListener):

    def on_message(self, frame):
        print(f"[CLIENT] Messaggio ricevuto {frame.body}")

if __name__ == "__main__":
    
    conn = stomp.Connection([('127.0.0.1',61613)])
    conn.set_listener("",MyListener())
    conn.connect(wait=True)
    conn.subscribe("/queue/response",1)

    for i in range(10):
        conn.send("/queue/request","Prova:"+str(i))

    while True:
        time.sleep(50)