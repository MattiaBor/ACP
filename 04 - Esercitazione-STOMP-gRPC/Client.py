import stomp, time, sys, random

class MyListener(stomp.ConnectionListener):

    def on_message(self, frame):
        print('[CLIENT] messaggio: '+ frame.body)


if __name__=="__main__":

    conn = stomp.Connection([('127.0.0.1', 61613)])
    conn.set_listener('', MyListener())
    conn.connect(wait = True)
    conn.subscribe('/queue/richiesta', id=1, ack='auto')

    tipo_richiesta = ['deposita','preleva','svuota']
    id_art = random.randint(1,40)
    prodotto = ['laptop', 'smartphone']

    for i in range(10):
        id_art = random.randint(1,40)
        msg = tipo_richiesta[0] + '-' +str(id_art)+ '-' + prodotto[random.randint(0,1)]
        conn.send('/queue/richiesta', msg)
    for i in range(5):
        msg = tipo_richiesta[1]
        conn.send('/queue/richiesta', msg)
    msg = tipo_richiesta[2]
    conn.send('queue/richiesta', msg)

    while True:
        time.sleep(60)
    
    conn.disconnect()