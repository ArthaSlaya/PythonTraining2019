import requests
APIKEY=""
r = requests.post('http://cricapi.com/api/matches', data = {'apikey':APIKEY})
data=r.json()
print (data["matches"][0]["team-1"])
