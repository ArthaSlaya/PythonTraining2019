import random
list_final=[] # Create a Empty List
list_names=["ABC","BCD","CDE","DEF","EFG"]
for x in range(0,100):
	random_selected_name=list_names[random.randint(0,len(list_names)-1)]
	random_selected_age=random.randint(0,100)
	list_final.append({"name":random_selected_name,"age":random_selected_age})
print (list_final)

