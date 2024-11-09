details={
	"firstname" : "Prathik",
	"lastname" : "Pai",
	"phonenumber":  "",
	"password"  : "secret",
	"address": [
				{
				"pincode": "570001",
				"street" : "StreetA",
				"typeofaddr" : "Home"
				},
				{
				"pincode": "570002",
				"street" : "StreetB",
				"typeofaddr" : "Office"
				}

	]
}

if("lastname" in details):
	print (details["lastname"])

for x in details["address"]:
	print (x)


'''
Check if firstname and lastname exist and the values are not empty,
if it exist then check if an address is registered under the name Office
'''

if("firstname" in details and "lastname" in details):
	if(len(details["firstname"])!=0 and len(details["lastname"])!=0):
		for x in details["address"]:
			if("typeofaddr" in x and x["typeofaddr"]=="Office"):
				print ("YES OFFICE EXIST")
				break;
	else:
		print ("Values of firstname or lastname is empty")
else:
	print ("Attributes Missing")