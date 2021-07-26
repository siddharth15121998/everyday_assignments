n1 = int(input("enter the first number"))
n2 = int(input("enter the second number"))
n3 = int(input("enter the third number"))
lis= [n1,n2,n3]
def square(num):
    return num**2
print(list(map(square,lis)))