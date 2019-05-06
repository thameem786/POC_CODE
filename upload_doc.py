from docx import Document
import os
import requests
import json
def upload_doc():
    upload_url = "http://<ip address>/storeinkb"
    upload_payload = """{
        "Subject": "","Body": "&&&&","Sender": null,"DocumentType": "Generic","Recipients": "","CarbonCopy": "","BackCarbonCopy": "",
        "SentOn": "","ContributedBy": "thameem.sakkarai","Attachments": "","FileName": "@@@@","Title": "#### ",
        "ExistingDocObjectId": "","Client": "thameem","DocumentTypeExtension": "$$$$","CustomTags": [],"StaticQuestions": [] }"""
    upload_filepath="./InputDocs/"
    headers = {'content-type': "application/json"}
    for i in os.listdir(upload_filepath):
        if i.endswith(".docx"):
            doc = Document(upload_filepath+ i )
            filename,extension=os.path.splitext(i)
            if filename =="Reset My Cardinal Health Password.lnk":
                filename = "CPA_IL Report"
            print(filename)
            extension=extension.upper()[1:]
            print(extension)
            fullText = []
            for para in doc.paragraphs:
                fullText.append(para.text)
            print(fullText)
            print(type(fullText))
            input_payload=upload_payload
            input_payload = input_payload.replace("&&&&", str(str(fullText).encode("utf-8", errors="strict")))
            input_payload = input_payload.replace("$$$$", str(extension))
            input_payload = input_payload.replace("####", str(filename)).replace("@@@@", str(i))
            print(input_payload)
            response = requests.request("POST", url=upload_url, data=input_payload, headers=headers)
            if response is not None and response.status_code == 200:
                resp = json.loads(response.text)
                print(resp)

        else :
            filename, extension = os.path.splitext(i)
            if filename =="Cardinal - RUN SOW Contract Awareness":
                filename = "Cardinal health"
            print(filename)
            print(extension.upper())
            file=open(upload_filepath + i, "r")
            fulltext=file.readlines()
            print(fullText)
            input_payload = upload_payload
            input_payload = input_payload.replace("&&&&", str(str(fullText).encode("utf-8", errors="strict")))
            input_payload = input_payload.replace("$$$$", str(extension.upper()))
            input_payload = input_payload.replace("####", str(filename)).replace("@@@@", str(i))
            print(input_payload)
            response = requests.request("POST", url=upload_url, data=input_payload, headers=headers)
            if response is not None and response.status_code == 200:
                resp = json.loads(response.text)
                print(resp)
if __name__ == "__main__":
    upload_doc()


