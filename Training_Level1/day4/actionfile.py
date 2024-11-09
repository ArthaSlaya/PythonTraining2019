'''
import callme
print ("Address of Erase in ACTION",callme.erase)
from callme import erase,backup
erase()     
# Remember the name of the function if printed contains the address of the function
# Importing twice is of no use in the same form, it will be imported only once
print ("Address of Explicit Import",erase)
# Aliasing when the name is big or you do not want to highlight the actual name
import callme as c
c.erase()

###################### TRY AT YOUR OWN RISK###################
def function1():   #100 assuming as initial address
	print ("Hi")
def function2():   #101
	print ("Hello")
def function3():   #102
	print ("OK")
flag=True
list_a=[]
# list_a=[function1,function2,function3]   # Possible!
list_a.append(function1)  # You are appending the address of the function and not calling the function
list_a.append(function2)
if(flag):   # Only if flag is true, add function3 in the forloop
	list_a.append(function3)
for x in list_a:
	x()     # X contains the address of the function appended, if you add () to the x, it becomes
			# a function call

'''
#########################Functions With Parameter ####################

'''
# Single Parameter
def printme1(data):
	print ("Data is ",data)
# Two Parameters
def printme2(data,data1):
	print ("Data is ",data,data1)
# Default Parameter
def printme3(data,data1=4):
	print ("Data is ",data,data1)
# Optional Parameter
def printmeoptional(*args):
	print (args)  # list
	for x in args:
		print (x)

printme1("Hello World")
printme2("Hello World",100)
printme3("Hello World",data1=45)
printmeoptional()

def printme4(data1,data2,*args,data3=4): 
	print (data1)
	print (data2)
	print (data3)
	print (args)
printme4(1,2,3,4,5,6,7,8,9,data3=10)   
	
a=4
b=4.6
c=True
d="hello World"
e=[]
print (isinstance(a,int))
print (isinstance(b,float))
print (isinstance(c,bool))
print (isinstance(d,str))
print (isinstance(e,list))
# isinstance()  # Next to be discussed
# isinstance("helloworld",str)
# isinstance(1,int)

def function1(data1,data2):
	if(not isinstance(data1,str)):
		return "Wrong Parameter"
	return  "Working"

print (function1("Hello World",1)

'''
'''
######################################DICTIONARY##########################################
dict_a={}
dict_a={"name":"batman","age":30,"place":"Gotham","married":False}
#print (dict_a["place"])
#print (dict_a["name"])
#print (dict_a["married"])
# Assigning a new key value pair
dict_a["suitcolor"]="black"
#print (dict_a)
# Editing the current value where is present
dict_a["suitcolor"]="blue"
#print (dict_a)
dict_a["skill"]="Jump"
if ("skill" in dict_a):
	print ("Skill Exist:",dict_a["skill"])
else:
	print ("Skill doesnt exist")
# Dictionary
for x,y in dict_a.items():
	print (x,y)
# list of reference
list_a=[1,2,3,4,5,6,7,8,9]
for x,y in enumerate(list_a):
	print (x,y)

# Removing from dict, if key exist it will remove and return the value
# if key doesnt exist, it will return the second parameter given (any datattype)
# if second parameter not given, and key doesnt exist, then execution will stop
print (dict_a.pop("skill",None))
'''
'''
# Properties of a dictionary
1)   index as to be string -> index is called key
2)   if you assign a key and a value -> it gets added
3)

'''
'''
# To Check if its a dictionary
print (isinstance(dict_a,dict))

# Questions
list_a=["america","india","africa","london","bangalore","chennai"]
if ("london" in list_a):
	print ("Exist")
else:
	print ("Doesnt Exist")

flag=True
for x in list_a:
	if(x=="london"):
		print ("Exist")
		flag=False
		break

if(flag):
	print ("Doesnt Exist")
# Character Matching
a="Hello World"
if("H" in a):
	print ("H exist")
# Word Matching case sensitive
if("Hell" in a):
	print ("Hell Exist")
'''
'''
# Set 1
x=open("script/operation.log","r")
data=x.read()  # read the complete file and store the content in data(local variable)
print (data) # Print the data
x.close()  # you have to close it, and rememeber close is a function

print ("Writing to the file")

y=open("script/operation.log","w")   # If file doesnt exist, it will be created
y.write("Hello World")
y.close()


file=open("me.txt","a")
file.write("\nOKAY BOSS")
file.close()



# FILE POINTER
# FILE VARIABLE
# MULTIPLE READ



# SET 2
with open("me.txt","r") as file:
	print (file.read())

with open("me.txt","w") as file:
	file.write("OKAY")

with open("me.txt","a") as file:
	file.write("GREAT")



'''
'''

a=[
	{
		"title": "MESSAGE",
		"msg" : {
				"from": "<RANDOMNUMBER>",
				"content": [
								{
								"msg": "MESSAGE",
								}
				
					]
		},
		"time" : <EPOCH TIME>
	},
	{
		"title": "<String>",
		"msg" : {
				"from": "<RANDOMNUMBER>",
				"content": [
								{
								"msg": "<String>",
								},
								{
								"msg": "<String>",
								},
								{
								"msg": "<String>",
								}
				
					]
		},
		"time" : <EPOCH TIME>
	},
	{
		"title": "<String>",
		"msg" : {
				"from": "<RANDOMNUMBER>",
				"content": [
								{
								"msg": "<String>",
								},
								{
								"msg": "<String>",
								},
								{
								"msg": "<String>",
								},
								{
								"msg": "<String>",
								}
				
					]
		},
		"time" : <EPOCH TIME>
	}
]







{
		"title": "<String>",
		"msg" : {
				"from": "<RANDOMNUMBER>",
				"content": [
								{
								"msg": "<String>",
								},
								{
								"msg": "<String>",
								},
								{
								"msg": "<String>",
								},
								{
								"msg": "<String>",
								}
				
					]
		},
		"time" : <EPOCH TIME>
	}
'''
import time
import json
from random import randint
temp_list=[]
for x in range(0,3):
	content_list=[]
	for x in range(0,randint(1,5)):
		content_list.append({"msg":"MESSAGE"})
	dict_a={
		"title": "ME",
		"msg" : {
				"from": randint(1000,20000),
				"content": content_list
		},
		"time" : time.time()
	}
	temp_list.append(dict_a)

data=json.dumps(temp_list,indent=4)
file=open("sample.json","w")
file.write(data)
file.close()


file=open("sample.json","r")
content=file.read()
file.close()

converteddata=json.loads(content)
print (converteddata[2]["msg"]["content"])


https://github.com/patrickpaip

python








