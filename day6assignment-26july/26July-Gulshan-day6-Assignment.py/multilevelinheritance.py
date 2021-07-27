class Trees:
    def mango(self,sweet):
        self.Bitter=sweet
        print(self.Bitter)
class Smallplants(Trees):
    def Tulasi(self,peppery):
        self.peppery=peppery
        print(self.peppery)
class Flowerplants(Smallplants):
    def Rose(self,smell):
        self.smell=smell
        print(self.smell)
obj=Flowerplants()
obj.mango("Mango is sweet taste")
obj.Tulasi("peppery taste")
obj.Rose("smells good")