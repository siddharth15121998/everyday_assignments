class Person:
    def __init__(self,name):
        self.name = name
    def sayMyName(self):
        print(self.name)
n = input("Type a name:")
p = Person(n)
p.sayMyName()

