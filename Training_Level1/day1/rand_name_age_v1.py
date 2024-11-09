import random

def generate_random_alpha(length):
	alpha="abcdeg"
	outcome=""
	for x in range(0,length):
		outcome+=alpha[random.randint(0,len(alpha)-1)]
	return outcome

print (generate_random_alpha(6))

def generate_name():
	names=["ABC","BCD"]
	return names[random.randint(0,len(names)-1)]

print (generate_name())








