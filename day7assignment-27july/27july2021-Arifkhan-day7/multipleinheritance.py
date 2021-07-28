class AdditionOperation:
    def addTwoNum(self,a,b):
        return a+b

class SubtractionOperation:
    def subTwoNum(self,a,b):
      return a-b

class MultiplicationOperation:
    def multiTwoNum(self,a,b):
        return a*b

class Calculator(AdditionOperation,SubtractionOperation,MultiplicationOperation):
    pass
objectc=Calculator()
n1=int(input("enter the first number"))       
n2=int(input("enter the second number"))    

#print(objectc.addTwoNum)
#print(objectc.subTwoNum)
#print(objectc.multiTwoNum)
print(issubclass(Calculator,MultiplicationOperation))