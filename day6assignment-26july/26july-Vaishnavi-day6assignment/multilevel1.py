class GrandFather:
    def func1(self):
        print("Grand Father class")

class Father(GrandFather):
	def func2(self):
		print("Father class")

class Child(Father):
	def func3(self):
		print("Child class")
obj=Child()
obj.func1()
obj.func2()
obj.func3()