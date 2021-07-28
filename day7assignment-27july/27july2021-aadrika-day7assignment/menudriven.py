def addme(a,b):
    return a+b

def subme(a,b):
    return a-b




while(True):
    print("Select an option from menu")
    print("\n")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Exit")
    choice=int(input("Enter your choice number :"))
    if (choice==1):
        print("Addition selected")
        n1=int(input("enter 1st num for addition :"))  
        n2=int(input("enter 2ndt num for addition :"))  
        print(addme(n1,n2))
        break
    elif choice==2:
        print("Subtraction is selected")
        n1=int(input("enter 1st num for subtraction :"))  
        n2=int(input("enter 2ndt num for subtraction :"))  
        print(subme(n1,n2))
        break
    elif choice==3:
        break
    else:
        print("Wrong choice")