import stomp, sys, time 
from multiprocessing import Queue
import matplotlib.pyplot as plt
import csv


class MyListner(stomp.ConnectionListener):

    def __init__ (self, count):
        self.count = count

    def on_message(self, frame):
        value = int(frame.body)
        self.queue.put(value)

        riga = [self.count, frame.body]

        with open ('press.csv', mode='a') as file:
            writer = csv.DictWriter(file)
            writer.writerow(riga)
        self.count = self.count + 1




if __name__=="__main__":



    conn = stomp.Connection([('127.0.0.1', 61613)])
    conn.set_listener('',MyListner())
    conn.connect(wait=True)
    conn.subscribe('/topic/temp')

    while True:
        time.sleep(60)
    
    conn.disconnect()
