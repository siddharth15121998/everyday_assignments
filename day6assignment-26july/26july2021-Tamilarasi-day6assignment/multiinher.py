class Product:
    def productid(self,id):
        print(id)
    
class productManufac(Product):
    def productmaking(self,brand,price):
        print(brand,price)


class Seller(productManufac):
    def custOrder(self,name,mblno):
        print(name,mblno)

objSeller=Seller()
objSeller.custOrder("tamil",9876543210)
objSeller.productmaking("MS Office",10000)
objSeller.productid(7896)