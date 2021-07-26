class student:
    
    def Student(self):
        self.name = input("Name: ")
        self.age = input("Age: ")
        self.gender = input("Gender: ")


class test(student):
    
    def Marks(self):
        self.stuClass = input("Class: ")
        print("Enter the marks of the respective subjects")
        self.literature = int(input("Literature: "))
        self.math = int(input("Math: "))
        self.biology = int(input("Biology: "))
        self.physics = int(input("Physics: "))

class marks(test):
    
    def display(self):
        print("\n\nName: ",self.name)
        print("Age: ",self.age)
        print("Gender: ",self.gender)
        print("Study in: ",self.stuClass)
        print("Total Marks: ", self.literature + self.math + self.biology + self.physics)


m1 = marks()
m1.Student()
m1.Marks()
m1.display()