import requests
url ="https://xxxxxxx"
headers = {'content-type': "application/json"}
try:
    response = requests.request("GET", url, headers=headers)
    print ("----",response)
except Exception as e:
    print (e)


