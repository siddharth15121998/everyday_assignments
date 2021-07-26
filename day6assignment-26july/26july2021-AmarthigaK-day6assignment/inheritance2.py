class shoes:         #base class
    def jogging(self,bottom,model,brand):
        print(bottom,model,brand)

class nike(shoes):         #dervied class
    def sports(self,size,model):
        print(size,model) 


objnike = nike()
objnike.jogging("leather","sneaker","Prada")
objnike.sports("10","Nike Air Max")