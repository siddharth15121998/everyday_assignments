import json
import requests
data=requests.get("https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=2d457423f58e40ecaaf14f41f400a44d")
ExtractedData=data.json()
print(ExtractedData)
print(ExtractedData["articles"])
# articles=ExtractedData["articles"]
# print(len(articles))
# for i in articles:
#     print(i["title"])
vowels="aeiou"
for i in articles:
    title=i["title"]
    count={}.fromkeys(vowel,0)
    print(title.lower())
    for x in title.lower():
        if x in count:
            count[x]=count[x+1]
        print(count)
