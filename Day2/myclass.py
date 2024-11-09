
'''
class Animal():
    noofanimals=0 # Class Variable
    def __init__(self,name): # Constructor
        self.name=name  # Instance Variable
        Animal.noofanimals+=1
        print ("I am Born")
    def sleeping(self):  # Methods, eac
        print ("I am sleeping")
    def running(self):
        print ("I am running")
    def __del__(self):  # destructor
        Animal.noofanimals-=1
        print ("{} is dead".format(self.name))

'''
'''
print (Animal.noofanimals)
lion=Animal("Simba")
print (lion.noofanimals)
del lion
tiger=Animal("Tiger")
print (tiger.noofanimals)
'''
'''
# Using a dot operator, can access the attribute
# print ("My name is {}".format(lion.name))
# lion.wings=2
# print (lion.wings)

# print (hasattr(lion,"wings"))
# print (getattr(lion,"wings"))
# print (delattr(lion,"wings"))
# print (setattr(lion,"wings",2))

# attrList=["wings","name","age"]
# for x in attrList:
#     #delattr(lion,x)
#     print (hasattr(lion,x))
'''
'''

class A():
    def __init__(self,name):
        self.name=name
        print ("Parent Class Contructor")
    def run(self):
        print ("Running A")
    def hear(self):
        print ("hearing")

class B(A):
    def __init__(self,name,age):
        self.age=age
        super().__init__(name)
        print ("Child Class Contructor")
    def sleep(self):
        print ("Sleeping B")
    def run(self):
        super().run()
        print ("Running B")

f=B("batman",20)
print (f.name)
'''

'''
import subprocess
import json
result=subprocess.run("python3 sample.py",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
if(result.returncode==0):
    data=result.stdout
    data1=json.loads(data)
    print(data1["name"])
else:
    print (result.stderr)


import subprocess
import json
result=subprocess.run("ls -la",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
if(result.returncode==0):
    data=result.stdout.decode('utf-8')
    with open("datafile.log","w") as file:
        file.write(data)
    print (data)
else:
    print (result.stderr)

'''


