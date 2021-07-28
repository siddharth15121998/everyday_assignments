class Cars:
    def color(self,color):
        self.col=color
        print(self.col)
class BMW(Cars):
     def speed(self,speed):
         self.sp=speed
         print(self.sp)
         

objcar=Cars()
objbmw=BMW()
#    objcar.color("pink")
#    objcar.sp(20)
objbmw.speed(300)
objbmw.color("red")

         



