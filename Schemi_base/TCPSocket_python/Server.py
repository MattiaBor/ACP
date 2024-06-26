import socket, sys

if __name__ == "__main__":
    try:
        PORT = sys.argv[1]
    except IndexError:
        print("Specify port ...")

    sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sk.bind(('127.0.0.1',PORT))
    sk.listen(5)

    while True:
        c,_=sk.accept()
        data = c.recv(1024)
        msg=data.decode()
        print("[SERVER] Messaggio ricevuto : " + msg)
        c.send("ACK".encode())
        c.close()

    sk.close()