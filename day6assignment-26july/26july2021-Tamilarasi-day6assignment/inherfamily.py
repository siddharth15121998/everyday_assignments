class Parent:
	def func1(self):
		print("Parent class")

class Child(Parent):
	def func2(self):
		print("Child class")


object = Child()
object.func1()
object.func2()
