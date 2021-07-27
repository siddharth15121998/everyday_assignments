class College:
    def func1(self,name):
        self.name=name
        print(self.name)
class Students(College):
    def func2(self,dept):
        self.dept=dept
        print(self.dept)
obj1=College()
obj1.func1("SKUCET")
#obj1.func2("CSE")
obj2=Students()
obj2.func1("SKU")
obj2.func2("ECE")
