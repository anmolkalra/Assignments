import requests,json
response=requests.get('https://api.forismatic.com/api/1.0/?method=getQuote&key=457653&format=json&lang=en')
new=response.json()
del new['quoteLink']
del new['senderLink']
del new['senderName']
print(new)
