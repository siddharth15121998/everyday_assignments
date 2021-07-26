class Laptops:               # laptop is a class which contains to attribute/parameter/ariables
    color = "black"         
    brand = "HP"
    #creating a function for defining battery power of the laptop
    def findBattery(self, volt, current):
        return volt*current

#object
myLaptop = Laptops()   # here the class (Laptops) is a function 
k = input("Enter color:")
j = input("Enter brand:")

v = (int(input("Give the value of power:")))
i = (int(input("Give the value of time:")))
battery = myLaptop.findBattery(v, i)

myLaptop.color = k
myLaptop.brand = j

print(myLaptop.color)
print(myLaptop.brand)

#printing default values using object
defaultLaptop = Laptops()
print(defaultLaptop.color)
print(defaultLaptop.brand)
print(battery)

