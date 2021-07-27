class Operations:
       a = 10
       b = 20
       def add(self):
              sum = self.a + self.b
              print("Sum of a and b is: ", sum)
 
class MyClass(Operations):
    c = 50
    d = 10
    def sub(self):
        s = self.c - self.d
        print("Subtraction of c and d is:" , s)
 
ob = MyClass()
ob.add()
ob.sub() 