class selected_team_player_details:
    def player_name(self,name):
        self.name = name
        print("the name of the player is:",self.name)
        
class position(selected_team_player_details):
    def pstnt(self,pst):
        self.pst = pst
        print("the player position is: ", self.pst)

class district(position):
    def address(self,add):
        self.add = add
        print("From the district: ",self.add)
class selected_as(district):
    def line_in(self,as_of):
        self.as_off = as_of
        print("the player selected as: ",self.as_off)


objplayer = selected_as()
objplayer.player_name("Divya")
objplayer.pstnt("Ball controller")
objplayer.line_in("5")
objplayer.address("Thanjavur")