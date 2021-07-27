class calculator:
    def addition(self,n1,n2):
        return n1+n2
    def subtraction(self,n1,n2):
        return n1-n2
    def multiplication(self,n1,n2):
        return n1*n2
    def division(self,n1,n2):
        return n1/n2
n1=int(input("enter a number"))
n2=int(input("enter a number"))
cal=calculator()
add=cal.addition(n1,n2)
sub=cal.subtraction(n1,n2)
mul=cal.multiplication(n1,n2)
div=cal.division(n1,n2)
print(add)
print(sub)
print(mul)
print(div)
    