##========= GameTable ========##
#---------- Version 0 ---------#
#::::::::::Contributers::::::::#
#         Josh Peacocke        #
#------------------------------#
#============Changes===========#
## Change date: 16/6/2020
## Change Branch: key sort
# testing the sorting key method

#==========Game Class==========#
class Game:
    def __init__(self, game_name, _total_hours, played_hours, priority):
        self.game_name = game_name  #Add a games name
        self._total_hours = _total_hours #Add amonut of hours
        self.played_hours = played_hours #Add hours the user has played
        self.priority = priority #Add the priority given by the user
        self.remaining_hours = (self._total_hours - self.played_hours) #How many hours left until user finishes game
        self.true_priority = self.remaining_hours * self.priority #What is the priority of the game balanced with the time till finished
    
    def update_values(self):
        self.remaining_hours = self._total_hours - self.played_hours #Update remaining hours
        self.true_priority = self.remaining_hours / self.priority #Update the true priority

    def played(self, hours):
        if hours >= 0: #Ensure the hours being added is atleast 0 or above
            self.played_hours += hours
            self.update_values()
        else:
            print("error, invalid amount of hours") #If below 0 hours, present error
    
    def change_priority(self, new_priority): #If the user wants to change priority, this allows them
        self.priority = new_priority #set the new priority as priority
        self.update_values()

    def increase_time(self, finish_hours): #Update the time if the user feels more time is needed
        self._total_hours += finish_hours  #Add hours to the total
        self.update_values()


#===========Functions==========#
def sort_games(list):
    def sort_key(game):
        return game.true_priority
    
    list.sort(key=sort_key)
    return list
#=======Dummy Variables========#
persona4golden = Game("Persona 4 Golden", 102, 0, 2)
persona5royal = Game("Persona 5 Royal", 150, 120, 1)
xenobladechronicles = Game("Xenoblade Chronicles", 45, 0, 2)
persona3fes = Game("Persona 3 FES", 88, 30, 3)

dummy_list = [persona3fes,persona4golden,persona5royal,xenobladechronicles]

sorted_list = sort_games(dummy_list)
for i in sorted_list: print(i.game_name + ' ' + str(i.true_priority))