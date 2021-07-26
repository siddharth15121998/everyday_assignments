class Quadrilateral:
    def myShape(self,shape):
        print(shape)
    
class Sides(Quadrilateral):
    def mySides(self,noofsides):
        print("No. of sides are",noofsides)

objquad=Quadrilateral()
objSides=Sides()

objquad.myShape("square")
objSides.mySides(4)
