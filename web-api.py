import requests,json
response=requests.get('https://api.forismatic.com/api/1.0/?method=getQuote&key=457653&format=json&lang=en')
abc=response.json()
del abc['quoteLink']
del abc['senderLink']
del abc['senderName']
print(abc)
