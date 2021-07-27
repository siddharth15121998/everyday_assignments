class Department:
    def __init__(self,dept):
        self.dept=dept
    def addStudent(self):
        self.Sname=input("enter your name :")
        self.Sroll=int(input("enter your roll :"))
        self.Sadno=int(input("enter your admisno :"))
        self.Scollege=input("enter your college :")
        self.Sadd=input("enter your address :")
        self.Smob=int(input("enter your smob :"))
        print("department :", self.dept)
        print("student name :", self.Sname)
        print("student roll no :", self.Sroll)
        print("student admission no :", self.Sadno)
        print("student college :", self.Scollege)
        print("student mobile :", self.Smob)
dname=input("enter department name :")
s1=Department(dname)
s1.addStudent()
print("\n")
# s2=Department("ECE")
# s2.addStudent()