class India:
    def alotnum(self,num):
        self.no=num
        print(self.no)
class Carman(India):
    def makecar(self,col,brand):
        self.col=col
        self.brand=brand
        print(self.col,self.brand) 
class Carseller(Carman):
    def customer(self,name,mob):
        self.name=name
        self.mob=mob
        print(self.name,self.mob)

objcarsell=Carseller()
objcarsell.customer("raj",9000) 
objcarsell.makecar("pink","ferrari")
objcarsell.alotnum(1)               