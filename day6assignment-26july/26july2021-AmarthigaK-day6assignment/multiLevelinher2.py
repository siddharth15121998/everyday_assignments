class India:
    def alotNumber(self,number):
        print(number)

class CarManufacturer(India):
    def makeAcar(self,brand,color,price):
        print(brand,color,price)

class seller(CarManufacturer):
    def CustomerOrder(self,Name,mobno):
        print(Name,mobno)

objseller=seller()
objseller.CustomerOrder("Aadhi",9876890876)
objseller.makeAcar("Ford","White", 100000)
objseller.alotNumber("MP15CB0449")
