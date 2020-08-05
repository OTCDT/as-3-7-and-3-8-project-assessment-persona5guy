##========= GameTable ========##
#---------- Version 1 ---------#
#::::::::::Contributers::::::::#
#         Josh Peacocke        #
#------------------------------#
#============Changes===========#
"""
 Change date: 5/8/2020
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
    
    def change_values(
        self, name, t_hours, p_hours, new_priority): 
        # If the user wants to change priority, this allows them to change
        # of games to be played
        # set the new priority as priority
        self.game_name = name
        self._total_hours = t_hours
        self.played_hours = p_hours
        self.priority = new_priority
        self.update_values()

    def increase_time(
        self, finish_hours): 
        # Update the time if the user feels more time is needed
        # haha funny number line
        self._total_hours += finish_hours  # Add hours to the total
        self.update_values()

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
sorted_list = sort_games(game_array)
#------------GUI---------------#

#-------GUI functions----------#

# Add in a new game
def add_game():
    add_button.grid_forget()
    confirm_game.grid(row=1,column=0)
    # Create a new row for the new game
    var_array.append([])
    entry_array.append([])
    for j in range(0,4):
        if j == 0:
            var_array[-1].append(StringVar())
        elif j != 0:
            var_array[-1].append(DoubleVar())
        entry_array[-1].append(ttk.Entry(games_frame,
                     textvariable = var_array[-1][j]))
    col_num = 0
    for entry in entry_array[-1]:
        entry.grid(row = len(sorted_list) + 1, column = col_num)
        col_num += 1
    exit_array.append(Button(games_frame, 
                            command=lambda row=len(sorted_list): delete(row)))
    exit_array[-1].grid(row = len(sorted_list) + 1, column = 4)
    button_frame.grid(row = len(sorted_list) + 2)
    root.geometry("520x" + str(len(sorted_list)*40+50 + 40))

def collect_game():
    confirm_game.grid_forget()
    new_game = Game(var_array[-1][0].get(),var_array[-1][1].get()
                    ,var_array[-1][2].get(),var_array[-1][3].get())
    print(new_game.game_name)
    game_array.append(new_game)
    sorted_list = sort_games(game_array)
    add_button.grid(row=1,column=0)

def delete(array_loc):
    for entry in entry_array[array_loc]:
        entry.grid_forget()
    exit_array[array_loc].grid_forget()
    root.mainloop()
    sorted_list.pop(array_loc)
    entry_array.pop(array_loc)
    var_array.pop(array_loc)

def present_game():
    confirm_changes()
    games_frame.grid_forget()
    new_list = sort_games(sorted_list)
    suggestion_label = Label(root, text = "GameTable reccomends " + new_list[0].game_name)
    suggestion_label.place(relx=0.5, rely=0.5, anchor=CENTER)

def confirm_changes():
    game_num = 0
    for game in sorted_list:
        game.change_values(
        var_array[game_num][0].get(), var_array[game_num][1].get(),
         var_array[game_num][2].get(), var_array[game_num][3].get())
        game_num += 1
        print(game.game_name + str(game.played_hours))
# GUI presentation
root = Tk()
root.title("GameTable")
root.geometry("520x" + str(len(sorted_list)*40+50))
# Make a Table Header for all the objects in the table
games_frame = ttk.LabelFrame(root, text="Edit Game Info")
games_frame.grid(row=0,column=0, columnspan = 3, sticky="NSEW")

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
def table_make(sorted_list):
    row_num = 1
    column_num = 0
    if len(sorted_list) > 0:
        for game in sorted_list:
            var_array = []
            entry_array = []
            # Create a row for each game in the list
            for i in range(0,len(sorted_list)):
                var_array.append([])
                entry_array.append([])
            # Create a column for each data entry
                for j in range(0,4):
                    if j == 0:
                        var_array[i].append(StringVar())
                    elif j != 0:
                        var_array[i].append(DoubleVar())
                    # Create an entry into a table
                    # with specific coordinates (i,j)
                    entry_array[i].append(ttk.Entry(games_frame,
                    textvariable = var_array[i][j]))
    else:
        var_array = []
        entry_array = []
    game_num = 0
    exit_array = []
    # Placement of each section of data
    for game in var_array:
        # Set all shown variables
        game[0].set(sorted_list[game_num].game_name)
        game[1].set(sorted_list[game_num]._total_hours)
        game[2].set(sorted_list[game_num].played_hours)
        game[3].set(sorted_list[game_num].priority)
        for entry in game:
            #Place the grid into it's correct place
            entry_array[game_num][column_num].grid(row = game_num + 1, 
            column = column_num)
            column_num += 1
        exit_array.append(Button(games_frame, 
                               command=lambda row=game_num: delete(row)))
        exit_array[game_num].grid(row = game_num + 1, column = column_num)
        column_num = 0
        game_num += 1
    return exit_array, var_array, entry_array


# See if user is adding a game or not
  
button_frame = ttk.LabelFrame(games_frame)
button_frame.grid(row = len(sorted_list) + 2, columnspan = 4)    
add_button = ttk.Button(button_frame, text = "Add a new game", command = add_game)
add_button.grid(row=1, column=0)
confirm_game = ttk.Button(button_frame, text = "Confirm game", command = collect_game)
change_confirm = ttk.Button(button_frame, text = "Confirm Changes", command = confirm_changes)
change_confirm.grid(row = 1, column = 1)
find_game = ttk.Button(button_frame, text = "Find what to play", command = present_game)
find_game.grid(row = 1, column = 2)
# Run the GUI
exit_array, var_array, entry_array = table_make(sorted_list)
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