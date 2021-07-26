class person:
    def __init__(self,name):
        self.myname=name
    def saymyname(self):
        print(self.myname)

n=input("enter a name")
p=person(n)
p.saymyname()
