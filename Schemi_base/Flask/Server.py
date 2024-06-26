from flask import Flask,request


app = Flask(__name__)

@app.post("/altro/<variabile>")
def store_data(variabile):
    body=request.get_json
    print(f"i dati inseriti sono :{body} tramite post in {variabile}")
    return {"result":"succes"}

@app.get("/altro")
def foo():
    print("hai fatto una get")
    return {"result":"succes"}

if __name__ == "__main__":
    app.run()