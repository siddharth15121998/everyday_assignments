class RBI:
    def InterestRate(self):
        print("RBI rate is 4.00%")

class CB(RBI):
    def InterestRate(self):
        print("SBI Interest rate is 5.20%")

class CBOI(RBI):
    def InterestRate(self):
        print("SBI Interest rate is 4.90%")

class IB(RBI):
    def InterestRate(self):
        print("SBI Interest rate is 5.60%")

class IOB(RBI):
    def InterestRate(self):
        print("SBI Interest rate is 5.65%")

class PSB(RBI):
    def InterestRate(self):
        print("SBI Interest rate is 5.65%")

class PNB(RBI):
    def InterestRate(self):
        print("PNBInterest rate is 5.70")

class SBI(RBI):
    def InterestRate(self):
        print("IDBI Interest rate is 5.50%")

class UCO(RBI):
    def InterestRate(self):
        print("IDBI Interest rate is 4.90%")

class UBOI(RBI):
    def InterestRate(self):
        print("IDBI Interest rate is 5.75%")

objcb=CB()
objcboi=CBOI()
objib=IB()
objiob=IOB()
objpsb=PSB()
objpnb=PNB()
objsbi=SBI()
objuco=UCO()
objuboi=UBOI()
objrbi=RBI()

objcb.InterestRate()
objcboi.InterestRate()
objib.InterestRate()
objiob.InterestRate()
objpsb.InterestRate()
objpnb.InterestRate()
objsbi.InterestRate()
objuco.InterestRate()
objuboi.InterestRate()
objrbi.InterestRate()

