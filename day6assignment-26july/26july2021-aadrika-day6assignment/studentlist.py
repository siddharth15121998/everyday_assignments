class Students:
    def __init__(self,name ,rollno,admino):
        self.myname=name
        self.myroll=rollno
        self.myadmino=admino


li=[]
li.append(Students("aadrika",101,123))
li.append(Students("anshita",102,124))
li.append(Students("vaishnavi",103,125))
for i in range(3):
    print(li[i].myname)

