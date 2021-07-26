class Car:
    color="black"
    model="kia"
    def mileage(self,l,k):
        return k/l
c=Car()
c.color="red"
c.model="seltos"
l=50
k=1000
print(c.color)
print(c.model)
print(c.mileage(l,k))
