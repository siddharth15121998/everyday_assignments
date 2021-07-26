class thread:
    def woolen(self,Name,color,texture):
        print(Name,color,texture)

class cloth(thread):
    def weaving(self,materialType,color,texture):
        print(materialType,color,texture)

class dress(cloth):
    def stiching(self,color,size,design):
        print(color,size,design)

objdress=dress()

objdress.woolen("Merino","White", "fluffy")
objdress.weaving("cotton","pink","smooth")
objdress.stiching("Red","L","Flare")


    
