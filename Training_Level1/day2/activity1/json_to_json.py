
import json
import time
# Read the File operation
file=open("settings.json")
data=file.read()
file.close()
# Convert to Dictionary from received String
op_content=json.loads(data)
# Check if attributes available, Note: Here you are checking against the indexes of Dictionary and not value
if("license" in op_content and "username" in op_content and "time" in op_content and "id" in op_content):
	# Check the validity of data as per conditions defined, Note: Here we are checking the value against the conditions
	if(op_content["license"].isalnum() and len(op_content["username"])>=6 and op_content["id"]<100 and op_content["id"]>0):
		# Check if "-add" contains inside the username
		if( 0<op_content["id"]<50 and "-add" not in op_content["username"]):
			op_content["username"]+="-add"
			# Since the data has been changed, the data in dictionary is converted to string and written to the file 
			with open("settings.json","w") as file:
				file.write(json.dumps(op_content))
			# Logging the data if change occured.
			with open("operation.log","a") as file:
				content="change: "+op_content["username"]+" at "+str(time.time())
				file.write(content+"\n")
		else:
			with open("operation.log","a") as file:
				content="No change: at "+str(time.time())
				file.write(content+"\n")
else:
	print ("Format Issue, Check Json File")
