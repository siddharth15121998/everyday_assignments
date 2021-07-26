n1=int(input("enter:"))
n2=int(input("enter:"))
n3=int(input("enter:"))
if(n1<=n2 and n1<=n3):
    small=n1
elif(n2<=n1 and n2<=n3):
    small=n2
else:
    small=n3
print("smallest num is",small)