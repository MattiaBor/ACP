import statistics_pb2_grpc, statistics_pb2
import grpc
import sys

if __name__ == "__main__":

    try:
        PORT = sys.argv[1]
    except IndexError:
        print("Specify port...")
    
    channel = grpc.insecure_channel('127.0.0.1:'+str(PORT))
    stub = statistics_pb2_grpc.StatisticsStub(channel)

    resp = stub.getSensors(statistics_pb2.Empty())

    sensors = []
    

    for sensor in resp:
        print(f'[DASHBOARD] sensor_id:')
        sensors.append(sensor)

    for sensor in sensors:
        mean = stub.getMean(statistics_pb2.MeanRequest(sensor._id,sensor.data_type))
        print(f"[DASHBOARD]: La media del sensore {sensor} è {mean}")