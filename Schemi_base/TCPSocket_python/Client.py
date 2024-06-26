import socket,sys

if __name__ == "__main__":
    try:
        PORT = sys.argv[1]
    except IndexError:
        print("Specofy port ...")

    sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sk.connect(('127.0.0.1',PORT))

    
    for i in range(10):
        msg = "Messaggio :"+str(i)
        sk.send(msg.encode())
        print("[CLIENT] Messaggio inviato : " + msg)
    
    for i in range(10):
        data = sk.recv(1024)
        print("[CLIENT ] Messagio ricevuto : " + str(data.decode()))

    sk.close()
