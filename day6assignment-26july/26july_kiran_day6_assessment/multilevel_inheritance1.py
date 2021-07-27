class Animal:
    def speak(self):
        print("animal speaking")
class Dog(Animal):
    def bark(self):
        print("dog barking")
class DogChild(Dog):
    def eat(self):
        print("child dog eating")

d=DogChild()
d.bark()
d.speak()
d.eat()