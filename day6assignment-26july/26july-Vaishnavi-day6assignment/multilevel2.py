class Animal:  
    def speak(self):  
        print("Animal is Speaking")  
 
class Dog(Animal):  
    def bark(self):  
        print("dog is barking")  
 
class Puppy(Dog):  
    def eat(self):  
        print("Eat pedigre")  
objd = Puppy()  
objd.bark()  
objd.speak()  
objd.eat() 