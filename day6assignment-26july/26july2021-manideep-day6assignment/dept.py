class department():
    def __init__(self,dept):
        self.dept=dept
    def addstudent(self):
        self.sname=input("enter your name:")
        self.sroll=int(input("enter you roll:"))
        self.sadmin=int(input("enter you admin:"))
        self.scollege=input("enter your college:")
        self.sadd=input("enter your address :")
        self.smob=int(input("enter mobile number:"))
        print("department is:",self.dept)
        print("student name is :",self.sname)
        print("student roll number is:",self.sroll)
        print("student admision number is :",self.sadmin)
        print("student college:",self.scollege)
        print("student mobile is:",self.smob)

dname=input("enter department name:")
s1=department(dname)
s1.addstudent()
print("\n")
s2=department("ece")
s2.addstudent()
    
    



        



