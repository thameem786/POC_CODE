import requests
# from shared.service_helper import ServiceHelper
# from va_ai_api.shared import file_helper

upload_url = "http://localhost:5000/convertdoctopdf?client=7777&doc_id=1111"

headers = {'token': 'multipart/form-data'}
# headers = {'token': ''}
# sh = ServiceHelper()

files = {'file': open('test.docx', 'rb')}
# response = requests.request("POST", url=upload_url, files=files,headers=headers)
# print(open('PPTConversion.pptx', 'rb').read())
r = requests.post(upload_url, files=files, headers=headers)
print(r.text)
