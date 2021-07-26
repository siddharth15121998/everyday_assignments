class Animal:
    def speak(self):
        print("Animal is speaking")

class Cat(Animal):
    def meows(self):
        print("Cat is meows")
d=Cat()
d.meows()
d.speak()        