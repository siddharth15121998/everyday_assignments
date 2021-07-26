class Family:
    def func1(self):
        print("family class")

class Parent(Family):
	def func2(self):
		print("Parent class")

class Child(Parent):
	def func3(self):
		print("Child class")
o=Child()
o.func1()
o.func2()
o.func3()
