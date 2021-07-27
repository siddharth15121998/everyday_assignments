#No of vowels
c=0
vowel = ["A","E","I","O","U","a","e","i","o","u"]
for x in "INDID IS MY COUNTRY":
    if x in vowel:
        c+=1
print("Number of Vowels",c)