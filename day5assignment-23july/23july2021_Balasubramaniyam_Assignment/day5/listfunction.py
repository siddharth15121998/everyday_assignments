large=[]
small=[]
n1=int(input("enter num 1: "))
n2=int(input("enter num 2: "))
def larger(n1,n2):
    if n1>n2:
        l=n1
    else:
        l=n2
    return l
def smaller(n1,n2):
    if n1<n2:
        s=n1
    else:
        s=n2
    return s
a=larger(n1,n2)
b=smaller(n1,n2)
large.append(a)
small.append(b)
print(large,small)