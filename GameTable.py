##========= GameTable ========##
#---------- Version 1 ---------#
#::::::::::Contributers::::::::#
#         Josh Peacocke        #
#------------------------------#
#============Changes===========#
"""
 Change date: 22/7/2020
 Change Branch: GUI
 GUI added in
 """

#============Imports===========#
import pickle as pkl
from tkinter import ttk
from tkinter import *
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
        # What is the priority of the game
        # balanced with the time till finished
        self.true_priority = (self.remaining_hours 
                              / self.priority)
    
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
# haha funny number line
#===========Functions==========# 

def boolean_input(user_input):
    while True:
        message = input(user_input)
            # This will transform a string input into a true or false
        POSITIVE_ANSWERS = ["yes","y","ok"]
        NEGATIVE_ANSWERS = ["no", "n"]
        # If the message is positive then return positive
        for i in POSITIVE_ANSWERS:
            if message.lower().strip(" ") == i:
                return "positive"
        # If the message is negative then return negative
        for j in NEGATIVE_ANSWERS:
             if message.lower().strip(" ") == j:
                return "negative"
    # If the user did not answer, then repeat

def sort_games(
    game_list): 
    # This function is designed to sort the list of games by order of priority
    # Get the games true priority as a key for sorting
    def sort_key(game): 
        return game.true_priority
    # sort the list using true priority
    game_list.sort(key=sort_key) 
    # Give the list back
    return game_list 

#---------Collection----------#

def add_games(): 
    # Dummy Variables
    repeating = "no answer"
    total_hours = -1
    played_hours = 0
    # Define a name
    name = input(
            "What's the games name? ") 
    # Does the game finish?
    while repeating == "no answer":
        repeating = boolean_input(
                                "Does the game have a finish time? (y/n) ")
        # Select between an 'infinite' or finite game
        if repeating == "negative":
            total_hours = float(input("How many hours for one session? "))
        elif repeating == "positive":
            while played_hours > total_hours or 0 > total_hours or 0 > played_hours:
                # The total hours to play game
                total_hours = float(input(
                           "How many hours approximately "
                           + "will it take to finish the game? ")) 
                # How many hours have been played
                played_hours = float(input(
                            "How many hours have you played? "))
                if total_hours < played_hours:
                    print("Ensure the total hours is more than the played hours")
                elif 0 > total_hours or  0 > played_hours:
                    print("The hours must be a positive value")
    # How much does the user want to play it
    priority = float(input(
                "Enter a priority from 1(Low) to 10(High) "))
    # If it is not the range, make the user input in the range
    while not 0 <= priority <= 10:
            priority = float(input("Please enter a value between 1 to 10"))
    # Give back the array
    return(
        Game(name,total_hours,played_hours,priority))

def collection(): 
    # Collect the add games into a list
    # Empty array to add games to 
    game_array = []
    # Keep adding games until user doesn't want to add more
    while boolean_input("\nWould you like to add a game? (y/n)") == "positive": 
        # Append the game to the array
        game_array.append(add_games())
    # Give back the created array
    return game_array 

#--------save system----------#

def save(object_array):
    # Save the game into a file
    with open("game.dat", "wb") as output:
        pkl.dump(object_array, output)
def load():
    # Load game into the file
    try:
        with open("game.dat", "rb") as input:
         return pkl.load(input)
    except FileNotFoundError:
        return []
#---------Editing data---------#
game_array = load()

new_games = collection()
for game in new_games:
    game_array.append(game)
sorted_list = sort_games(game_array)
#------------GUI---------------#
root = Tk()
root.title("GameTable")

# Make a Table Header for all the objects in the table
games_frame = ttk.LabelFrame(root, text="Added Games")
games_frame.grid(row=0,column=0,sticky="NSEW")

# Title for game name
table_title_gamename = ttk.Label(games_frame, text = "Game Name")
table_title_gamename.grid(row=0 , column=0, padx=10, pady=2)

#Title for total hours
table_title_totalhours = ttk.Label(games_frame, text = "Total Hours")
table_title_totalhours.grid(row=0,column=1, padx=10, pady=2)

#Title for played hours
table_title_playedhours = ttk.Label(games_frame, text = "Played Hours")
table_title_playedhours.grid(row=0,column=2, padx=10, pady=2)

#Title for priority
table_title_priority = ttk.Label(games_frame, text = "Priority")
table_title_priority.grid(row=0,column=3, padx=10, pady=2)

#Table Creation
row_num = 1
column_num = 0
for game in sorted_list:
    # Create 2d Array of each entry
    string_array = []
    entry_array = []
    for i in range(0,len(sorted_list)):
        string_array.append([])
        entry_array.append([])
        for j in range(0,4):
            if j == 0:
                string_array[i].append(StringVar())
            elif j != 0:
                string_array[i].append(DoubleVar())
            entry_array[i].append(Entry(games_frame,
            textvariable = string_array[i][j]))

game_num = 0
# Row of each entry
for game in string_array:
    game[0].set(sorted_list[game_num].game_name)
    game[1].set(sorted_list[game_num]._total_hours)
    game[2].set(sorted_list[game_num].played_hours)
    game[3].set(sorted_list[game_num].priority)
    for entry in game:
        entry_array[row_num - 1][column_num].grid(row = row_num, column = column_num)
        column_num += 1
    column_num = 0
    row_num += 1
    game_num += 1
# Run the GUI
root.mainloop()
#=======Dummy Variables========#
print("All games in list")
for i in sorted_list: print(i.game_name + ' ' + str(i.true_priority))
print("""Finish list
    \n 
    \n 
    \n""")
if len(sorted_list) > 0:
    print("You should play " + sorted_list[0].game_name)
else:
    print("No games were added")

save(sorted_list)