class Cars:
    def carColor(self,color):
        self.color=color
        print(self.color)
class Toyoto(Cars):
    def carSpeed(self,speed):
        self.speed=speed
        print(self.speed)
objcars=Cars()
objtoyoto=Toyoto()
objcars.carColor("red")
# objcars.carSpeeb(100)
objtoyoto.carColor("blue")
objtoyoto.carSpeed(200)