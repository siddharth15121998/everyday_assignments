class Department:
    def __init__(self,depname):
        self.depname = depname
    def departname(self):
        print(self.depname)
    def add_students(self,name,roll_no,address):
        print(name,roll_no,address)
d = input("enter a department name: ")    
n = input("enter a name: ")
r = int(input("enter a roll number: "))
a = input("enter a address: ")

Dep1 = Department(d)
Dep1.departname()
Dep1.add_students(n,r,a)
Dep2 = Department("ECE")
Dep2.departname()
Dep2.add_students("div",13,"yyyy")
