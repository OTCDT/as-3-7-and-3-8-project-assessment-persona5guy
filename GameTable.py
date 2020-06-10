##========= GameTable ========##
#---------- Version 0 ---------#
#::::::::::Contributers::::::::#
#         Josh Peacocke        #
#------------------------------#
#============Changes===========#
## Change date: 10/6/2020
## Change Branch: Collection
# Created basic class

#==========Game Class==========#

class Game:
    def __init__(self, game_name, _total_hours, played_hours, priority):
        self.game_name = game_name  #Add a games name
        self._total_hours = _total_hours #Add amonut of hours
        self.played_hours = played_hours #Add hours the user has played
        self.priority = priority #Add the priority given by the user
        self.remaining_hours = (self._total_hours - self.played_hours) #How many hours left until user finishes game
        self.true_priority = self.remaining_hours / self.priority #What is the priority of the game balanced with the time till finished
    
    def played(self, hours):
        if hours >= 0:
            self.played_hours += hours
        else:
            print("error, invalid amount of hours")
        
    

#=======Dummy Variables========#
persona5royal = Game("Persona 5 Royal", 150, 120, 1)
xenobladechronicles = Game("Xenoblade Chronicles", 45, 0, 2)
persona3fes = Game("Persona 3 FES", 88, 30, 3)


