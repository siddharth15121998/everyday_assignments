class Calculator:
    def operation(self):
        print("operation successfully")

class Calculate(Calculator):
    def add(self):
        print("add successfully")
d=Calculate()
d.add()
d.operation()