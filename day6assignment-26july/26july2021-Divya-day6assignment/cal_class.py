class Calculator:

    def addnum(self,a,b):
        return a+b
    def subnum(self,a,b):
        return a-b
    def mulnum(self,a,b):
        return a*b
    def divinum(self,a,b):
        return a/b
    def flodivi(self,a,b):
        return a//b
   
  

    
My_calculator = Calculator()
a = int(input("enter a number: "))
b = int(input("enter a number: "))

addition = My_calculator.addnum(a,b)
print("the sum of two num:",addition)
subraction = My_calculator.subnum(a,b)
print("the sub of two num:",subraction)
multiply = My_calculator.mulnum(a,b)
print("the mul of two num:",multiply)
division = My_calculator.divinum(a,b)
print("the division of two num :",division)
floor_div = My_calculator.flodivi(a,b)
print("the floor division of two num:",floor_div)
