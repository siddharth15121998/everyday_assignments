import json
import requests
data = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=5b00428da5f24a4dae3f2558212dd2d8")
ExtractedData = data.json()     #json parsing
#print(ExtractedData)  #extracted data is imagery here
#print(ExtractedData["articles"])  
# print(data)
# print(data.text)
articles=ExtractedData["articles"]
#print(len(articles))

#vowel count
vowel ="aeiou"

for i in articles:
    title=i["title"]
    count={}.fromkeys(vowel,0)
    print(title)
    for n in title.lower():
        if n in count:
            count[n]=count[n]+1

    print(count)
