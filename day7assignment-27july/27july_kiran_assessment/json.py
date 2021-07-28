import json
import requests
data=requests.get("https://reqres.in/api/users?page=2")
Extracteddata=data.json()
print(ExtractedData)