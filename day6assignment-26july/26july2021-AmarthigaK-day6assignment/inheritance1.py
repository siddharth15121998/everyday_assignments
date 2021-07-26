class hotels:         #base class
    def givenMenu(self,menu):
        self.menu=menu
        print(self.menu)

class SaiSakthi(hotels):         #dervied class
    def service(self,Service):
        self.Service = Service
        print(self.Service) 

objhotels = hotels()
objSai = SaiSakthi()
#objhotels.givenMenu("Idly") #error
objSai.service("Good")
objSai.givenMenu("Idly")