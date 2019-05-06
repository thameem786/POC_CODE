import requests
import json
# import pybase64
# import base64
# from pptx import Presentation
from shared.service_helper import ServiceHelper
# from va_ai_api.shared import file_helper

upload_url = "http://localhost:5000/convertppttoimage?client=7777&doc_id=1111"

headers = {'token': 'multipart/form-data'}
# headers = {'token': ''}
sh = ServiceHelper()

files = {'file': open('AccountOnboardingDeckV2.pptx', 'rb')}
# response = requests.request("POST", url=upload_url, files=files,headers=headers)
# print(open('PPTConversion.pptx', 'rb').read())
r = requests.post(upload_url, files=files, headers=headers)
print(r.text)
# !venv/bin/python

# import requests
#
# file = open('PPTConversion.pptx', 'rb')
# url = 'http://localhost:5000/convertppttoimage?client=5555&doc_id=1111'
# headers = {'token': 'c203x302s30s03x0322x0320'}
# payload = {'client_id': 1}
# files = {'file': file}
# r = requests.post(url, files=files, data=payload, headers=headers)
# json_data = r.json()
# print(json_data)
