
'''
import json
dataset=None
from datetime import datetime

config={
    "configuration" : {
        "setting.conf" : "settings.json",
        "logger" : "operationx.log"
    }
}
# Reading the Target file
with open(config["configuration"]["setting.conf"]) as file:
    dataset=json.loads(file.read())


def logger(data):
    with open(config["configuration"]["logger"],"a") as file:
        file.write(str(data)+"\n")


def checkAttr(dataset,attributeSet):
    print (dataset)
    for x in attributeSet:
        if(x not in dataset.keys()):
            logger("Atribute Missing, {}".format(x))
            return False
    logger("All Attributes are present")
    return True

def validate(dataset):
    if(not dataset["license"].isalnum()):
        logger("License Has Issues")
        return False
    if(len(dataset["username"])<6):
        logger("Username Has Issues")
        return False
    if(not isinstance(dataset["time"],int)):
        logger("Time Has Issues")
        return False
    if(not 0<dataset["id"]<100):
        logger("ID Has Issues")
        return False
    logger("All Validation Successful")
    return True


        
if(checkAttr(dataset,["license","username","time","id"])):
    if(validate(dataset)):
        if(0<dataset["id"]<50 and "-add" not in dataset["username"]):
            dataset["username"]+="-add"
            logger("The Setting Configuration has changed {} {}".format(dataset["username"],str(datetime.now())))
            with open(config["configuration"]["setting.conf"],"w") as file:
                file.write(json.dumps(dataset,indent=4))
        else:
            logger("No Changes to the settings file")

'''
'''
command="sample.txt"
with open(command) as file:
    print (file.read())
'''
'''
try:
    pass
except:
    pass
else:
    pass
finally:
    pass
#ZeroDivisionError

def logsomething():
    print ("logged")

x=1
y=0
dict_a={}
list_a=[]
try:
    #print (dict_a["name"])
    #print  (list_a[99])
    print (x/y)
except ZeroDivisionError:
    print ("Zero Division")
except (KeyError,IndexError):
    logsomething()
except :
    print ("Error occured")
else:
    print ("All Good")
finally:
    print ("Finally Im done")
'''
'''
# raise error
import io

try:
    file=open("sample.txt")
    try:
        file.write("Hello World")
    except io.UnsupportedOperation:
        print ("Write Error")
    except Exception as e:
        print ("File Write Issue",e,e.__class__)
except:
    print ("File not Found")
else:
    file.close()
finally:
    print ("Finally")

# Custom Exception
class SaskenException(Exception):
    pass

try:
    print ("100")
    #raise
    raise SaskenException("What happened")
    raise IndexError("Something isnt right")
    print ("101")
except SaskenException as e:
    print ("EXCEPTION",e)
except IndexError:
    print ("Index Issue")
except:
    print ("Caught")
'''
# import sys
# print (sys.path)

# How to Import
# How to Import only a function
# Multiple imports have same instance (Singleton Pattern)
# Use sys.path to include extra directories
# 
'''
import json
with open("config.json","r") as file:
    config=json.loads(file.read())

import sys
sys.path.insert(0,"libraries")

from me import callme1,config
import me
import me as m

print (callme1)
print (me.callme1)
print (m.callme1)
'''

# import me
# import me
# me.callme1()
# print ("Hello")


'''
from threading import Thread
from multiprocessing import Queue
from time import sleep
def task1(loggerQ):
    while(True):
        loggerQ.put("Hello")
        sleep(1)

def task2(loggerQ):
    while(True):
        loggerQ.put("World")
        sleep(1)

def logger(loggerQ):
    while(True):
        data=loggerQ.get()
        with open("logger.log","a") as file:
            file.write(data+"\n")
        #print

def main():
    loggerQ=Queue()
    t1=Thread(target=task1,args=(loggerQ,))
    t2=Thread(target=task2,args=(loggerQ,))
    t3=Thread(target=logger,args=(loggerQ,))
    t1.start()
    t2.start()
    t3.start()

if __name__=="__main__":
    pass

'''
'''
import sys
sys.path.insert(0,"libraries")
import requests

r=requests.get("https://jsonplacdsadwde.com")
print (r.status_code)

int(time.time())

ERROR TYPE => Server Return Code | Server Not Accessible
SITE ID 
URL

Server Not Accessible,FACE,www.google.com,12

'''

'''
Question:
Create a Website uptime monitor which takes in an config file which
contains the interval and the url information.
if the website is not accessible or if the status code is other than
200 then the data has to be logged into a seperate CSV file with the 
current time (In Epoch format) as filename. 

#config.json
{
    "interval" : 1,
    "urls" : [{
        "SITE_ID" : "FACE",
        "URL" : "facebook.com"
    },
    {
        "SITE_ID" : "GOOGLE",
        "URL" : "google.com"
    }]
}

# Conditions:
if not 200, reason = Server Error Code
if failed, then reason = Server Not Reachable

#Target CSV Format:
reason,siteid,url,time
Server Not Reachable,FACE,facebook.com,2019-08-31 12:21:29.914741
Server Not Reachable,GOOGLE,google.com,2019-08-31 12:21:29.914903

'''

import json
import csv
import time
import requests
from threading import Thread
from datetime import datetime

def website_uptime_monitor():
    while(True):
        config={}
        try:
            with open("config.json") as file:
                config=json.loads(file.read())
        except:
            print ("File Error")
            time.sleep(10)
            print ("Trying to Read Config")
            continue
        else:
            urls=config.get("urls",[])
            result=[]
            for x in urls:
                try:
                    r=requests.get(x["URL"])
                    if(r.status_code!=200):
                        result.append({
                            "reason" : "Server Error Code",
                            "siteid" : x["SITE_ID"],
                            "url" : x["URL"],
                            "time" : str(datetime.now())
                        })
                except:
                    result.append({
                            "reason" : "Server Not Reachable",
                            "siteid" : x["SITE_ID"],
                            "url" : x["URL"],
                            "time" : str(datetime.now())
                    })
            if(len(result)!=0):
                filename="{}.csv".format(int(time.time()))
                with open(filename, 'w') as writeFile:
                    fields = ['reason', 'siteid','url','time']
                    writer = csv.DictWriter(writeFile, fieldnames=fields)
                    writer.writeheader()
                    writer.writerows(result)
        
        # If interval not defined inside the file, then it defaults to 1min
        interval=int(config.get("interval",5))
        if(interval==0):
            print ("Very Small Interval, Defaults to 1")
            interval=1
            # Write to CSV
        time.sleep(60*interval)

def main():
    websiteUptimeThread=Thread(target=website_uptime_monitor)
    websiteUptimeThread.start()

if __name__=='__main__':
    main()


import requests
r=requests.get("http://localhost:5000/")
print (r.text)











