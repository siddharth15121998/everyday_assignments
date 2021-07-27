class student:   
    def Student(self):
        self.name = input("Name: ")
        self.age = input("Age: ")
        self.gender = input("Gender: ")
class test(student):
    
    def Marks(self):
        self.stuClass = input()
        self.literature = int(input())
        self.math = int(input())
        self.biology = int(input())
        self.physics = int(input())
class marks(test):    
    def display(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Gender: ",self.gender)
        print("Study in: ",self.stuClass)
        print("Total Marks: ", self.literature + self.math + self.biology + self.physics)
m1 = marks()
m1.Student()
m1.Marks()
m1.display()