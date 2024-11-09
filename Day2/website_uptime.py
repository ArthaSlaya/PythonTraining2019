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