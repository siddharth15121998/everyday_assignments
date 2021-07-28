class Car:
    def color(self):
        print("red")

class BMW(Car):
    def color(self):
        print("white")   

obje=BMW()
obje.color()

obcar=Car()
obcar.color()
