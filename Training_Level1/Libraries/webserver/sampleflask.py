from flask import Flask,request
import json
app = Flask(__name__)

# pymotw.com

# Function 1
def takebackup():
	print ("Taking backup")
# Function 2
def erasedrive():
	print ("Erasing drive")

mapper={
	"backup": takebackup,
	"erase" : erasedrive
}

@app.route("/home",methods=["POST","GET"])
def hello():	
	dict_a={"name":request.form["username"]}
	return json.dumps(dict_a)

@app.route("/command",methods=["POST"])
def command():
	if("command" in request.form):
		if(request.form["command"] in mapper):
			mapper[request.form["command"]]()
			return "Command Executed"
		else:
			return "Command not found in list"
	return "Command Parameter Missing"

if __name__ == '__main__':
	app.run("0.0.0.0",5000)