'''
############################### FUNCTIONS ##############################################
#=============================================
#           Functions Revisited
#=============================================

# Def is a keyword, f1 contains the address of function
def f1():
	print ("Hello World")  # prints to standard output
print (f1())  # Returns None since function isnt returning anything

def f2():
	print ("Hello")
	return 1,2   # The multiple returns are converted into tuple and returned
x,y=f2()  # Thus one to one mapping occurs x->1 and y->2
print (x,y)

def f3(a,b=4):  # Note: The default parameter and postional cannot be interchanged.
	print ("Hello",a,b)
f3(2)  # Minimum number of parameter to be sent is 1 since b is an default parameter

#=============================================
#      Functions as parameters and returns
#=============================================

###
###
# Value of a is address of f2
# To that address you are giving a call
def f1(a):   # Variable a contains the address of f2 function
	a()   # To any variable containing address of a function you can give a call by attaching ()
	print ("Variable",a)  
def f2():
	print ("Something")

f1(f2)


###
###
def f1():
	return f2

def f2():
	print ("Hello World")

g=f1  # Attaching address of function to another variable
g()
# Can we do this?
f1()()   # Divide and Conquer

# Returning Inner Function and Executing Globally
def f1():
	def f2():
		print  ("Hello World")
	return f2

d=f1()  # The Outer Function returns the address of inner function but doesnt execute it
d()  # Executing the inner function
'''
############################## END OF BASIC FUNCTIONS #################################


################################ CLOSURE FUNCTION ###################################
'''
# Closure
# The Inner functions keep the context of the enclosing function 
def f1(a):
	def f2():
		print  ("Hello World",a)
	return f2
d1=f1(2)  
d2=f1(4)
# In the above code, observe the parameters are different
print (d1,d2)  # Observe the Address
d1() 
d2()
'''
################################ END OF CLOSURE ####################################

# def f1():
# 	print ("Hello")

# def f2():
# 	print ("Okay")

# list_a=[f1,f2]
# for x in list_a:
# 	x()

# # Map the Functions Address to the dictionary
# mapper={
# 	"1001" : f1,
# 	"1002" : f2
# }
# # To Iterate a dictionary
# mapper.values()  #Returns all the values as a list
# mapper.keys() # Returns all the keys as a list
# for x,y in mapper.items():
# 	print (x,y)
# # Attaching to List Dynamically and executing it as required
# list_t=[]
# list_t.append(mapper["1001"])
# print (list_t)

# command="1010"

# if(command in mapper):
# 	mapper[command]()
# else:
# 	print ('Invalid Command')

# commandlist=["1002","1010","1001"]
# for x in commandlist:
# 	if (x in mapper):
# 		mapper[x]()
# 	else:
# 		print ("Invalid Command")



# list_b=[1,2,3,4,5,6,7]
# for x,y in enumerate(list_b):  
# 	print ("At Index {}, Value is {}".format(x,y))


# list_b=[1,2,3,4,5,6,7]
# for x in enumerate(list_b):  
# 	print ("At Index {}, Value is {}".format(x[0],x[1]))




# def f1(a,*args,b=4):
# 	print ("a",a)
# 	print ("b",b)
# 	print ("args",args)
# 	for x in args:
# 		print (x)

# f1(12,3,4,5,6,7,7,b=6)

# def f2(**kwargs):
# 	print (kwargs)
# f2(name="batman",age=100)

# def f3(*args):
# 	print (args)
# f3(1,2,3,4,5,6)


# def f4(a,*args,b=4,**kwargs):
# 	print ("a",a)
# 	print ("b",b)
# 	print ("args",args)
# 	print ("kwargs",kwargs)
# f4(1,2,3,4,5,6,name="batman")

# # Decorator
# from datetime import datetime
# import time
# from deco import timerestrict,timing

# @timing
# def f2(a,b):
# 	time.sleep(2)
# 	print ("Hello World2",a,b)
# 	return "Okay"

# # output=f2(1,2)
# # print (output)

# def printme():
# 	pass

