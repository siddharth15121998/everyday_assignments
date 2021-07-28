class Car:
    def color(self):
        print("red")
class BMW(Car):
    def color(self):
        print("White")

obj1=BMW()
obj1.color()
obj2=Car()
obj2.color()