from flask import Flask,request
import json

app = Flask(__name__)

@app.route("/",methods=["GET"])
def get_request_demo():
	print (request.args)
	return json.dumps({"err":200})

@app.route("/",methods=["POST"])
def post_request_demo():
	print (request.form)
	return json.dumps({"err":200})

if __name__ == '__main__':
	app.run("0.0.0.0",5000)

