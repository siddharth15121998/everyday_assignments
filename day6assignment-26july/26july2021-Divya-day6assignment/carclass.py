class Cars:
    color = "black"
    brand = "Benz"

    def Find_mileage(self,liter,km):
        return km/liter


My_car = Cars()
c = input("enter a color: ")
b = input("enter a brand name: ")

li = int(input("enter a liter: "))
kilometer = int(input("enter a km: "))

My_mileage = My_car.Find_mileage(li,kilometer)
My_car.color=c
My_car.brand=b
print(My_car.color)
print(My_car.brand)
print(My_mileage)
#to print default variables_values using object
default_car = Cars()
print(default_car.color)
print(default_car.brand)
