class College:
    def func1(self,name):
        self.name=name
        print(self.name)
class Principal(College):
    def func2(self,name):
        self.name=name
        print(self.name)
class Students(Principal):
    def func3(self,dept):
        self.dept=dept
        print(self.dept)
obj1=College()
obj1.func1("SKUCET")
#obj1.func2("CSE")
obj2=Principal()
obj2.func2("Ramachandra sir")
obj2.func1("sri krishnadavaraya university")
#obj2.func3("EEE")
obj3=Students()
obj3.func1("SKU")
obj3.func2("kiran")
obj3.func3("ECE")
