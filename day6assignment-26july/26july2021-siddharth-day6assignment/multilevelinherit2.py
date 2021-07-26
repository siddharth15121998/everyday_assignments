class Animal:  
    def speak(self):  
        print("Animal is Speaking")  
 
class Dog(Animal):  
    def bark(self):  
        print("dog is barking")  
 
class DogChild(Dog):  
    def eat(self):  
        print("Eat chapati...")  
objd = DogChild()  
objd.bark()  
objd.speak()  
objd.eat() 