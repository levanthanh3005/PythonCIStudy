from flask import Flask
from time import sleep, time
import socket
hostname = socket.gethostname()

app = Flask(__name__)

@app.route('/')
def index():
 return "Hello Python"

if __name__ == "__main__": 
 app.run(host='0.0.0.0', port=80, debug=True)