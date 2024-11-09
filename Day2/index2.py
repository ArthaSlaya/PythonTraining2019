'''
a=4
b=4
if(a is 4 or b is 4):
    print ("yes")
else:
    print ("No")

data=True
data=not data
'''
'''
target=100
count=0
while(count<target):
    print (count)
    # No Unary Increment/Decrement
    count+=1

a="Hello World"
l=len(a)
index=0
while(index<l):
    print (a[index])
    if(index==4):
        break
    index+=1
else:
    print ("Completed Iteration")

'''

'''
a="Hello"
b="World"
print (a+b)
print (a,b)

username="Batman"
string="Hello {}, How are you? {}".format(username,4)
print (string)
'''

'''
a="Hello World"
for x,y in enumerate(a):
    print (x,y)
else:
    print ("Called")

# Do something n times
for x in range(50,100,1):
    print (x)
'''


'''
a=4
list_a=[1,2,a]
print (list_a)
list_b=list_a
a=6
list_a=[1,a]
print (list_a)

name            address         value       ref
--                100             4           0
--           101            [,#103,#100]        1
--               102              1          1
--               103              2          1
a                104               6          2
list_b           107               #101       1
list_a           105              [#106,#104]          1
--               106              1           1

'''

'''
list_a=[1,2,3,4,5]
l=len(list_a)
index=0
flag=False
while(index<l):
    if(list_a[index]==4):
        Flag=True
        break
    index+=1
if(not Flag):
    pass
else:
    print ("Do Something")

list_a=[1,2,3,4,5]
l=len(list_a)
index=0
while(index<l):
    if(list_a[index]==4):
        break
    index+=1
else:
    print ("Do Something")

'''

'''
list_a=[]
print (list_a)
print (list_a[0])
print (list_a[-1])
print (list_a[:3])
list_b=list_a[:] # Cloning 
print (list_b)
list_b[0]="hello World"
print (list_b)
print (list_a)
'''
'''
list_a=[]
list_a.append([1,2,3])
list_a.append([4,5,6])
list_a.append([7,8,9])
list_a.insert(0,["ID","Name","Age"])
print (list_a)
'''
'''
list_b=[1,2,3,4,5]
# Remove By Value
list_b.remove(5)
# Remove by Index
del list_b[0]

# Merging
list_c=[1,2]
list_d=[3,4]
list_f=list_c+list_d
# Merging to Existing List
list_c.extend(list_d)
print (list_c)
'''
'''
# Shallow Copy
list_a=[1,2]
list_b=[2,3]
list_a.append(list_b.copy())
list_a.append(list(list_b))
list_a.append(list_a[:])
print (list_a)
list_b[0]="Edited"
print (list_b)
print (list_a)
'''
# From Library Copy get a function called deepcopy
'''
import copy
list_a=[1,2]
list_b=[3,4]
list_c=[5,6]
list_b.append(list_c)
list_a.append(copy.deepcopy(list_b))
print (list_a)
list_b[0]="Hello World"
list_c[0]="Okay"
print (list_a)

# Activity Time
from random import randint
g=randint(0,100)
'''
Create a list of list where in each internal list
must contain 2 random numbers
And the total number of internal list
should be 100
'''


from random import randint

temp=[]
alpha="abcde"
for x in range(0,10):
    string=""
    for x in range(6):
        string+=alpha[randint(0,len(alpha)-1)]
    temp.append([string,randint(0,100)])  
print (temp)

x=5
y=7
x,y=y,xx
print (x,y)x
'''


'''
Topics for the Day
Dictionary
Functions
   -> Normal
   -> HOC
   -> Arguments
   -> Scope
Dictionary to Function Mapping
List to Function Mapping
Tuple
Solving Relations
JSON
File Operation
'''

dict_a={
    "name":"batman",
    "age":25,
    "place":"gotham"
    }
print (dict_a["place"])
# print (dict_a["fight"])

# Get a Default when key is not present
fight=False
if ("fight" in dict_a):
    fight=dict_a["fight"]
# Get a Default when key is not present
fight=dict_a.get("fight",False)

# Read the keys and values as list
print(list(dict_a.keys()))
print (list(dict_a.values()))

# If key is not present and you are attaching a value
# to the key, then the key:value pair gets added to dict
# If key is present, then the value will overwrite the 
# existing value
dict_a["name"]="Ironman"
dict_a["suits"]=10
print (dict_a)

# Delete, Throws key error if key is not present
del dict_a["suits"]
# Safe Delete
if("suits" in dict_a):
    del dict_a["suits"]

# If key is present, the value is returned and deleted from
# the dictionary. If key is not present, then NO NAME as 
# default is returned. 
# del dict_a["name"] # Use to get result as No Name
name=dict_a.pop("name","NO NAME")
print (name)


dict_a={
    "name":"batman",
    "age":25,
    "place":"gotham"
    }
# Items is a function which returns both key value 
# items() is lazily evaluated, But Why?
# We have keys() and values() to do the same, but not 
# efficient
for x,y in dict_a.items():
    print ("The Key is {} and the value is".format(x,y))
    print (x,y)

