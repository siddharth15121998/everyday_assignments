class A:
    def explore(self):
        print("explore() method called")

class B(A):
    def search(self):
        print("search() method called")

class C(B):
    def discover(self):
        print("discover() method called")

d_obj = C()
d_obj.explore()
d_obj.search()
d_obj.discover()
