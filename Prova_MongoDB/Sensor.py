import threading
import requests, random

def run_fun(id):

    server_address = "http://127.0.0.1:5000"
    data_t = ["temp", "press"]
    t = random.randint(0,1)
    
    msg = {'id':id, 'data_type':data_t[t]}


    response = requests.post(server_address+'/sensor', json=msg)

    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        print(f"[SENSOR-{id}] Error: REcieved {response.status_code}-{response.text}")
    else:
        print(f"[SENSOR-{id}] Added sensor with :  {msg}")

    data = { '_id':id, 'data_type':random.randint(1,50)}

    for i in range(5):
        requests.post(server_address + '/data/' + data_t[t] , json=random.randint(1,50))

        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            print(f"[SENSOR-{id}] Error: REcieved {response.status_code}-{response.text}")
        else:
            print(f"[SENSOR-{id}] Added data with :  {data}")
       

if __name__ == "__main__":

    threads = []

    for i in range(1,6):
        t = threading.Thread(target=run_fun, args=(i,))
        t.start()
        threads.append(t)
    
    for th in threads:
        th.join()