import requests
data = {'apikey':'yvWCocqm8kVlFxRsB0dQlxKP0t12'}
r = requests.get('http://cricapi.com/api/matches?apikey=yvWCocqm8kVlFxRsB0dQlxKP0t12',)
data=r.json()
print (data["provider"])