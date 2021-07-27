class Parent:
      def eat(self):
          print("he is eating")
class father(Parent):
      def cooking(self):
          print("he is cooking")
class Child2(father):
      def running(self):
          print("he is running")
ob = Child2()
ob.eat()
ob.cooking()
ob.running()