class addnumber:
    def add(self,n1,n2):
        return n1+n2
class subnumber:
    def sub(self,n1,n2):
        return n1-n2
class multiplynumber:
    def mul(self,n1,n2):
        return n1*n2
class calculator(addnumber,subnumber,multiplynumber):
    pass

obj1=calculator()
print(obj1.add(5,3))
print(obj1.sub(5,3))
print(obj1.mul(5,3))
print(issubclass(calculator,addnumber))
print(issubclass(addnumber,subnumber))
print(issubclass(addnumber,multiplynumber))
