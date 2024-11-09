from flask import Flask,request,render_template
import json
app = Flask(__name__)

@app.route("/",methods=["GET"])
def render_request_demo():
	return render_template("home.html",list_a=["Hello","Ok","Bye"])


@app.route("/gethome",methods=["GET"])
def get_request_demo():
	print (request.args["name"])
	return "Hello World!"

@app.route("/posthome",methods=["POST"])
def post_request_demo():
	dict_a={
		"name" : request.form["name"]
	}
	return json.dumps(dict_a)

if __name__ == '__main__':
	app.run("0.0.0.0",5000)


