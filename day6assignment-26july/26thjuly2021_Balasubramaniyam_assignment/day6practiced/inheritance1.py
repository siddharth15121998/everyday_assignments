class Person(object):   
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
   
class Employee(Person): 
    def __init__(self, name,id):
        self.id=id
        super().__init__(name)
    def getName(self):
        return self.name,self.id
   
emp = Person("Balu") 
print(emp.getName())
emp1=Employee("Balu",1)
print(emp1.getName())