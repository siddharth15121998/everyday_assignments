class Country:
    def countrycode(self,code):
        print(code)

class India(Country):
    def minister(self,defence,foriegn,culture):
        print(defence,foriegn,culture)

class states(India):
    def states_india(self,stateName,Scode):
        print(stateName,Scode)

objstates=states()
objstates.states_india("TamilNadu",33)
objstates.minister("Nirmala","Jaisankar","KishanReddy")
objstates.countrycode("+91")