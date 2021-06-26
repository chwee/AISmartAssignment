import requests
import json

#POST Test
url = 'http://192.168.50.86.:5000/predict'
myobj = {'query': 'I have my windows issue. Pls send office to check'}
json_object = json.dumps(myobj)
x = requests.post(url, json = myobj).json()

print(x['prediction'])
print(x['confidence'])

#GET Test server ok
# x = requests.get('http://192.168.50.86.:5000/test')
# print(x.text)

#GET version of Bert model 
# x = requests.get('http://192.168.50.86.:5000/version')
# print(x.text)
