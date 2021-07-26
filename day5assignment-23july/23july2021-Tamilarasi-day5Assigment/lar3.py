n1=int(input("enter:"))
n2=int(input("enter:"))
n3=int(input("enter:"))
if(n1>=n2 and n1>=n3):
    large=n1
elif(n2>=n1 and n2>=n3):
    large=n2
else:
    large=n3
print("largest num is",large)