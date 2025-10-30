import requests
from requests.auth import HTTPDigestAuth
import json

# Digest authentication credentials
username = 'XXXXXXX'
password = 'XXXXXXX'

url = "http://xx.xx.x.xx/ISAPI/AccessControl/UserInfo/Record?format=json"

files ={}

payload = json.dumps({
  "UserInfo": {
    "employeeNo": "12345",
    "name": "Lipheng",
    "userType": "normal",
    "Valid": {
      "enable": True,
      "beginTime": "2024-08-12T00:00:00",
      "endTime": "2034-08-12T23:59:00",
      "timeType": "local"
    },
    "doorRight": "1",
    "RightPlan": [
      {
        "doorNo": 1,
        "planTemplateNo": "1"
      }
    ]
  }
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files, auth=HTTPDigestAuth(username, password))

print(response.text)
