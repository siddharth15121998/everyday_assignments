import requests,json
data=requests.get("https://reqres.in/api/users?page=2")
string=data
a=string.json()
da=a['data']
for d in da:
    print(d['first_name'])
