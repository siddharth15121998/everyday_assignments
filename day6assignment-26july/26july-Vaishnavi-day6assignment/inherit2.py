class Parent():
       def first(self):
           print('father')
 
class Child(Parent):
       def second(self):
          print('Son')
 
ob = Child()
ob.first()
ob.second()