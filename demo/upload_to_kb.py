import requests

url = "http://<ip address>/storeinkb"

payload = "{\r\n  \"Subject\": \"\",\r\n  \"Body\": \"Test\",\r\n  \"Sender\": null,\...}"
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "xxxxx"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
