import pandas as pd
import requests
import json
from pandas import ExcelWriter
import os
from docx import Document
import pathlib
import ast


class KBAutomatedTester:
    def __init__(self):
        self._url = "http://<ip address>/searchkb"
        self._payload = {"text" : "","client": "300000000000000000000002","user_name": "thameem.sakkarai","is_sfb" : "N","is_initial_chat" : "N","search_combined" : "Y"}
        self._headers = {'content-type': "application/json"}
        self._file_path = "Payload.xlsx"
        self._upload_url = "http://<ip address>/storeinkb"
        self._upload_payload = '''{
            "Subject": "","Body": "&&&&","Sender":None ,"DocumentType": "Generic","Recipients": "","CarbonCopy": "","BackCarbonCopy": "",
            "SentOn": "","ContributedBy": "thameem.sakkarai","Attachments": "","FileName": "@@@@","Title": "####",
            "ExistingDocObjectId": "","Client": "Cardinal","DocumentTypeExtension": "$$$$","CustomTags": [],"StaticQuestions": [] }'''
        self._upload_filepath="./InputDocs/"

    def upload_doc(self):
        return_message = {}
        try:
            for i in os.listdir(self._upload_filepath):
                fullText=[]
                if pathlib.Path(self._upload_filepath + "/" + str(i)).suffix == ".docx":
                    doc = Document(self._upload_filepath + i)
                    filename, extension = os.path.splitext(i)
                    extension = extension.upper()[1:]
                    for para in doc.paragraphs:
                        fullText.append(para.text)
                elif pathlib.Path(self._upload_filepath + "/" + str(i)).suffix == ".txt":
                    filename, extension = os.path.splitext(i)
                    file = open(self._upload_filepath + i, "r", encoding='utf-8')
                    fullText = file.readlines()
                else:
                    return_message["message"]="Please provide docx/txt files"
                if (len(fullText) > 0):
                    d = ''.join(fullText).replace('\t', '').replace('\n', '').replace('\"', '')
                    input_payload = self._upload_payload
                    input_payload = input_payload.replace("&&&&",str(d))
                    input_payload = input_payload.replace("$$$$", str(extension.upper()))
                    input_payload = input_payload.replace("####", str(filename)).replace("@@@@", str(i))
                    input_payload = ast.literal_eval(input_payload)
                    response = requests.request("POST", url=self._upload_url, json=input_payload, headers=self._headers)
                    if response.status_code == 200:
                        resp = json.dumps(response.text)
                        print(resp)
                    else:
                        if (response is not None):
                            return_message["message"] = "Server returned status: " + response.status_code
                        else:
                            return_message["message"] = "Could not get any response from server."
                else:
                    return_message["message"] = "No content found."

        except Exception as e:
            return_message["message"] = str(e)
        return return_message

    def get_test_payload(self):
        lst_payload_data = []
        df_data = pd.read_excel(self._file_path)
        for i in df_data.index:
            payload_item = dict()
            payload_item["Query"] = df_data["Query"][i]
            payload_item["ExpectedSummary"] = df_data["ExpectedSummary"][i]
            payload_item["ExpectedDetails"] = df_data["ExpectedDetails"][i]
            lst_payload_data.append(payload_item)
        return lst_payload_data

    def search_kb_with_payload(self, lst_query_details):
        return_message={}
        try:
            for payload_item in lst_query_details:
                input_payload = self._payload
                input_payload["text"] = str(payload_item["Query"].encode("utf-8", errors="strict"))
                response = requests.request("POST", url=self._url, json=input_payload, headers=self._headers)
                if response is not None and response.status_code == 200:
                    print(response.text)
                    resp = json.loads(response.text)
                    if type(resp)==list:
                        payload_item["ActualDetails"] = resp[0]["details"]
                        payload_item["ActualSummary"] = resp[0]["summary"]
                        print(payload_item["ActualSummary"])
                        payload_item["StandardResponse"] = resp[0]["standard_response"]
                        if payload_item["StandardResponse"] == "Y":
                            payload_item["Response"] = resp[0]["response"]
                    else:
                        payload_item["ActualDetails"] = resp["details"]
                        payload_item["ActualSummary"] = resp["summary"]
                        print(payload_item["ActualSummary"])
                        payload_item["StandardResponse"] = resp["standard_response"]
                        if payload_item["StandardResponse"] == "Y":
                            payload_item["Response"] = resp["response"]
        except Exception as e:
            print (e)
            return_message["message"] = str(e)
        return lst_query_details, return_message

    def compare_kb_log__results(self, lst_data_details):
        data = pd.DataFrame(lst_data_details[0],columns=("Query","ExpectedSummary","ActualSummary","ExpectedDetails","ActualDetails","StandardResponse"))
        data['is_compare'] = (data.ExpectedDetails == data.ActualDetails) & (data.ExpectedSummary == data.ActualSummary)
        writer = ExcelWriter("Output.xlsx", engine="xlsxwriter")
        data.to_excel(writer, sheet_name="Output",index=False)
        writer.save()



if __name__ == "__main__":
    kb_automated_tester = KBAutomatedTester()
    # output=kb_automated_tester.upload_doc()
    lst_payload = kb_automated_tester.get_test_payload()
    lst_data = kb_automated_tester.search_kb_with_payload(lst_payload)
    kb_automated_tester.compare_kb_log__results(lst_data)
