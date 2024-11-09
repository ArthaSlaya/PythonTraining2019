# Function Scope
# Multiple Arguments to Function
# Dictionary and List Arguments
'''
def printme(*args):
	outcome=""
	for x in args:
		outcome+=str(x)+" "
	print (outcome)

a="hello"
b=2
printme(a,b)
print (a,b)
'''

def me(**kwargs):
	print (kwargs)
	if("indent" in kwargs):
		print ("Indentation is "+str(kwargs["indent"]))

me(space=3)



'''
def call_me():
	a=8    #101
	def keep_the_call():
		a=10   #100
		print (a)  #100
	keep_the_call()
	print (a)   #101
call_me()
print (a)   #100
'''

