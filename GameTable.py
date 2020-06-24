##========= GameTable ========##
#---------- Version 1 ---------#
#::::::::::Contributers::::::::#
#         Josh Peacocke        #
#------------------------------#
#============Changes===========#
               """
 Change date: 23/6/2020
 Change Branch: v1-stylefix
 Testing and Feedback on 1st prototype
               """
#==========Game Class==========#
class Game:
    def __init__(
        self, game_name, _total_hours,
        played_hours, priority): 
        # Initalisation class to set intial variables  
        # Add a games name
        self.game_name = game_name
        # Add amonut of hours
        self._total_hours = _total_hours
        # Add hours the user has played
        self.played_hours = played_hours 
        # Add the priority given by the user
        self.priority = priority 
        # How many hours left until user finishes game
        self.remaining_hours = (self._total_hours 
                                - self.played_hours) 
        # What is the priority of the game balanced with the time till finished
        self.true_priority = (self.remaining_hours 
                              * self.priority)
    
    def update_values(
        self):
        # Update remaining hours
        self.remaining_hours = (self._total_hours 
                                - self.played_hours) 
        # Update the true priority
        self.true_priority = (self.remaining_hours 
                              / self.priority)
        
    def played(
        self, hours):
        if (hours >= 0): 
        # Ensure the hours being added is atleast 0 or above
            self.played_hours += hours
            self.update_values()
        else:
        # If below 0 hours, present error
            print("error, invalid amount of hours") 
    
    def change_priority(
        self, new_priority): 
        # If the user wants to change priority, this allows them to change
        # of games to be played
        # set the new priority as priority
        self.priority = new_priority 
        self.update_values()

    def increase_time(
        self, finish_hours): 
        # Update the time if the user feels more time is needed
        self._total_hours += finish_hours  # Add hours to the total
        self.update_values()

#===========Functions==========#

def sort_games(
    game_list): 
    # This function is designed to sort the list of games by order of priority
    # haha funny number line
    # Get the games true priority as a key for sorting
    def sort_key(game): 
        return game.true_priority
    # sort the list using true priority
    game_list.sort(key=sort_key) 
    # Give the list back
    return game_list 

def add_games(): 
    # This is to let users create objects to be added to lists
    # Define a name
    name = input("""
         What's the games name? """) 
    # The total hours to play game
    total_hours = int(input("""
                How many hours approximately 
                will it take to finish the game? """)) 
    # How many hours have been played
    played_hours = int(input("""
                How many hours have you played? """)) 
    # How much does the user want to play it
    priority = int(input("""
                From 0 being maximum priority, what is 
                the priority to finish the game """))
    # Give back the array
    return(
        Game(name,total_hours,played_hours,priority)) 

def collection(): 
    # Collect the add games into a list
    # Empty array to add games to 
    game_array = [] 
    # Keep adding games until user doesn't want to add more
    while input("Would you like to add a game? y/n ") == "y": 
        # Append the game to the array
        game_array.append(add_games()) 
    # Give back the created array
    return game_array 

#=======Dummy Variables========#

game_array = collection()
sorted_list = sort_games(game_array)
print("All games in list \/ \/ \/")
for i in sorted_list: print(i.game_name + ' ' + str(i.true_priority))
print("""Finish list /\ /\ /\ 
    \n 
    \n 
    \n""")
print("You should play " + sorted_list[0].game_name)


