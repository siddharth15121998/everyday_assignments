class mobile:
    def mycolor(self,color):
        self.color=color
        print(self.color)
class brand(mobile):
    def realme (self,android):
        self.android=android
        print(self.android)
obj1=mobile()
obj2=brand()
obj1.mycolor("Black")
obj2.realme("samsung M30S")