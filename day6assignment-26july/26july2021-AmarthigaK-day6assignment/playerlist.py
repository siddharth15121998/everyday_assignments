class player:
    def __init__(self,name,gamename,reg_no):
        self.playername = name
        self.game=gamename
        self.reg=reg_no

obj=[]
obj.append(player("Amarthiga","Badminton",1234))
obj.append(player("div","basketball",1235))

print(obj[0].game)
print(obj[1].reg)


        