class Person:

    def __init__(self,name):
        self.name = name
    def Myname(self):
        print(self.name)
n = input("enter a name: ")
p = Person(n)
p.Myname()