# print (f2.__name__)
# print (printme.__name__)

################################# Lazy Evaluation Techniques#######################

# f=iter(range(4))
# print (next(f))  # Use this 
# print (f.__next__()) # Or this
# print (f.__next__())
# print (f.__next__())

# g=[1,2,3,4,5,6]
# g=iter(g)
# print (next(g))

# for x in g: # Why dont we convert this into iter?
# 	print (g)

# g=[1,2,3,4,5,6]
# iter_obj=iter(g)
# while(True):
# 	try:
# 		data= iter_obj.__next__()
# 		print (data)
# 	except StopIteration:
# 		break

# g=[1,2,3,4,5,6]
# for x in g:
# 	print (x)

# class PowTwo:
# 	def __init__(self,max=0):
# 		self.max=max
# 		print ("Started",self.max)

# 	def __iter__(self):
# 		self.n=0
# 		return self
# 	def __next__(self):
# 		if(self.n<=self.max):
# 			result = 2**self.n
# 			self.n+=1
# 			return result
# 		else:
# 			raise StopIteration
 
# g=PowTwo(3)
# i=iter(g) 
# print (next(i))
# print (i.__next__())
# print (i.__next__())
# print (i.__next__())

# for x in PowTwo(10):
# 	print (x)

# class PowTwoInfi:

# 	def __iter__(self):
# 		self.n=0
# 		return self
# 	def __next__(self):
# 		result = 2**self.n
# 		self.n+=1
# 		return result

# f=PowTwoInfi()
# h=iter(f)
# for x in f:
# 	print (x)

# def PowTwo(max=0):
# 	current=0
# 	while(current<max):
# 		yield 2**current
# 		current+=1

# f=PowTwo(5)
# print (next(f))
# print (next(f))
# print (next(f))
# print (next(f))
# print (next(f))

# for x in PowTwo(5):
# 	print (x)

# def sample():
# 	yield 1
# 	yield 2
# 	yield 3

# for x in sample():
# 	print (x)


# squares=[]
# for x in range(0,20):
# 	squares.append(x**2)
# print (squares)

# listsquares=[x**2 for x in range(0,20)]
# print ("Listquars",listsquares)

# flistsquares=[x**2 for x in range(0,20) if x%2==0]
# print ("fListquars",flistsquares)

# # filteredsquares=[]
# # for x in range(0,20):
# # 	if(x%2!=0):
# # 		continue
# # 	filteredsquares.append(x**2)
# # print (filteredsquares)
# from random import randint
# temp_a=[]
# for x in range(100):
# 	temp_a.append([randint(0,10),randint(0,10)])
# print (temp_a)

# randomList=[[randint(0,10),randint(0,10)] for x in range(100)]

# addList=[]
# for x in range(10):
# 	for y in range(20):
# 		if((x*y)%2==0):
# 			addList.append(x*y)

# y=(x*y for x in range(10) for y in range(20) if((x*y)%2==0))

# for x in y:
# 	print (x%10)


# def multiply(x):
# # 	# operatio
# 	return x*x

# f=multiply
# print (f)
# print (f(5))

# f=lambda x: x*x
# # print (f)
# # print (f(5))

# list_a=[1,2,3,4,5,6]
# list_b=list(map(multiply,list_a))
# print (list_b)
# list_b=list(map(lambda x: x*x,list_a))
# print (list_b)

# list_a=[1,2,3,4,5,6]
# list_c=list(filter(lambda x: x%2==0,list_a))
# print (list_c)

# print (list(filter(lambda x: x%2==0,map(lambda x:x**3,range(100))




# class PowTwo:
# 	def __init__(self,max):
# 		self.max=max
# 	def __iter__(self):
# 		self.n=0
# 		return self
# 	def __next__(self):
# 		if(self.n<self.max):
# 			result=2**self.n
# 			self.n+=1
# 			return result
# 		else:
# 			raise StopIteration


# g=PowTwo(4)
# h=iter(g)
# print (next(g))
# print (next(g))
# print (next(g))
# print (next(g))


