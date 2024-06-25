import stomp, time


class MyListener(stomp.ConnectionListener):
    def on_message(self, frame):
        print(frame.body)


conn = stomp.Connection([('localhost', 61613)])
conn.set_listener('', MyListener())
conn.connect(wait=True)


conn.subscribe('/queue/bw',1)
conn.subscribe('/queue/color',2)


time.sleep(20000)