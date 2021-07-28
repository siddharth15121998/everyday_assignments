class rbi:
    def interset(self):
        print("interset is 9")

class sbi(rbi):
    def interset(self):
        print("interset is 10")

class pnb(sbi):
    def interset(self):
        print("interset is 5")

class icici(pnb):
    def interset(self):
        print("interset is 9")
obj1=icici()
obj1.interset()
obj2=pnb()
obj2.interset()
obj3=sbi()