# list
# str
# dict
# for x in PowTwo(6):
# 	print (x)

# def sample(max):
# 	counter=0
# 	while(counter<max):
# 		result=2**counter
# 		counter+=1
# 		yield result

# for x in sample(5):
# 	print (x)

# list_a=[2,3,4,5,6]
# g=lambda x: x**2
# h=map(g,list_a)
# print (next(h))
# print (next(h))
# print (next(h))
# print (next(h))

# listsquares=[x**2 for x in range(0,20)]
# print (listsquares)

# for x in (x**2 for x in range(0,20)):
# 	print (x)

# from time import time
# import functools

# def wrapper(func):
# 	@functools.wraps(func)
# 	def inner(*args,**kwargs):
# 		a=time()
# 		ret=func(*args,**kwargs)
# 		print ("Excecution Time is",time()-a)
# 		return ret
# 	return inner

# @wrapper
# @wrapper
# @wrapper
# def f1():
# 	print ('Good Morning')
# 	return "HelloWorld"

# print (f1())
# print (f1.__name__)

################################ COUNTER #######################################
'''
dict_a={}
list_a=['A','A','B','C','C','C']
for x in list_a:
	if x in dict_a:
		dict_a[x]+=1
	else:
		dict_a[x]=1
print (dict_a)

from collections import Counter
# Outcomes
print (Counter(list_a))
print (Counter({'A': 2, 'B': 1, 'C': 3}))
print (Counter(A=2,B=3,C=5))
# How to Create an Empty Counter
f=Counter()
print (f)
# How to Add to an Counter
f.update("abcdeeea")
f.update("abcdeeea") # string Value
f.update({'abc':4})  # It can take an dictionary/List Too
print (f)
# How to Access From the Counter
print (f['a'])  # Note: if an key is not present then default value is 0 
# How to get back the elements from the Counter
print (list(f.elements()))
# Consider you have a file with words filled with it
# Task is to calculate the most common word used
with open("sample.txt","r") as file:
	content=list(file.read()) # For Letters
	# content=file.read().split() # For Words Delimiter is space
	g=Counter(content)
	print (g.most_common(3)) # Most Common Letters Used

# Single Liner for the above
with open("sample.txt","r") as file:
	print (Counter(list(file.read())).most_common(3)) 

# Operations
# Subtract
c1=Counter(A=4,B=5,C=6)
c2=Counter(A=2,B=4)
# c3=c1-c2  # Creating an new Counter c3
# print (c3) 
# #If need to preserve the result in c1 then
# c1.subtract(c2)
# print (c1)

c3=c1|c2  # Creating an new Counter c3
print ("Union",c3)
c3=c1&c2  # Creating an new Counter c3
print ("Intersection",c3) 
c3=c1+c2  # Creating an new Counter c3
print ("Addition",c3)  
'''

