class tense:
    def Fancy(self,jeans):
        self.jeans=jeans
        print(self.jeans)
class present(tense):
    def Stylish(self,skirts):
        self.skirts=skirts
        print(self.skirts)
class future(present):
    def orthodox(self,saree):
        self.saree=saree
        print(self.saree)
obj=tense()
obj.Fancy("jeans")
obj.Stylish("skirts")
obj.orthodox("saree")

