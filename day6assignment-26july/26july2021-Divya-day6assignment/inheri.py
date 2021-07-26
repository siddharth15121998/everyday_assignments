class mobiles:
    def my_color(self,color):
        self.color = color
        print(self.color)
class brand(mobiles):
    def bname(self,name):
        self.name = name
        print(self.name)

objmobiles = mobiles()
objbname = brand()
objmobiles.my_color("red")
objbname.bname("nokia")
objbname.my_color("black")