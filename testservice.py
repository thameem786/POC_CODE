import requests,os
url="http://192.168.30.141/api/storage/uploadfile?client=xxxx"
path="/var/www/va/va_ai_api/temp/filestore/xxxx/cb0994c6bee047ca99d1bf378b7ae364/converted_image/cardinal_run_sow_thameem.pdf"
try:
    return_message = {}
    return_message["result"] = False
    return_message["message"] = ""
    os.chdir(path)
    for img_file in os.listdir():
        print("entered")
        files = {'file': open(img_file, 'rb')}
        headers = {'token': 'multipart/form-data'}
        response = requests.request("POST", url, files=files, headers=headers)
        print("----1",response)
        if response.status_code != 200:
            response = requests.request("POST", url, files=files, headers=headers)
        print("-----2",response)
except Exception as e:
    return_message["message"] = "System has encountered an error in file uploading."
    return_message["result"] = False
    print (e)
