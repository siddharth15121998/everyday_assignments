import re as r
txt = "The rain in Spain"
x = r.search("The Spain", txt)
if x:
  print("YES! We have a match!")
else:
  print("No match")
