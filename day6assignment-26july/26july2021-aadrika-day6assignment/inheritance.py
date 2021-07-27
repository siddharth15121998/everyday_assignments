class Cars:
    def minecolor(self,col):
        self.color=col
        print(self.color)

class BMW(Cars):
    def topSpeed(self,speed):
        self.speed=speed
        print(self.speed)

c=Cars()
b=BMW()       
# c.minecolor("red")
# c.topSpeed(100)
b.minecolor("blue")
b.topSpeed(100)