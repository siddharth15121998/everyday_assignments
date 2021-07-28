class Rbi:
    def interest(self):
        print("10%")

class sbi(Rbi):
    def interest(self):
        print("7%")
class canara(Rbi):
    def interest(self):
        print("8.5%")

class hdfc(Rbi):
    def interest(self):
        print("6%")

obRbi = Rbi()
obRbi.interest()

obsbi=sbi()
obsbi.interest()
obcanara=canara()
obcanara.interest()
obhdfc=hdfc()
obhdfc.interest()