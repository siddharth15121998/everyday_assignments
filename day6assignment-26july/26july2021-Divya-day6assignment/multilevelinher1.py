class tour_package:
    def tourist_name(self,name):
        self.name = name
        print("the name of tourist is:",self.name)
        
class amount(tour_package):
    def amt(self,rupess):
        self.rupess = rupess
        print("Total amount to pay is: ", self.rupess)

class mode_of_transport(amount):
    def trans(self,transport):
        self.transport = transport
        print("the mode of transport is: ",self.transport)


objcustomer = mode_of_transport()
objcustomer.tourist_name("Divya")
objcustomer.amt("Rs.50000")
objcustomer.trans("Train")