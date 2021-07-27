class Calculator:
    def addNum(self,a,b):
        return a+b
    def subNum(self,a,b):
        return a-b
    def mulNum(self,a,b):
        return a*b
    def divNum(self,a,b):
        return a/b
    def floorNum(self,a,b):
        return a//b
mycal=Calculator()
n1=int(input("enter a number:"))
n2=int(input("enter a number:"))
add=mycal.addNum(n1,n2)
sub=mycal.subNum(n1,n2)
mul=mycal.mulNum(n1,n2)
div=mycal.divNum(n1,n2)
floordiv=mycal.floorNum(n1,n2)
print(add,sub,mul,div,floordiv)