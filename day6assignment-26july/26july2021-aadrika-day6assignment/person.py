class Person:
    def __init__(self,name):
        self.name=name
    def sayMyName(self):
        print(self.name)
n=input('enter your name :')
p1=Person(n)
p1.sayMyName()