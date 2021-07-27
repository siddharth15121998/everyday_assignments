class Cars:
    color="black"
    brand="BMW"

    def findMileage(self,liter,km):
        return km/liter


myCar=Cars()
cl=input("enter your color :")
b=input("enter your brand :")

lit=int(input("enter fuel consuption :"))
km=int(input("enter kilometers :"))
mileage=myCar.findMileage(lit,km)


print(mileage)
myCar.color=cl
myCar.brand=b
print(myCar.color)
print(myCar.brand)

#default values accessing through another object
# defcar=Cars()
# print(defcar.color)
# print(defcar.brand)
