class Person:
    def __int__(self,myname):
        self.myname=myname

    def sayMyName(self):
        print(self.myname)

nam=input("enter the name:")
pi=Person(nam)
pi.sayMyName()
