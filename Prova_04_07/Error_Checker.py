import stomp, time, sys

class MyListener(stomp.ConnectionListener):

    def __init__(self,msg):
        self.msg = msg

    def on_message(self, frame):
        data = frame.body
        print("[ERRORR_CHECKER] Messaggio: " + data)
        if data.split("-")[0]== str(self.msg):
            print(data)


if __name__ == "__main__":

    try:
        msg = sys.argv[1]
    except IndexError:
        print("Spercificare il tipo di errore")

    conn = stomp.Connection([('localhost',61613)])
    conn.set_listener('', MyListener(msg))
    conn.connect(wait=True)

    conn.subscribe('/queue/error', id=1, ack='auto')

    while True:
        time.sleep(60)

    conn.disconnect()
