class Father():
    def __init__(self, name):
        self.name = name
  
    # To get name
    def generate(self):
        print (self.name)
  
  
# Inherited or Sub class (Note Person in bracket)
class Child(Father):
      
    # Constructor
    def __init__(self, name, age):
        super().__init__( name)
        self.age = age
  
    # To get name
    def generate(self):
        print(self.name, self.age)
  
# Inherited or Sub class (Note Person in bracket)
class GrandChild(Child):
    def __init__(self, name, age, address):
        
        self.name=name
        self.age=age
        self.address = address
        super().__init__( name, age)
    def generate(self):
        print(self.name,self.age ,self.address)      

g = GrandChild("Balu", 21, "Noida")  
g.generate()