class Animal:  
    def sound(self):  
        print("Animal Sounding")  

class Cat(Animal):  
    def meow(self):  
        print("cat sounding")  
d = Cat()  
d.meow()  
d.sound()