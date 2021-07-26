class Calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b
    def floor(self,a,b):
        return a//b
a=int(input("Enter First Number :"))
b=int(input("enter second number : "))
cal=Calculator()
print(cal.add(a,b))
print(cal.sub(a,b))
print(cal.mul(a,b))
print(cal.div(a,b))
print(cal.floor(a,b))
