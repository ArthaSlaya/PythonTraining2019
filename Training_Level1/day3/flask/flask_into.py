from flask import Flask,request

app = Flask(__name__)

@app.route("/",methods=["GET"])
def get_request_demo():
	print (request.args)
	return "Hello World!"

@app.route("/",methods=["POST"])
def post_request_demo():
	print (request.form)
	return "Hello World!"

if __name__ == '__main__':
	app.run("0.0.0.0",5000)

