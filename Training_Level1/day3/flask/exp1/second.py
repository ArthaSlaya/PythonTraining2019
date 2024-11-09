from flask import Flask,request,render_template
import json
app = Flask(__name__)
'''
@app.route("/")
@app.route("/<name>")
def hello(name=None):
	return render_template('hello.html', name=name)
'''

@app.route("/listme",methods=["GET"])
def listme():
	list_a=["Sugar","Salt","Lime","Soda"]
	return render_template('list.html',mylist=list_a)
	
@app.route("/getme",methods=["POST"])
def getme():
	print (request.form)
	if("name" in request.form):
		return request.form["name"]
	return "Parameter name is missing"

@app.route("/home/<username>")
def home(username):
	return json.dumps({"err":200,"username":username})

if __name__ == '__main__':
	app.run("0.0.0.0",5000)
