import sys, time
from random import randint
from proxyPrintServer import ProxyPrintServer as Proxy

printType_accepted = ['bw', 'sg', 'color']
ext_accepted = ['doc', 'txt']
base_filename = '/user/file_'

def run(port):
    print()
    px = Proxy(host='localhost',port=port)

    for i in range(10):
        numFile = randint(0,100)
        printType = printType_accepted[numFile%3]
        ext = ext_accepted[numFile%2]
        filenmae = f"/user/file_{numFile}.{ext}"
        print(f"[Client] filename Send {filenmae}")
        px.print(filenmae, printType)
        time.sleep(1)





if __name__ == "__main__":
    try:
        port = sys.argv[1]
    except IndexError:
        print("Insert valid port")

    run(port=int(port))

    
