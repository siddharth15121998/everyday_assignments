class Employee:
    name = "divya"
    
    def PrintName(self):
        print(self.name)

Employee.PrintName = classmethod(Employee.PrintName)
Employee.PrintName()
