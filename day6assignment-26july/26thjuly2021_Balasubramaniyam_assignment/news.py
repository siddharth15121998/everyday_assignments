import requests
data=requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=5b00428da5f24a4dae3f2558212dd2d8")
#print(data.text)
dict1=data.text
list1=dict1.articles
print("list1:",list1)