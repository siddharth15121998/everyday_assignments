'''strings'''
data=input("enter the string ")
x=slice(5)
print(data)
print(data[x])
print(data.capitalize())
print(data.title())
print(data.upper())
print(data.lower())
print(data.strip())
print(data.find("world"))
print(data.count("hello"))
print(data.replace("hello","hi"))
print(data[0])
print(len(data))
print(data[len(data)-1])
print(data[22])
print(data[::-1])



'''lists'''

names=["aadrika","sid","anshita",21,34.5,9]
del names[3]
names.remove("sid")
print(names)
names.pop(1)
print(names)
names.clear()
print(names)


'''tuples'''

name=("aadrika","mish","amyra")
nm=(1,2,3)
name[0]="sid"
del names[1]
print(len(name))
print(name+nm)
print(nm*3)

name.clear()
print(name)
a="aadrika"
if (a in name):
    print("present in the tuple")
else:
    print("not present")

print(max(nm))
print(min(name))
print(cmp(names,nm))
print(list(name))