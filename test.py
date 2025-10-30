import requests
from requests.auth import HTTPDigestAuth

url = "http://xx.xx.x.xx/ISAPI/Intelligent/FDLib/FaceDataRecord?format=json"

payload = {
    'person': '{"faceLibType": "blackFD", "FDID": "1", "FPID": "12345", "name": "Lipheng"}'
}

files=[
  ('image',('C0748.jpg',open('D:\data\C0748.jpg','rb'),'image/jpeg'))
]

headers = {}

# Digest authentication credentials
username = 'admin'
password = '@@123456'

response = requests.request("POST", url, headers=headers, data=payload, files=files, auth=HTTPDigestAuth(username, password))

print(response.text)
