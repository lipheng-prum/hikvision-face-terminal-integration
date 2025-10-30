import requests
from requests.auth import HTTPDigestAuth
import xml.etree.ElementTree as ET
# Digest authentication credentials
username = 'XXXXXXX'
password = 'XXXXXXX'

url = "http://xx.xx.x.xx/ISAPI/System/deviceInfo"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload, auth=HTTPDigestAuth(username, password))

# Check if the response is successful
if response.status_code == 200:
    try:
        # Parse the XML response
        root = ET.fromstring(response.text)

        # Define the namespace
        namespace = {'ns': 'http://www.isapi.org/ver20/XMLSchema'}

        # Extract the model
        model = root.find('ns:model', namespace).text

        # Print the model
        print(f"Model: {model}")
    except ET.ParseError:
        print("Failed to parse XML.")
else:
    print(f"Request failed with status code {response.status_code}.")