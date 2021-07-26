class calculator:

    def findAdd(self,x,y):
        return x+y

    def findSub(self,m,n):
        return m-n

    def findMulti(self,p,q):
        return p*q

    def findDiv(self,r,s):
        return r/s

    def findFloat(self,w, z):
        return w//z

findValues = calculator()
a = int(input("Give a value:"))    
b = int(input("Give a value:"))

addition = findValues.findAdd(a,b)
sub = findValues.findSub(a,b)
Multi = findValues.findMulti(a,b)
Div = findValues.findDiv(a,b)
Float = findValues.findFloat(a,b)
print(addition)
print(sub)
print(Multi)
print(Div)
print(Float)



