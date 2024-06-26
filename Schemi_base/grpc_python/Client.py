import grpc, service_pb2, service_pb2_grpc
import sys

if __name__ == "__main__":

    try:
        PORT = sys.argv[1]
    except IndexError:
        print("Specify port ...")
    
    channel = grpc.insecure_channel("127.0.0.1:"+str(PORT))
    stub = service_pb2_grpc.ServiceStub(channel)

    for i in range(10):
        msg = "prova1"
        stub.Servizio1(service_pb2.Msg1(id=i,msg=msg))
    
    for i in range(10):
        msg = "prova2"
        stub.Servizio1(service_pb2.Msg2(msg=msg))

    
