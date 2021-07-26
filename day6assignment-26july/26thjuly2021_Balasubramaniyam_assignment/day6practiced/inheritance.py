class Car:
    def mcolor(self,color):
         self.color=color
         print(self.color)
class Bmw(Car):
    def topspeed(self,speed):
        self.speed=speed
        print(self.speed)
    
b=Bmw()
c=Car()
b.mcolor("RED")
b.topspeed(120)
c.mcolor("RED")
#c.topspeed(120)