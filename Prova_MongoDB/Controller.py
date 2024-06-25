from flask import Flask, request
import pymongo

app = Flask(__name__)

def get_Database(nome):
    client = pymongo.MongoClient('172.0.0.1', 27017)
    return client[nome]

@app.post('/sensor')
def salva_sensore():

    db = get_Database("test")

    sensor_spec = request.get_json()
    collection = db['sensor']
    try:
        result = collection.insert_one(document=sensor_spec)
    except Exception as e:
        print("[STORE DATA]: Operation failed")
        return {'result' : 'failed - ' +str(e)}, 500

    return sensor_spec

@app.post('/data/<data_type>')
def salva_dati(data_type):

    db = get_Database("test")

    data = request.get_json()

    if data_type == "temp":
        collection = db["temp"]
    elif data_type == "press":
        collection = db["press"]
    
    try:
        result = collection.insert_one(document=data)
    except Exception as e:
        print("[STORE DATA]: Operation failed")
        return {'result' : 'failed - ' +str(e)}, 500

    collection.insert_one(document=data)

    return data

if __name__ == "__main__":
    app.run(debug=True, port=5000)