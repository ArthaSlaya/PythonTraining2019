import threading
from multiprocessing import Queue
import time
import json
from flask import Flask,request

app = Flask(__name__)

def backup():
	print ("-----------------")
	print ("Backup Initiated")
	time.sleep(5)
	print ("Backup Completed")
	print ("-----------------")

def erase():
	print ("-----------------")
	print ("erase Initiated")
	time.sleep(3)
	print ("erase Completed")
	print ("-----------------")
	

@app.route("/job",methods=["POST"])
def hello1():
	inQ.put(request.form["data"])
	return json.dumps({"err":200})

inQ=Queue()

def worker():
	mapper={"backup":backup,"erase":erase}
	while(True):
		data=inQ.get()
		if(data in mapper):
			mapper[data]()
		else:
			print ("Invalid Option")

if __name__ == '__main__':
	t=threading.Thread(target=worker)
	t.start()
	app.run("0.0.0.0",5000)













