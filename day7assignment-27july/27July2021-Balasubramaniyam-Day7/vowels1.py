import requests,json
data=requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=5b00428da5f24a4dae3f2558212dd2d8")
string=data.text
a=json.loads(string)
length=len(a)
#(a.keys())
b=a['articles']
print(isinstance(b[0],dict))
vowelcount=[]
for i in range(len(b)):
    c=b[i]
    #print(c['title'])
    tit=c['title']
    count=0
    vowelcountandtit=""
    for x in tit:
        if x=="a" or x=="e" or x=="i" or x=="o" or x=="u" or x=="A" or x=="E" or x=="I" or x=="O" or x=="U":
            count=count+1
    vowelcountandtit=tit+" "+str(count)
    vowelcount.append(vowelcountandtit)
for i in vowelcount:
    print(i)    