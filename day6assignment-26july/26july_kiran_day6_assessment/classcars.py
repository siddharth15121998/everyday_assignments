class Cars:
    def findSpeed(self,dis,tim):
        return dis/tim
    colour="blue"
    brand="fortuner"
mycars=Cars()
a1=input("enter colour:")
a2=input("enter brand:")
d=int(input("enter distance:"))
t=int(input("enter time:"))
speed=mycars.findSpeed(d,t)
print(speed)
mycars.colour=a1
mycars.brand=a2
# print(mycars.colour)
# print(mycars.brand)
# defaultcar=Cars()
# print(defaultcar.colour)
# print(defaultcar.brand)