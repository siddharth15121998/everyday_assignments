class India:
    def alotNumber(self,number):

        print(number)
    
class CarManufacturer(India):
    def makeACar(self,brand,color,price):
        print(brand,color,price)

class Seller(CarManufacturer):
    def CustomerOrder(self,name,mobno):
        print(name,mobno)

objSeller=Seller()
objSeller.CustomerOrder("Vaishnavi",7067776453)
objSeller.makeACar("BMW","Black",500000)
objSeller.alotNumber("MP23KB03456")