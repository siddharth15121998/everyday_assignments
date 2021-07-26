class Shape:  
    def area(self):  
        print("surface area")  


class Rectangle(Shape):  
    def length(self):  
        print("length size")
    def height(self):
        print("height size")  


class Rectanglesize(Rectangle):  
    def width(self):  
        print("width size")  
d = Rectanglesize()  
d.length()  
d.height()  
d.width()
d.area()