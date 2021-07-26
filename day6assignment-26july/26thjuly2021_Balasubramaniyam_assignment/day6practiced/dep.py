class Department:
    def __init__(self,deptname):
        self.deptname=deptname
    def addstudent(self,name,rollno,phone,address):
        print(name,rollno,phone,address,self.deptname)
Departmentname=input("Enter your First department name :")
d=Department(Departmentname)
name1=input("Enter student name :")
roll=int(input("Enter roll number : "))
phone1=int(input("Enter phone number : "))
city=input("Enter the city :")
Departmentname=input("Enter your Second department name :")
e=Department(Departmentname)
name2=input("Enter student name :")
roll2=int(input("Enter roll number : "))
phone2=int(input("Enter phone number : "))
city2=input("Enter the city :")
d.addstudent(name1,roll,phone1,city)
e.addstudent(name2,roll2,phone2,city2)
