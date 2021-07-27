class person:
    def __init__(self,name):
        self.name=name
    def sayMyName(self):
        print(self.name)
n1=input("enter a name")
p=person(n1)
p.sayMyName()