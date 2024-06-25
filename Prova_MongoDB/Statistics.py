import grpc
import statistics_pb2
import statistics_pb2_grpc
from concurrent import futures
import pymongo

def get_Database(nome):
    client = pymongo.MongoClient('172.0.0.1', 27017)
    return client[nome]

class stat_service(statistics_pb2_grpc.StatisticsServicer):

    def getSensors(self, request, context):

        db = get_Database('test')
        collection = db['sensor']

        results = collection.find({})
        
        for result in results:
            yield statistics_pb2.Sensor(_id = result['_id'], data_type=result['data_type'])

    def getMean(self, request, context):

        db = get_Database('test')
        if request.data_type == "temp":
            collection = db['temp']
        elif request.data_type == "press":
            collection = db['press']

        results = collection.find({'sensor_id' : request._id})

        i = 0
        s = 0
        for res in results:
            s = s + res.data
            i = i + 1

        avg = s/i 

        return statistics_pb2.StringMessage(msg=str(avg))


if __name__ == "__main__":

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), options=(('grpc.os_reusport', 0),))
    statistics_pb2_grpc.add_StatisticsServicer_to_server(stat_service(), server)

    port = 0

    port = server.add_insecure_port('[::]:'+str(port))
    print ("[STATISTICS]: In ascolto sul porto " + str(port))

    server.start()

    server.wait_for_termination()
