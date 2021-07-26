class Country:
    def __init__(self,Countryname):
        self.Countryname = Countryname
        print("Country")
  
class State(Country):
    def __init__(self,Countryname,state):
        self.state = state   
        super().__init__(Countryname)
        print("State")
  
class District(State):
    def __init__(self,Countryname,state,district):
        self.district=district
        self.Countryname=Countryname
        self.state=state
        super().__init__(Countryname,state) #super key is used to call its Base class Constructor not all first base class
        
    def printdistrict(self):
        print(self.Countryname, self.state,self.district)
d=District("India","TamilNadu","Cuddalore")
d.printdistrict()