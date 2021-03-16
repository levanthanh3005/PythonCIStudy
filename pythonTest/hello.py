from flask import Flask
from time import sleep, time
import socket
hostname = socket.gethostname()

app = Flask(__name__)

@app.route('/')
def index():
	return "Hello Python"


@app.route('/hello2')
def index2():
	return "Hello Python 2"

@app.route('/getparams/<int:test_id>',methods=['GET','POST'])
def get_params(test_id):
	return "Hello "+str(test_id)

@app.route('/testpost',methods=['POST'])
def testpost():
	value = request.args.get('somekey')

	return "Hello "+value

if __name__ == "__main__": 
 app.run(host='0.0.0.0', port=80, debug=True)