import json
import requests
data = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=5b00428da5f24a4dae3f2558212dd2d8")
ExtractedData = data.json()     #json parsing
#print(ExtractedData)  #extracted data is imagery here
print(ExtractedData["articles"])  
print(data)
# print(data.text)
articles=ExtractedData["articles"]
print(len(articles))