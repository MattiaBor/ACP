import stomp,  sys, time

class MyListner(stomp.ConnectionListener):

    def __init__(self, tipo_r):
        self.tipo_r = tipo_r

    def on_message(self, frame):

        msg = frame.body

        if msg.split('.')[1].split('-')[0] == tipo_r:
            print(str(msg))


if __name__ == "__main__":
    try: 
        tipo_r = sys.argv[1]
    except IndexError:
        print("sprcify a type")

    conn = stomp.Connection([('127.0.0.1', 61613)])
    conn.set_listener('', MyListner(tipo_r))
    conn.connect(wait=True)
    conn.subscribe('/queue/color', id=1, ack='auto')

    while True:
        time.sleep(60)