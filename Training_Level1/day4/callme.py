import time
def backup():   #110
	print ("Starting Backup")
	time.sleep(5)
	print ("Backup Complete")
	return "DONE"

def erase():    #111
	print ("Erasing Folder Started")
	time.sleep(5)
	print ("Erase Complete")

print ("Address of Backup",backup)
print ("Address of Erase",erase)
