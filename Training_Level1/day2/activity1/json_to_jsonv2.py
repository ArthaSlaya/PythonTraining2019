import json
import time

def logger(data):
	file=open("operations.log","a")
	string="Operation at"+data["position"]+" at "+str(time.time())+": "+data["err"]+"\n"
	file.write(string)
	file.close()

def check_attributes(data):
	for x in ["license","username","time","id"]:
		if(x not in data):
			logger({"position":"at attributes","err":(x+" Not Found")})
			return False
	return True

def validate(data):
	if(data["license"].isalnum() and len(data["username"])>6 and str(data["time"]).isdigit() and 0<data["id"]<100):
		return True
	logger({"position":"at Validation","err":""})
	return False

file=open("settings.json")
temp_data=file.read()
file.close()
data=json.loads(temp_data)

if(check_attributes(data)):
	if(validate(data)):
		if(0<data["id"]<50 and "-add" not in data["username"]):
			data["username"]+="-add"
			file=open("settings.json","w")
			file.write(json.dumps(data))
			file.close()
			logger({"position":"Persistence","err":"Changed"})
		else:
			logger({"position":"Persistence","err":"No Change"})
	else:
		print ("Validation Failed")
else:
	print ("Parameter Missing")
