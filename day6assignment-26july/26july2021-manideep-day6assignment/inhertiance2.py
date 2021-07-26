class Animals:
    def ear(self,ear):
        self.ear=ear
        print(ear)
    def foots(self,foot):
        self.foot=foot
        print(foot)
class Dog(Animals):
    def dogcolor(self,color):
        self.color=color
        print(color)
objeye=Animals()
objcolor=Dog()
objcolor.foots(4)
objeye.ear(2)
objcolor.dogcolor("Black")