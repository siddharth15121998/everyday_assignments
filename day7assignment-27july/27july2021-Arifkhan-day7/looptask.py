def count(str):
    count=0
    vowel=set("aeiouAEIOU")
    for x in str:
        if x in vowel:
            count=count+1
    print("no of vowel:",count)

str="Indiaismycountry"
count(str)