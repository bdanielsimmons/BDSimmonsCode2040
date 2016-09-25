import json, requests, datetime #Used to encode dictionary, post/pull from APIs, and gather datetime information

TOKEN = '6ecdff3c2d49cf120e8a354696bd350b' #Step 1 (Establish ID)
dict = {'token': TOKEN, 'github': 'https://github.com/bdanielsimmons/BDSimmonsCode2040'} #Fill in dictionary and post to site
r = requests.post("http://challenge.code2040.org/api/register", json = dict)


dict = {'token': TOKEN} #Step 2 (Reset the token)
string = requests.post("http://challenge.code2040.org/api/reverse", dict)
reverseString = string.text[::-1] #Slices through the strin backwards and posts to API
myKey = {'token': TOKEN, 'string': reverseString}
string = requests.post("http://challenge.code2040.org/api/reverse/validate", myKey)


r = requests.post("http://challenge.code2040.org/api/haystack", data={'token': TOKEN}) #Step 3 (Grab data from the API)
json = r.json() #Convert info from JSON dict, create variable/array
needle = json['needle'] #Extract array infor
haystack = json['haystack'] 
index = haystack.index(needle) #Add index to dict and send back
r = requests.post("http://challenge.code2040.org/api/haystack/validate", data={'token': TOKEN, 'needle': index})


URL = "http://challenge.code2040.org/api/prefix"
r = requests.post(URL, data={'token': TOKEN}) #Step 4 (Get info from the API)
json = r.json()
prefix = json['prefix'] #For whatever item we're looking at, if it doesn't have the decoded prefix, add the item to newArray
array = json['array']
newArray = []
for item in array:
    if not item.startswith(prefix):
        newArray.append(item)
r = requests.post(URL, json={'token': TOKEN, 'array': newArray}) #Post back to the API


URL = "http://challenge.code2040.org/api/dating/validate"
r = requests.post(URL, data={'token': TOKEN}) #Step 5 (Gather data from API)
json = r.json()
datestamp = json['datestamp']
interval = json['interval'] #Take time and time change from the dating API
current_datestamp = datetime.datetime.strptime(datestamp, "%Y-%m-%dT%H:%M:%SZ")
new_datestamp = current_datestamp + datetime.timedelta(seconds=int(interval)) #Scale up the current date by the interval
new_datestamp_formatted = new_datestamp.strftime("%Y-%m-%dT%H:%M:%SZ")
r = requests.post(URL, data={'token': TOKEN, 'datestamp': new_datestamp_formatted})#Post back to the API
