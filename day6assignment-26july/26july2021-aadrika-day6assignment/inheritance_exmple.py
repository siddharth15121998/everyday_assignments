class Animal:
    def eating(self,food):
        self.eat=food
        print("I eat", self.eat)
class Cat(Animal):
    def sound(self,sound):
        self.sound=sound
        print("I make sound ",self.sound)

a=Animal()
b=Cat()
a.eating("animal food")
b.eating("fish")
b.sound("meow")