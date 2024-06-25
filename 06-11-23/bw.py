import stomp, sys, time

class MyListner(stomp.ConnectionListener):
    def __init__(self,tipo):
        self.tipo = tipo


    def on_message(self, frame):
        msg = frame.body.split('-')
        if msg[1] == self.tipo:
            with open('bw.txt', mode='a') as file:
                file.write(frame.body + '\n')

if __name__ == "__main__":
    try:
        tipo = sys.argv[1]
    except IndexError:
        print("Insert valid type (bw/sg)")

    print("Tipo inserito: ",tipo)

    conn = stomp.Connection([('localhost', 61613)])
    conn.set_listener('', MyListner(tipo))
    conn.connect(wait=True)
    conn.subscribe('/queue/bw',1)
    with open('bw.txt', mode='a') as file:
        file.write(f"------------ [Select type {tipo}] ------------\n")



    time.sleep(20000)
