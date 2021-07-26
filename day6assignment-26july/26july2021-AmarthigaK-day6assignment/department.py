class department:
    def __init__(self,dept_name):  #comstructor
        self.dept_name = dept_name
    def dept(self):
        print(self.dept_name)
    def addstd(self,name,rollno,add,blood):
        print(name,rollno,add,blood,self.dept_name)
n = department("CSE")
n.addstd("Amar","001","614626","B+ve")
p = department("EEE")
p.addstd("Mani","015", "614601","B+ve")




