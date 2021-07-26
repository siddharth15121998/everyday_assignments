odd=[]
even=[]
def oddeve(n1):
    if n1%2==0:
        even.append(n1)
        print(even)
    else:
        odd.append(n1)
n1=int(input("enter number:"))
oddeve(n1)
