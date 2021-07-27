import json
import requests
data = requests.get("https://reqres.in/api/users?page=2")
ExtractedData = data.json()
D = ExtractedData["data"]
# print(D)
# print(len(D))

for n in D:
    name = n["first_name"]
    print(name)
