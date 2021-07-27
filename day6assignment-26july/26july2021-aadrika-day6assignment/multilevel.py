class India:
    def alotNumber(self,num):
        self.num=num
        print(self.num)
class CarManufacturer(India):
    def makeCar(self,brand,color,price):
        self.brand=brand
        self.color=color
        self.price=price
        print(self.brand,self.color,self.price)

class Seller(CarManufacturer):
    def CustomerOrder(self,name,mobn):
        print(name, " ", mobn)

objseller=Seller()
objseller.CustomerOrder("aadrika",1234)
objseller.makeCar("ford","brown",100000)
objseller.alotNumber("mp150789")
ind=India()
# ind.alotNumber(12345)
# int.CustomerOrder("aa",12)
