class Animal():
    def acolor(self,color):
        self.color=color

        print(self.color)
class Dog(Animal):
    def sound(self,sound):
        self.sound=sound
        print(self.sound)
D=Dog()
A=Animal()
D.sound("Barking")
D.acolor("red")
A.acolor("black")
A.sound("speaks")