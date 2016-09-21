import json, requests, datetime

TOKEN = '6ecdff3c2d49cf120e8a354696bd350b' 
dict = {'token': TOKEN, 'github': 'https://github.com/bdanielsimmons/BDSimmonsCode2040'}
r = requests.post("http://challenge.code2040.org/api/register", json = dict)

dict = {'token': TOKEN}
string = requests.post("http://challenge.code2040.org/api/reverse", dict)
reverseString = string.text[::-1]
myKey = {'token': TOKEN, 'string': reverseString}
string = requests.post("http://challenge.code2040.org/api/reverse/validate", myKey)

r = requests.post("http://challenge.code2040.org/api/haystack", data={'token': TOKEN})
json = r.json()
needle = json['needle']
haystack = json['haystack']
index = haystack.index(needle)
r = requests.post("http://challenge.code2040.org/api/haystack/validate", data={'token': TOKEN, 'needle': index})

r = requests.post("http://challenge.code2040.org/api/prefix", data={'token': TOKEN})
json = r.json()
prefix = json['prefix']
array = json['array']
newArray = []
for item in array:
    if not item.startswith(prefix):
        newArray.append(item)
r = requests.post("http://challenge.code2040.org/api/prefix/validate", json={'token': TOKEN, 'array': newArray})

r = requests.post("http://challenge.code2040.org/api/dating", data={'token': TOKEN})
json = r.json()
datestamp = json['datestamp']
interval = json['interval']
current_datestamp = datetime.datetime.strptime(datestamp, "%Y-%m-%dT%H:%M:%SZ")
new_datestamp = current_datestamp + datetime.timedelta(seconds=int(interval))
new_datestamp_formatted = new_datestamp.strftime("%Y-%m-%dT%H:%M:%SZ")
r = requests.post("http://challenge.code2040.org/api/dating/validate", data={'token': TOKEN, 'datestamp': new_datestamp_formatted})
