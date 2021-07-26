class Animal:  
    def sound(self):  
        print("Animal sounding")  


class Cat(Animal):  
    def meow(self):  
        print("meow")  


class CatChild(Cat):  
    def eat(self):  
        print("drinking milk")  
d = CatChild()  
d.meow()  
d.sound()  
d.eat()