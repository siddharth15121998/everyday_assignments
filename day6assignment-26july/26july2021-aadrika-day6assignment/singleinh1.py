class Quadrilateral:
    def myShape(self,shape):
        print(shape)
    
class Sides(Quadrilateral):
    def mySides(self,noofsides):
        print("No. of sides are",noofsides)

quad=Quadrilateral()
Side=Sides()
quad.myShape("square")
Side.mySides(4)