class Employee:
    emp_name="Rani"

    def printName(self):
        print(self.emp_name)


Employee.printName=classmethod(Employee.printName)
Employee.printName()
print(Employee.emp_name)