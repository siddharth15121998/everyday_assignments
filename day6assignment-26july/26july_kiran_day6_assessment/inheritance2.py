class Parent:
    def func1(self):
        print("parent class")
class Child(Parent):
    def func2(self):
        print("child class")
p=Parent()
p.func1()
c=Child()
c.func1()
c.func2()