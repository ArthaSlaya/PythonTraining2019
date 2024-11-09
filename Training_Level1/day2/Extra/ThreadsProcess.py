from multiprocessing import Queue,Process
import threading
import time

def backup(path,loggerQ):
	time.sleep(2)
	loggerQ.put("Backup Success:"+path)

def erase(path,loggerQ):
	time.sleep(3)
	loggerQ.put("erase Success:"+path)

def printer(path,loggerQ):
	time.sleep(5)
	loggerQ.put("printer Success:"+path)

def logger(loggerQ):
	while(True):
		getlogData=loggerQ.get()
		with open("logs","a") as file:
			file.write(str(getlogData)+"\n")

def processor(inQ,outQ,loggerQ):
	mapper={
	"1001" : backup,
	"1002" : erase,
	"1003" : printer
	}
	while(True):
		data=inQ.get()
		if(data[0] in mapper):
			mapper[data[0]](data[1],loggerQ)
			outQ.put(data[0]+" Success")
		else:
			outQ.put("Command Not Found"+data[0])

def terminalInput(inQ,loggerQ):
	while True:
		data=input("Enter Your Command") # Blocking Call
		datasplit=data.split()
		if(len(datasplit)>=2):
			inQ.put([datasplit[0],datasplit[1]])
			loggerQ.put("Data Input Success")
		else:
			loggerQ.put("Issue with Input")

def terminalOutput(outQ,loggerQ):
	while True:
		data=outQ.get()
		print (data)
		loggerQ.put("TERMINALOUT:"+data)

if __name__ == '__main__':
	# Queues
	inQ=Queue()
	# Pass content  from Terminal to Process
	outQ=Queue()
	# Pass Process to Terminal
	loggerQ=Queue()
	# Logging Queue
	t=threading.Thread(target=terminalInput,args=(inQ,loggerQ,))
	t.start()
	t1=Process(target=processor,args=(inQ,outQ,loggerQ,))
	t1.start()
	t2=Process(target=logger,args=(loggerQ,))
	t2.start()
	t3=threading.Thread(target=terminalOutput,args=(outQ,loggerQ,))
	t3.start()