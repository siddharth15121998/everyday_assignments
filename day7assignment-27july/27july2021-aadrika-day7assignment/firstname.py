import json
import requests



data=requests.get("https://reqres.in/api/users?page=2")
ex=data.json()  #json parsing


data=ex["data"]
#print(data)
for i in data:
    firstName=i["first_name"]
    print(firstName)