import requests

server_addres = 'http://127.0.0.1:5000'

if __name__ == "__main__":

    res = requests.post(server_addres+"/altro/prova",json={1:"a",2:"b"})

    try:
        res.raise_for_status
    except requests.exceptions.HTTPError:
        print(f"status:{res.status_code}, {res.text}")
    else:
        print("Success")

    res = requests.get(server_addres+"/altro")

    try:
        res.raise_for_status
    except requests.exceptions.HTTPError:
        print(f"status:{res.status_code}, {res.text}")
    else:
        print("Success")