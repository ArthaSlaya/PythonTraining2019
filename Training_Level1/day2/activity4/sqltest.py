

available_operations=["insert","select"]
available_tables=["users","activities"]

def get_query_select(selected_table,selected_op,selected_col,selected_condition):
	temp_string=selected_op+" "
	if(len(selected_col)==0):
		temp_string+="* "
	else:
		temp_string+="("
		for x in selected_col:
			temp_string+=x+","
		temp_string=temp_string[:-1]+") "
	temp_string+="from "+selected_table
	if(len(selected_condition)!=0):
		temp_len=len(selected_condition)
		temp_string+=" where "
		count=1
		for x,y in selected_condition.items():
			if(isinstance(y, str)):
				temp_string+=x+"='"+y+"'"
			elif(isinstance(y, int)):
				temp_string+=x+"="+str(y)
			if(count!=temp_len):
				temp_string+=" and "
			count+=1
		
	return temp_string
'''
insert users #name=prathik #age=30
insert into users (name,age)values(prathik,30)
'''

def get_query_insert(selected_table,selected_op,selected_col,selected_condition):
	temp_string="insert into "+selected_table+" "
	if(len(selected_condition)!=0):
		temp_string+="("
		for x,y in selected_condition.items():
			temp_string+=x+","
		temp_string=temp_string[:-1]+") "
	temp_string+="values("
	for x,y in selected_condition.items():
		if(isinstance(y,str)):
			temp_string+="'"+str(y)+"',"
		elif(isinstance(y,int)):
			temp_string+=str(y)+","
	temp_string=temp_string[:-1]+")"
	return temp_string

def query_processor(input_str):
	# Temp Data for Processing
	selected_table=None
	selected_op=None
	selected_col=[]
	selected_condition={}
	# Operation Start
	input_list=input_str.split()
	print (input_list)
	flag=False
	for x,y in enumerate(input_list):
		if(x==0):
			if (y in available_operations):
				selected_op=y
			else:
				print (1)
				flag=True
				break
		elif(x==1):
			if(y in available_tables):
				selected_table=y
			else:
				print (2)
				flag=True
				break;
		elif("@" in y):
			selected_col.append(y[1:])
		elif("#" in y):
			d=y[1:]
			d=d.split("=")
			if(len(d)==2):
				if(d[1].isdigit()):
					selected_condition[d[0]]=int(d[1])
				else:
					selected_condition[d[0]]=d[1]
			else:
				print (3)
				flag=True
				break

	if(flag):
		print ("Invalid Syntax")
	else:
		print ("Processing")
		if(selected_op=="select"):
			output=get_query_select(selected_table,selected_op,selected_col,selected_condition)
			return output
		elif(selected_op=="insert"):
			output=get_query_insert(selected_table,selected_op,selected_col,selected_condition)
			return output
'''
Test Case: 1
input_str="select users"
output ->>> "select * from users'"

input_str="select users #name=prathik"
output ->>> "select * from users where name='prathik'"

input_str="select users @age #name=prathik @name"
output ->>> "select (name,age) from users where name='prathik'"

input_str="select users @age #name=prathik @name #age=24"
output ->>> "select (name,age) from users where name='prathik' and age=24"


Test Case 2
input_str="insert users #name=prathik #age=30"
output ->>> "insert into users (name,age) values('prathik','age')"
'''