import json
import requests
data=requests.get("https://reqres.in/api/users?page=2")
E=data.json()
articlesname=E["data"]
print(articlesname)
li=[]
for i in articlesname:
    li.append(i["first_name"])
print(li)
