class Fruit():
       def first(self):
           print('Fruit')
 
class Apple(Fruit):
       def second(self):
          print('Apple')
 
ob = Apple()
ob.first()
ob.second()