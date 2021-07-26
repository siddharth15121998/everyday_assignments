n1=int(input("Enter the num 1:"))
n2=int(input("Enter the num 2:"))
n3=int(input("Enter the num 3:"))
list1=[n1,n2,n3]
def sqr(a):
    return a**2
print(list(map(sqr,list1)))