######################## END OF COUNTER ######################
'''
####################### NAMED TUPLES #######################
# Useful for DataScience and BigData

from collections import namedtuple

student=namedtuple('Student',['name','age','place'])
s1=student("Batman",100,"gotham")
print (s1)
# s2=student("Superman")   # Gives Error,Need to Adhere to the schema
s3=student(age=400,name="python",place="Fideliy")
print (s3)
# How to Access??????
# Yon can access using integer Index and also the string index
print (s3[0])
print (s3.name)
# print (s3['name']) # s3 is an object and thus name is an instance variable
# So How do you access by string Index
print (getattr(s3,'name'))  # Is an inbuilt function in Python under class

# Functions
# When the Input is a list
list_a=["Ironman",50,"Bangalore"]
s4=student._make(list_a)
print (s4)
# When the Input is a dict
dict_a={'name':'antman','age':20,'place':'local'}
s5=student(**dict_a)
print (s5)
# Converting into an orderedDict and eventually to a dict
print (dict(s5._asdict()))
# Replacing a Varible in a student Object saty s5 from antman to wasp
s5=s5._replace(name="Wasp") # Returns the new object of students
print (s5)
# To know all the fields
print (s5._fields)  # Returns as a Tuple
'''
'''
######################### DEQUEUE ##########################
# Are ThreadSafe
from collections import deque

# Empty Deque
d=deque()
print (d)
# Filled With String
d=deque('abcde')
print (d)
# Left Side
print (d[0])
# Rigth Side
print (d[-1])
#Remove By Value
d.remove('c')
print (d)
# Popping up -> Default is right side
print ("Popped Value From Right",d.pop())
print ("Content",d)
# Popping up
print ("Popped Value from Left",d.popleft())
print ("Content",d)
# Extending from Right and Left
d.extend('efg')
print ('After Extending from Right',d)
d.extendleft('123')
print ("After Extending from Left",d)  # Observe the outcome
# OUTPUT: deque(['3', '2', '1', 'b', 'd', 'e', 'f', 'g'])

# Rotating the DQueue
r=deque(range(10))
print ("InitialValue",r)
# Rotate to the Right
r.rotate(2)
print ("RightRotate",r)
# Rotate to the Left
r.rotate(-2)
print ("RightRotate",r)

# Limiting the Size
limited= deque(maxlen=3)
print (limited)
limited.extend('123')
print (limited)
limited.extend('4') # Observe the Outcome
print (limited)

# Extras
f=deque([{'name':'batman'},{'age':30}])
print (f)
f.pop()
print (f)

########################## END OF DQUEUE ######################
'''
'''
#############################LOGGING###########################

# # Basic Way But what can be the liability?
# from datetime import datetime
# def logger(data):
# 	with open("logs","a") as file:
# 		file.write("{}: {} \n".format(str(datetime.now()),str(data)))

# logger("Its Not Working")

# #logging to the console
# import logging
# # Setting the Configuration
# logging.basicConfig(level=logging.DEBUG, 
# 	format='%(name)s - %(levelname)s - %(message)s')
# # Levels :  debug->info->warning->error->critical
# logging.debug('Debugging Level')
# logging.info('Info Level')
# logging.warning('Warning Level')
# logging.error('Error Level')
# logging.critical('Critical Level')

#logging to a file
import logging
# Setting the Configuration
logging.basicConfig(level=logging.DEBUG,filename='app.log',
	filemode='a',format='%(name)s - %(levelname)s - %(message)s')
# Levels :  debug->info->warning->error->critical
logging.debug('Debugging Level')
logging.info('Info Level')
logging.warning('Warning Level')
logging.error('Error Level')
logging.critical('Critical Level')

# How to Capture the Stack Trace
try:
	a=1/0
except Exception as e:
	logging.error("Exception Occured",exc_info=True)
	pass

#######################LOGGING BASICS END ##########################
'''
'''
#######################SUB PROCESS ###############################

import subprocess
subprocess.run(['dir'],shell=True)

import subprocess
try:
	import requests
except ModuleNotFoundError:
	subprocess.run(['pip','install','requests'],shell=True)
	import requests

import subprocess
r=subprocess.run(['python','test.py'],shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
print (r.stdout.decode('utf-8'))
print (r.stderr.decode('utf-8'))

######################## END OF SUBPROCESS #######################
'''

