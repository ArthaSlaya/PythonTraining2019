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
x,y=y,x
print (x,y)



























# Immutable vs Mutable
# Addressing
# print in single line avoid \n