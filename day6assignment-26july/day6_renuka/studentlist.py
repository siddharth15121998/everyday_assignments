class students:
    def __init__(self,name,rno,adminno):
        self.sname=name
        self.srno=rno
        self.sadminno=adminno
obj=[]
obj.append(students("ram",101,500))
obj.append(students("rasi",102,501))
obj.append(students("rahul",103,502)) 

print(obj[0].sname)       
print(obj[2].srno)