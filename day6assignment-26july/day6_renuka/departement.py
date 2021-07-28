class departement:
    def __init__(self,sroll,scoll,smob,sadd,sname):
        self.ssroll=sroll
        self.sscoll=scoll
        self.ssmob=smob
        self.ssadd=sadd
        self.ssname=sname
    def addStudentNames(self):
        print(self.ssroll)
        print(self.sscoll)
        print(self.ssmob)
        print(self.ssadd)
        print(self.ssname)
roll=int(input("enter a roll number"))
coll=input("enter a college")
mob=int(input("enter a mobile number"))
add=input("enter a address")
name=input("enter a name")
dep1=departement(roll,coll,mob,add,name)
dep1.addStudentNames()
