class emp:
    name="raja"

    def printName(self):
        print(self.name)

emp.printName=classmethod(emp.printName)
emp.printName()          