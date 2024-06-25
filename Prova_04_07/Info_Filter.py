import stomp, time, sys

class MyListener(stomp.ConnectionListener):


    def on_message(self, frame):
        data = frame.body

        if data.split("-")[1] == str(1):
            print(data)


if __name__ == "__main__":


    conn = stomp.Connection([('localhost',61613)])
    conn.set_listener('', MyListener())
    conn.connect(wait=True)

    conn.subscribe('/queue/info', id=1, ack='auto')

    while True:
        time.sleep(60)

    conn.disconnect()
