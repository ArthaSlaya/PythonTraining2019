import sys
sys.path.insert(0,"libraries")
import json
import csv
import time
import requests
from threading import Thread
from multiprocessing import Queue
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


def webserver(schedulerQ):
    from flask import Flask,request
    import json

    app=Flask(__name__)

    @app.route('/command')
    def commandManagenent():
        command=request.args["command"]
        schedulerQ.put(command)
        return json.dumps({"err":False,"message":"Command is in Queue"},indent=4)

    app.run("0.0.0.0",5000)

def scheduler(schedulerQ):
    import time
    def backup():
        print ("Backup Started")
        time.sleep(10)
        print ("Backup Complete")
    def erase():
        print ("erase Started")
        time.sleep(15)
        print ("erase Complete")
    def printer():
        print ("printer Started")
        time.sleep(30)
        print ("printer Complete")
    mapper={
        "1001" : backup,
        "1002": erase,
        "1003" : printer
    }
    while(True):
        data=schedulerQ.get()
        if(data in mapper):
            mapper[data]()




def main():
    schedulerQ=Queue()
    #websiteUptimeThread=Thread(target=website_uptime_monitor)
    #websiteUptimeThread.start()
    webserverThread=Thread(target=webserver,args=(schedulerQ,))
    webserverThread.start()
    schedulerThread=Thread(target=scheduler,args=(schedulerQ,))
    schedulerThread.start()

if __name__=='__main__':
    main()