'''
########### TUPLE ##############

x=4
y=6
x=y,x
# Type is tuple
print (type(x))

# Declaring a Tuple
tuple_a=(1,2,)
# Converting a list to a tuple
list_a=[1,2,3,4,5]
tuple_b=tuple(list_a)
print (tuple_b)
# Demonstrating property sharing of list and tuple
# Both work the same way
list_g=[1,2]
a,b=list_g
print (a,b)
# Utilizing the same property to ease readability
outcome=[["batman",34],["superman",23]]
for name,age in outcome:
    print ("The Name is {} and the Age is {}".format(name,age))

'''


######### FUNCTIONS ############

'''
def IntegerCheck(x):
    if(isinstance(x,int)):
        print ("Its an Integer, All good")
    else:
        print ("Not Good")
    return "Hello World"

result=IntegerCheck(10)
print (result)  

# Multiply String
string="Hello"
print (string*10)

# Why none, on append. It doesnt have a return statement
list_a=list()
print (list_a.append("Something"))

'''
'''
# Passing function address as parameter
def f1(x):
    x()
    print ("F1 Function")

def f2():
    print ("F2 Function")

f1(f2)

'''
'''
# Returning a functions address

# Higher Order Functions
def f1():
    print ("F1 Function")
    return f2

def f2(x):
    print ("F2 Function")

# a=f1()
# a()

f1()(1)
'''

'''
# Inner Functions

def f1():
    def innerFunction1():
        print ("I am inner Function")
    def innerFunction2():
        print ("I am inner Function")
    print ("Something")
    return innerFunction

a=f1()
a()


# Decorators

import time
from datetime import datetime

def timing(f):
    def inner():
        starttime=time.time()
        f()
        endtime=time.time()
        print("Time Taken is {}".format(endtime-starttime))
    return inner

def permission(f):
    def inner():
        if(14<datetime.now().hour<16):
            f()
        else:
            print ("You are not allowed to call")
    return inner


@timing
def xyz():
    print ("Start")
    time.sleep(2)
    print ("Stop")

@permission
@timing
def abc():
    print ("Start")
    time.sleep(3)
    print ("Stop")

abc()

#timing(xyz)()
#timing(abc)()



def f1(x):
    def inner():
        print (x)
    return inner

q=f1(3)
print (id(q))
print (q)
w=f1(3)
print (id(w))
print (w)

def createDB(url):
    def connect():
        print ("URL",url)
    return connect

conn=createDB("postgres://localhost:5432/mydb")

cursor=conn()

'''

'''
# Attaching functions to Dictionary

def backup():
    print ("Backup")
def erase():
    print ("Erase")
def printer():
    print ("Printing")

mapper={
    "1001" : backup,
    "1002" : erase,
    "1003" : printer
}

command=["1001","1100","1002","1001","1003"]

for x in command:
    if(x in mapper):
        mapper[x]()
    else:
        print ("Command Not Found {}".format(x))


'''
'''

def f1(a,b=4,c=5):
    print ("a is",a)
    print ("B is ",b)
    print ("C is ",c)

f1(1,c="String",b="Yes")

def f2(*args):
    print (args)
    for x in args:
        print (x)

f2(1,2,"HelloWorld")

def f3(a,b=4,*args):
    print ("a is",a)
    print ("b is",b)
    print ("args is ",args)

f3(10,10,10,1,2,3,5,6,7,8,9)

def f4(**kwargs):
    print (kwargs)

f4(name="batman",age=50)

def f5(a,*args,b=4,**kwargs):
    print ("a is",a)
    print ("b is",b)
    print ("args is ",args)
    print ("kwargs is ",kwargs)

f5(10,9,1,2,3,4,5,5,name="batman",b="Sleeping")
'''
'''
################## Function Scope | Variables #########

a=4
def f1():
    a=5   #Intensional
    def inner():
        nonlocal a
        a=6
        print ("Inner",a)
    inner()
    print ("F1",a)

f1()
print ("GLOBAL A:",a)
'''
'''
from random import randint

def createName(length):
    alpha="abcde"
    temp=""
    for x in range(length):
        temp+=alpha[randint(0,len(alpha)-1)]
    return temp


def dummyDataGenerator(records,nameSize):
    temp=[]
    for x in range(records):
        temp.append({
            "name" : createName(nameSize),
            "age" : randint(0,100)
        })
    return temp

data=dummyDataGenerator(10,6)
print (data)

import json

dict_a=[
    {
        "name" : "Antman",
        "time" : 5344236456542,
        "seen"  : True,
        "badhabits" : None
    }
]

print (dict_a)
convertedData=json.dumps(dict_a)
print (convertedData)

result= json.loads(convertedData)
print (result)

<msg>
        <title> Hi </title>
        <time>  1534232323 </time>
        <seen>  false  </seen>
   </msg>
'''

file=open("sample.txt","r")
data=file.read()
print (data)
file.close()

# Yet another way to read it

with open("sample.txt","r") as file:
    data=file.read()
    print (data)

# Write to a file
# If the file is not present, then the file would be created
# if the file is present, then file would be trucated then added

with open("sample.txt","w") as file:
    file.write("I just Wrote")


# Write a JSON to the file
import json
dict_a={
        "name" : "Antman",
        "time" : 5344236456542,
        "seen"  : True,
        "badhabits" : None
    }
with open("profile.json","w") as file:
    data=json.dumps(dict_a,indent=4)
    file.write(data)

with open("profile.json","r") as file:
    data=file.read()
    converted=json.loads(data)
    print (converted["name"])

with open("sample.txt","a") as file:
    file.write("\nAppended")




































# Immutable vs Mutable
# Addressing
# print in single line avoid \n



