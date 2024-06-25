import stomp, sys, time 
from multiprocessing import Queue
import matplotlib.pyplot as plt

class MyListner(stomp.ConnectionListener):

    def __init__ (self, queue):
        self.queue = []

    def on_message(self, frame):
        value = int(frame.body)
        self.queue.put(value)

        if (self.queue.full()):
            plt.plot(self.queue)
            plt.title('lineplot')
            plt.xlabel('Tempo')
            plt.ylabel('Temperatura')
            plt.show()

            self.queue.clear()


if __name__=="__main__":



    conn = stomp.Connection([('127.0.0.1', 61613)])
    conn.set_listener('',MyListner())
    conn.connect(wait=True)
    conn.subscribe('/topic/temp')

    while True:
        time.sleep(60)
    
    conn.disconnect()
