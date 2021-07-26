class bike:
    def original_color(self,color):
        self.color = color
        print("the color is: ",self.color)

class brand(bike):
    def bname(self,name):
        self.name = name 
        print("My bike is" ,self.name)
    def mileage(self,mil):
        self.mil = mil
        print("the mileage is: ",self.mil)


objbike = bike()
objbname = brand()
#objbike.original_color("red")
objbname.bname("RX100")
objbname.original_color("black")
objbname.mileage("40 kmph")