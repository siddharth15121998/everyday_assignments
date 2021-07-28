class doctor:
    def eyespec(self,cost):
        self.cost=cost
        print(self.cost)
class patient(doctor):
    def reges(self,fee):
        self.fee=fee
        print(self.fee)

objdoc=doctor()
objpat=patient()  
objdoc.eyespec(1000)
objpat.reges(500)     
