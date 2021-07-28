import json
import requests
data=requests.get("https://reqres.in/api/users?page=2")
ExtractedData=data.json()

x=ExtractedData["data"]

p=[]
for i in x:
    p.append(i["first_name"])
print(p)    


     
