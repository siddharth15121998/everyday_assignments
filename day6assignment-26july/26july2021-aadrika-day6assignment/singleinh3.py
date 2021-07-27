class Devices:
    def Name(self):
        print("devices")
class Smartphone(Devices):
    def working(self):
        print("smartphones used for calling")

sp=Smartphone()
sp.Name()
sp.working()