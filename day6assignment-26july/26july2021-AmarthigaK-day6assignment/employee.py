class Employee:
    emp_name = "Kowsalya"

    def printEmp(self):
        print(self.emp_name)

Employee.printEmp = classmethod(Employee.printEmp)
Employee.printEmp()
