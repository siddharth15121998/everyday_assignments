class Team:
   def show_Team(self):
      print("This is our Team:")


class Testing(Team):
   TestingName = ""

   def show_Testing(self):
      print(self.TestingName)
 

class Dev(Team):
   DevName = ""

   def show_Dev(self):
      print(self.DevName) 
 

class Sprint(Testing, Dev):
   def show_parent(self):
      print("Testing :", self.TestingName)
      print("Dev :", self.DevName)

s1 = Sprint()  
s1.TestingName = "James"
s1.DevName = "Barter"
s1.show_Team()
s1.show_parent()