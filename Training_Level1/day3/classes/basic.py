class me():
	def __init__(self):
		print ("ok")
	def printme(self):
		print("Printing")
class animal (me):
	__noofanimals=0
	def __init__ (self,legs):
		animal.__noofanimals+=1
		self.legs=legs
		print ("Im an created")

	def run(self):
		print ("I am Running")

	def printme(self):
		print ("Im animal")

lion=animal(4)
tiger=animal(4)
lion.printme()




#lion.noofanimals=5
#print ("No of Animals Created",animal.noofanimals)
#print ("Value of lion",lion.noofanimals)
#print ("Value of lion",tiger.noofanimals)
