class Addition:
    def add(self,a,b):
        return a+b
class subtraction(Addition):
    def sub(self,a,b):
        return a-b
class multiplication(subtraction):
    def mul(self,a,b):
        return a*b
class divison(multiplication):
    def div(self,a,b):
        return a/b
class floordivison(divison):
    def floor(self,a,b):
        return a//b
obj1=floordivison()
a=int(input("enter a number: "))
b=int(input("enter a 2 nd number :"))
while(1):
    print("select an option:")
    print("1)addition :")
    print("2) subtraction : ")
    print("3) Multiplication:")
    print("4) Divison : ")
    print("5) floor:")
    print("6 or other To Exit")
    option=int(input())
    if option==1:
        a=obj1.add(a,b)
        print(a)
    elif option==2:
        print("Subtraction is selected: ")
        a=obj1.sub(a,b)
        print(a)
    elif option==3:
        print("Multipilcation is selected: ")
        a=obj1.mul(a,b)
        print(a)
    elif option==4:
        print("Division is selected: ")
        a=obj1.div(a,b)
        print(a)
    elif option==5:
        print("Floor is selected: ")
        a=obj1.floor(a,b)
        print(a)
    else:
        break