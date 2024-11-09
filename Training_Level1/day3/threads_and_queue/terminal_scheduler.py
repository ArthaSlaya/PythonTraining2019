from multiprocessing import Queue
import threading
import time

def backup():
	print ("-----------------------")
	print ("Backup Process Initiated")
	# Simulating Work Done
	time.sleep(4)
	print ("Backup Process Complete")
	print ("------------------------")

def maintain():
	print ("-----------------------")
	print ("Maintainance Process Initiated")
	# Simulating Work Done
	time.sleep(6)
	print ("Maintainance Process Complete")
	print ("------------------------")

def terminal_listener(common_queue):
	while(True):
		common_queue.put(input("Enter the Command"))

def command_executioner(common_queue):
	process_mapper={
		"backup" : backup,
		"maintain" : maintain
	}
	while(True):
		data=common_queue.get()
		if( data=="maintain" or data=="backup"):
			process_mapper[data]()

if __name__ == '__main__':
	common_queue=Queue()
	t1=threading.Thread(target=terminal_listener,args=(common_queue,))
	t1.start()
	t2=threading.Thread(target=command_executioner,args=(common_queue,))
	t2.start()