######################## THREADS #################################
'''
from time import sleep
from threading import Thread,current_thread

# No Global Variables

def printinfinite1(alias):
	counter=0
	while(True):
		print ("CounterValue {}: {}".format(alias,counter))
		print ("Name of Thread",current_thread().getName())
		counter+=1
		sleep(1)

def printinfinite2(alias):
	counter=0
	while(True):
		print ("CounterValue {}: {}".format(alias,counter))
		print ("Name of Thread",current_thread().getName())
		counter+=1
		sleep(2)

def main():   # User Initiated Process
	t1=Thread(target=printinfinite1,name="Batman",args=("thread1",))
	t1.daemon=True  # Make sure its not handling an files
	t1.start()
	t2=Thread(target=printinfinite2,name="Superman",args=("thread2",))
	t2.daemon=True
	t2.start()
	sleep(6)
	print ("Main Thread has ended")

if __name__ == '__main__':
	main()
'''
'''

from threading import Thread,current_thread
import threading
from time import sleep
from multiprocessing import Queue
from random import randint

def producer(dataQ):
	while(True):
		dataQ.put("From {} Value:{}".format(current_thread().getName(),str(randint(0,100))))
		sleep(1)

def consumer(dataQ):
	counter=0
	while(True):
		data=dataQ.get()
		if(counter==2):
			break
		counter+=1
		print ("Thread:{} Value=>>{}".format(current_thread().getName(),data))

def main():
	threadlist=[]
	dataQ=Queue()
	t1=Thread(target=producer,name="producer1",args=(dataQ,))
	threadlist.append(t1)
	t1.start()
	t1=Thread(target=producer,name="producer2",args=(dataQ,))
	threadlist.append(t1)
	t1.start()
	t2=Thread(target=consumer,name="consumer1",args=(dataQ,))
	threadlist.append(t2)
	t2.start()
	t2=Thread(target=consumer,name="consumer2",args=(dataQ,))
	threadlist.append(t2)
	t2.start()

	while(True):
		for x in threadlist:
			if(x.isAlive()):
				print ("{} Is Alive".format(x.name))
			else:
				print ("{} Is Dead".format(x.name))
		sleep(2)

	# Unreachable
	import threading
	# Get the name of all threads
	for t in threading.enumerate():
		print (t.getName())

if __name__ == '__main__':

	main()
'''

'''

import threading
import time

def wait_for_event1(e):
	print ("I am Waiting1")
	event_is_set=e.wait()
	print ("I just Executed1")

def wait_for_event2(e):
	print ("I am Waiting2")
	event_is_set=e.wait()
	print ("I just Executed2")

def nonblocking(e):
	while(not e.is_set()):
		print ("Okay")
		time.sleep(1)
	print ("Completed")

def timeevent(e):
	time.sleep(5)
	e.set()

def main():
	e=threading.Event()
	t1=threading.Thread(target=wait_for_event1,args=(e,))
	t1.start()
	t1=threading.Thread(target=wait_for_event2,args=(e,))
	t1.start()
	t1=threading.Thread(target=nonblocking,args=(e,))
	t1.start()
	t2=threading.Thread(target=timeevent,args=(e,))
	t2.start()

if __name__ == '__main__':
	main()
'''

'''
import threading
import time

def worker1(lock):
	with lock:
		print ("Accessing Variable: Worker1")
		time.sleep(2)

def worker2(lock):
	with lock:
		print ("Accessing Variable: Worker2")
		time.sleep(3)

def main():
	lock=threading.Lock()
	t1=threading.Thread(target=worker1,args=(lock,))
	t1.start()
	t2=threading.Thread(target=worker2,args=(lock,))
	t2.start()
	


if __name__ == '__main__':
	main()

'''

'''

import multiprocessing
from random import randint
import time

def do_calculation(data):
	for x in range(10000000): pass
	return data*2

def start_process():
	print ("Starting",multiprocessing.current_process().name)

def main():
	inputs=list(range(10))

	pool_size= 16
	pool=multiprocessing.Pool(processes=pool_size,initializer=start_process)
	pool_output=pool.map(do_calculation,inputs)
	pool.close()
	pool.join()
	print ("output:",pool_output)
if __name__ == '__main__':
	main()

'''

######################## END OF THREADS ##########################

'''
# Website Uptime Monitoring

import requests
import time
import logging
import threading
def uptimeCheck():
    urls=["https://google.com","https://gohhhhqdsfasadadsasad.com"]
    while(True):
        for x in urls:
            try:
                r=requests.get(x)
                if(not (r.status_code==200 or r.status_code==304)):
                    raise
            except Exception as e:
                logging.error("WebSite: {} is Down".format(x))
        time.sleep(30)

def main():
    t=threading.Thread(target=uptimeCheck)
    t.daemon=False
    t.start()
    
if __name__=='__main__':
    main()
    
'''

