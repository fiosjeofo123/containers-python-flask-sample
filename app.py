from flask import Flask
from threading import Thread
import backend_code
Thread(target=backend_code.run).start()
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello Back4apper!"
def run():
    while True:
        print("HI")
        import time as t
        t.sleep(1)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
