##========= GameTable ========##
#---------- Version 1 ---------#
#::::::::::Contributers::::::::#
#         Josh Peacocke        #
#------------------------------#
#============Changes===========#
## Change date: 23/6/2020
<<<<<<< HEAD
## Change Branch: v1-bugfix
# Debugging of processes found in the testing process
=======
## Change Branch: bugfix-v1
# Testing and Feedback on 1st prototype
>>>>>>> e76397c1ab49d14ac4598d90bc1ab6f0b7d10ba9

#==========Game Class==========#
class Game:
    def __init__(
        self, game_name, _total_hours,
        played_hours, priority):
        #Initalisation class to set intial variables
        self.game_name = game_name  #Add a games name
        self._total_hours = _total_hours #Add amonut of hours
        self.played_hours = played_hours #Add hours the user has played
        self.priority = priority #Add the priority given by the user
<<<<<<< HEAD
        self.remaining_hours = (self._total_hours - self.played_hours) #How many hours left until user finishes game
        self.true_priority = self.remaining_hours / self.priority #What is the priority of the game balanced with the time till finished
=======
        #How many hours left until user finishes game
        self.remaining_hours = (self._total_hours - self.played_hours) 
        #What is the priority of the game balanced with the time till finished
        self.true_priority = self.remaining_hours * self.priority 
>>>>>>> e76397c1ab49d14ac4598d90bc1ab6f0b7d10ba9
    
    def update_values(
        self):
        #Update remaining hours
        self.remaining_hours = self._total_hours - self.played_hours 
        #Update the true priority
        self.true_priority = self.remaining_hours / self.priority
        
    def played(
        self, hours):
        if (hours >= 0): 
        #Ensure the hours being added is atleast 0 or above
            self.played_hours += hours
            self.update_values()
        else:
        #If below 0 hours, present error
            print("error, invalid amount of hours") 
    
    def change_priority(
        self, new_priority): 
        #If the user wants to change priority, this allows them
        self.priority = new_priority #set the new priority as priority
        self.update_values()

    def increase_time(
        self, finish_hours): 
        #Update the time if the user feels more time is needed
        self._total_hours += finish_hours  #Add hours to the total
        self.update_values()

#===========Functions==========#
def sort_games(
    game_list): 
    #This function is designed to sort the list of games by order of priority
    def sort_key(game): #Get the games true priority as a key for sorting
        return game.true_priority
    
    game_list.sort(key=sort_key) #sort the list using true priority
    return game_list #Give the list back

<<<<<<< HEAD
def add_games(): #This is to let users create objects to be added to lists
    name=input("What's the games name? ") #Add a name
    total_hours=float(input("How many hours approximately will it take to finish the game? ")) #The total hours to play game
    played_hours=float(input("How many hours have you played? ")) #How many hours have been played
    priority=int(input("From 10 being maximum priority, what is the priority to finish the game ")) #How much does the user want to play it
    return(Game(name,total_hours,played_hours,priority)) #Give back the array

def collection(): #Collect the add games into a list
    game_array = [] #Empty array to add games to
    while input("Would you like to add a game? y/n ") == "y",: #Keep adding games until user doesn't want to add more
        game_array.append(add_games()) #Append the game to the array
    return game_array #Give back the created array
=======
def add_games(): 
    #This is to let users create objects to be added to lists
    name=input("""
         What's the games name? """) #Add a name
    #haha funny number line
    #The total hours to play game
    total_hours=int(input("""
                How many hours approximately will it take to finish the game? """)) 
    #How many hours have been played
    played_hours=int(input("""
                 How many hours have you played? """)) 
    #How much does the user want to play it
    priority=int(input("""
             From 0 being maximum priority, what is the priority to finish the game """))
    #Give back the array
    return(
        Game(name,total_hours,played_hours,priority)) 

def collection(): 
    #Collect the add games into a list
    #Empty array to add games to
    game_array = [] 
    #Keep adding games until user doesn't want to add more
    while input("Would you like to add a game? y/n ") == "y": 
        #Append the game to the array
        game_array.append(add_games()) 
    #Give back the created array
    return game_array 
>>>>>>> e76397c1ab49d14ac4598d90bc1ab6f0b7d10ba9
#=======Dummy Variables========#
game_array = collection()

sorted_list = sort_games(game_array)
print("All games in list \/ \/ \/")
for i in sorted_list: print(i.game_name + ' ' + str(i.true_priority))
print("Finish list /\ /\ /\ \n \n \n")
print("You should play " + sorted_list[0].game_name)


