import requests
from requests.auth import HTTPDigestAuth
import json

# Digest authentication credentials
username = 'XXXXXXX'
password = 'XXXXXXX'

url = "http://xx.xx.x.xx/ISAPI/Intelligent/FDLib/FDSearch/Delete?format=json&FDID=1&faceLibType=blackFD"

payload = json.dumps({"FPID": [{"value": "12345"}]})
headers = {'Content-Type': 'application/json'}

response = requests.request("PUT", url, headers=headers, data=payload, auth=HTTPDigestAuth(username, password))

print(response.status_code)
print(response.json())
# Check if statusString is "OK"
if response.json().get("statusString") == "OK":
    print("ok")
