class India:
    def first(self):
        print ('India is the largest democratic country in the world')
class MP(India):
    def sec(self):
        print ('Madhya Pradesh is heart of india')
class Bhopal(MP):
    def third(self):
        print ('Bhopal is city of lakes')
b=Bhopal()
b.first()
b.sec()
b.third()