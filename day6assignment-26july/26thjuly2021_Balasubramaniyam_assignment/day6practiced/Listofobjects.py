class Listofobjects:
    def __init__(self,name,rollno,admino):
        self.name=name
        self.rollno=rollno
        self.admino=admino
list1=[]
list1.append(Listofobjects("Balu",1,123))
list1.append(Listofobjects("MSD",2,456))
list1.append(Listofobjects("raina",3,789))
print(list1[0].name)
print(list1[1].rollno)
print(list1[2].admino)
