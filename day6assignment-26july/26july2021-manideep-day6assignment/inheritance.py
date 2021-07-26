class cars:
    def mycolor(self,color):
        self.color=color
        print(self.color)

class BMW(cars):
    def topspeed(self,speed):
        self.speed=speed
        print(self.speed)

obj1=cars()
obj2=BMW()

obj1.mycolor("blue")
obj1.topspeed(100)

