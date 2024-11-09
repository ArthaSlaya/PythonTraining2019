import random
list_a=[]
list_b=["dummy",12]
list_names=["ABC","BCD","CDE","DEF","EFG"]
for x in range(0,100):
	list_b[0]=list_names[random.randint(0,len(list_names)-1)]
	list_b[1]=random.randint(0,100)
	list_a.append(list_b.copy()) #list_a.append(list(list_b))
print (list_a)

# Conditions:
# The Syntax defined above should not be shifted across lines
# Modify with minimal changes to correct the code