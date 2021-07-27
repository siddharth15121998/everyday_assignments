class Calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def div(self,a,b):
        return a/b
    def mul(self,a,b):
        return a*b
    def floord(self,a,b):
        return a//b

calci=Calculator()
n1=int(input("enter first number :"))
n2=int(input("enter second number :"))
print(calci.add(n1,n2))
print(calci.sub(n1,n2))
print(calci.div(n1,n2))
print(calci.mul(n1,n2))
print(calci.floord(n1,n2))