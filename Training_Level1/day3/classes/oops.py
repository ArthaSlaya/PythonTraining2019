class mammal():
	def __init__(self):
		print ("Hey im mammalia")
	def smile(self):
		print("Smiling")

class reptiles():
	def __init__(self):
		print ("I love crocs")
	def bite(self):
		print ("Biting")

class animal(mammal):
	__noofanimals=0
	def __init__(self,legs,nose):
		self.legs=legs
		self.nose=nose
		print ("I am Born")
		animal.__noofanimals+=1
		mammal.__init__(self)
	def running(self):
		print ("I am Running with",self.__noofanimals,"legs")
	def teasing(self):
		print ("I am teasing")
	def smile(self):
		print ("Smiling Animal")

lion=animal(4,1)
lion.smile()