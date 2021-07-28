while(True):
    print("select an option from menu")
    print("\n")
    print("1. Addition")
    print("2. Subtraction")
    print("3. exit")
    choice=int(input("enter your value:"))
    a = int(input("give a value:"))     
    b = int(input("give a value:"))


    if choice==1:
        print("Addition Selected")
        def add(x,y):
            return x+y
    print(add(a,b))
    
    if choice==2:
        print("Subtraction Selected")
        def sub(m,n):
            return m-n   
    print(sub(a,b))
    
    if choice==3:
        break

    else:
        print("wrong choice")

    
         