class Calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
obj=Calculator()
while(True):
    print("select option from menu")
    print("1.addition selected")
    print("2.subtraction selected")
    print("3.exit")
    choice=int(input("enter your choice:"))
    n1=int(input("enter a number:"))
    n2=int(input("enter a number:"))
    if choice==1:
        print("addition:",obj.add(n1,n2))
    elif choice==2:
        print("subtraction",obj.sub(n1,n2))
    else:
        break
        print("wrong choice")