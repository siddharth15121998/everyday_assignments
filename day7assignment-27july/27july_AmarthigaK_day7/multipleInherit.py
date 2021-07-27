class Addition:
    def addTwoNum(self,a,b):
        return a+b
class Subtraction:
    def subTwoNum(self,a,b):
        return a-b
class Multiplication:
    def MultiTwoNum(self,a,b):
        return a*b
    
class Calculator(Addition,Subtraction,Multiplication):
    pass

objcal=Calculator()
n =int(input("Give a number:"))
m =int(input("Give a value:"))
print(objcal.MultiTwoNum(m,n))
print(objcal.addTwoNum(m,n))
print(objcal.subTwoNum(m,n))

#To check the relationship between classes
print(issubclass(Calculator,Addition))
print(issubclass(Calculator,Subtraction))
print(issubclass(Calculator,Multiplication))
print(issubclass(Addition,Multiplication))
print(issubclass(Addition,Subtraction))
print(issubclass(Subtraction,Multiplication))