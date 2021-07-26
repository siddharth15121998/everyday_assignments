class department:
    def __init__(self,dept):  
        self.dept = dept
    def dept(self):
        print(self.dept)
    def addstd(self,name,rollno,add):
        print(name,rollno,add,self.dept)
n = department("CSE")
n.addstd("Vaishnavi","105","3591")
p = department("EEE")
p.addstd("Piya","110", "3682")
