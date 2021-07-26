class Laptops:
    def processor(self,process):
        self.process = process
        print("the Processor is: ",self.process)

class brand(Laptops):
    def bname(self,name):
        self.name = name 
        print("My laptop is" ,self.name)
    def graphical_memory(self,gm):
        self.gm = gm
        print("the Graphical memory is: ",self.gm)


objlaptops = Laptops()
objbname = brand()
#objbike.original_color("red")
objbname.bname("Dell")
objbname.processor("11th Generation Intel® Core™ i5-11300H Processor")
objbname.graphical_memory("discrete graphics with up to 2GB GDDR5")