'''
# Read JSON, Filter and Give Result
import requests
ids=[]
url="https://jsonplaceholder.typicode.com/comments"
for x in requests.get(url).json():
	if (x['email'][-4:]=='.biz'):
		ids.append(x['id'])
print (ids)
'''
'''
# Read JSON, Filter and Give Result using List Comprehension
from requests import get
url="https://jsonplaceholder.typicode.com/comments"
# Get all IDs with email contains .biz as domain type
ids1=[x['id'] for x in get(url).json() if (x['email'][-4:]=='.biz')]
print (ids1)
'''
'''
# Get data from CommandLine

import sys
from requests import get

if(len(sys.argv)==1):
	print ("Usage is python filename url")
	sys.exit(1)
else:
	# Read JSON, Filter and Give Result using List Comprehension
	# Get all IDs with email contains .biz as domain type
	ids1=[x['id'] for x in get(sys.argv[1]).json() if (x['email'][-4:]=='.biz')]
	print (ids1)
'''

'''
# Add Other Path for Libraries
import sys
sys.path.insert(0,'libraries')
import requests
# Read JSON, Filter and Give Result using List Comprehension
from requests import get
url="https://jsonplaceholder.typicode.com/comments"
# Get all IDs with email contains .biz as domain type
ids1=[x['id'] for x in get(url).json() if (x['email'][-4:]=='.biz')]
print (ids1)

# Adding Proxy to PIP under Windows
pip install --user --proxy=<ProxyIP> requests --target .
'''

'''
from flask import Flask,request
import json
app=Flask(__name__)

@app.route('/',methods=["GET","POST","PUT"])
def rootRoutine():
	if("name" in request.args):
		dict_a={'err':False,'name':request.args['name'],'age':40}
		return json.dumps(dict_a,indent=4)
	else:
		return json.dumps({"err":True})

# Accepting Post Request
@app.route('/users',methods=["POST"])
def rootRoutine1():
	print (request.form)
	return "I am USer"

# Accepting URL based Request
@app.route('/user/<username>',methods=["GET"])
def rootRoutine2(username):
	return username

if __name__ == '__main__':
	app.run("0.0.0.0",5000)

'''
'''
import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()

try:
# Create table
	c.execute('CREATE TABLE users
    	         (name text, age text, place text)')
	conn.commit()
except  Exception as e:
	print ("Table Exist")
# # Insert a row of data
dataset=[('catwoman','30','qwerty'),('flash','20','Dontknow')]
c.executemany("INSERT INTO users VALUES (?,?,?)",dataset)
# # Save (commit) the changes
# conn.commit()

f=c.execute("SELECT * from users")
for x in f:
	print (x)
# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()

'''

'''
from flask import Flask,request,g
import sqlite3
import json
app=Flask(__name__)

conn = sqlite3.connect('example.db')
c = conn.cursor()
try:
# Create table
	c.execute('CREATE TABLE users (name text, age text, place text)')
	conn.commit()
except  Exception as e:
	print ("Table Exist")

def getDB():
	if not hasattr(g,"sqlite"):
		conn = sqlite3.connect('example.db')
		c = conn.cursor()
		g.sqlite=c
		g.conn=conn
	return getattr(g,"conn"),getattr(g,"sqlite")


@app.route('/getuser',methods=["GET"])
def manipulate():
	conn,c=getDB()
	data=[{'name':x,'age':int(y),'place':z} 
	for x,y,z in c.execute("SELECT * from users")]
	return json.dumps(data,indent=4)

@app.route('/putuser',methods=["POST"])
def manipulate1():
	check=["name","age","place"]
	for x in check:
		if(x not in request.form):
			return json.dumps({'err':True})
	conn,c=getDB()
	c.execute("INSERT INTO users VALUES(?,?,?)",
		(request.form['name'],request.form['age'],request.form['place'],))
	conn.commit()
	return json.dumps({'err':False})

if __name__ == '__main__':
	app.run("0.0.0.0",5000)

'''

############################ END OF FLASK AND SQLITE #######################





