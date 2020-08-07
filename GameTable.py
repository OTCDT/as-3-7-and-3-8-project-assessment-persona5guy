##========= GameTable ========##
#---------- Version 1 ---------#
#::::::::::Contributers::::::::#
#         Josh Peacocke        #
#------------------------------#
#============Changes===========#
"""
 Change date: 5/8/2020
 Change Branch: GUI
 Comments added
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
        # Check for any errors made by user
        self.game_name = name
        self._total_hours = t_hours
        self.played_hours = p_hours
        self.priority = new_priority
        self.update_values()

# haha funny number line
    def increase_time(
        self, finish_hours): 
        # Update the time if the user feels more time is needed

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
#============GUI===============#

#-------GUI functions----------#

# Add in a new game
def add_game():
    add_button.grid_forget()
    confirm_game.grid(row=1,column=0)
    # Create a new row for the new game in each array
    var_array.append([])
    entry_array.append([])
    for j in range(0,4):
        if j == 0:
            # If first column use a string(game name)
            var_array[-1].append(StringVar())
        elif j != 0:
            # If other column us a number
            var_array[-1].append(DoubleVar())
        # Add in the entry box
        entry_array[-1].append(ttk.Entry(games_frame,
                     textvariable = var_array[-1][j]))
    col_num = 0
    for entry in entry_array[-1]:
        # Place the new entries in the last row
        entry.grid(row = len(sorted_list) + 1, column = col_num)
        col_num += 1
    # Add in a delete button at the end of te row
    exit_array.append(Button(games_frame, 
                            command=lambda row=len(sorted_list): delete(row)))
    exit_array[-1].grid(row = len(sorted_list) + 1, column = 4)
    button_frame.grid(row = len(sorted_list) + 2)
    # Readjust the window size to accomodate more new games
    root.geometry("520x" + str(len(sorted_list)*40+90))

# Collect in a new game from the user
def collect_game():
    # Remove the confirm button
    confirm_game.grid_forget()
    # Take information from the entry array and add it into a new object
    new_game = Game(var_array[-1][0].get(),var_array[-1][1].get()
                    ,var_array[-1][2].get(),var_array[-1][3].get())
    # Add the object into the array
    game_array.append(new_game)
    # Sort this array to find the 'best option'
    sorted_list = sort_games(game_array)
    # Add the add button back
    add_button.grid(row=1,column=0)

# Delete a game if user desires
def delete(array_loc):
    # Remove each entry row
    for entry in entry_array[array_loc]:
        entry.grid_forget()
    # Remove the delete button
    exit_array[array_loc].grid_forget()
    # Remove this from any related tables
    sorted_list.pop(array_loc)
    entry_array.pop(array_loc)
    var_array.pop(array_loc)

# Show the user what the program reccomends
def present_game():
    # Save all the changes made to the list
    confirm_changes()
    new_list = sort_games(sorted_list)
    # Show the new list
    suggestion_label = Label(root, text = "GameTable reccomends " 
    + new_list[0].game_name)
    suggestion_label.grid(row = 2, columnspan = 4)
    # Resize to fit the reccomendation
    root.geometry("520x" + str(len(sorted_list)*40 + 100))

# Allow the user to add in new values
def confirm_changes():
    game_num = 0
    # For each game, change the values using the entries
    error_message = StringVar()
    error_label = Label(root, textvariable = error_message)
    for game in sorted_list:
        if var_array[game_num][3].get() < 0:
            error_message.set("Please set priority above 0")
            error_label.grid(row = 2, column_span = 4)
        if var_array[game_num][1] < var_array[game_num][2]:
            error_message.set("Please set total hours to be higher than played")
            error_label.grid(row = 2, column_span = 4)
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
    # Make sure the length of the list is larger than one
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
    # If not, then make empty arrays
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
        # Create and grid a delete button
        exit_array.append(Button(games_frame, 
                               command=lambda row=game_num: delete(row)))
        exit_array[game_num].grid(row = game_num + 1, column = column_num)
        column_num = 0
        game_num += 1
    return exit_array, var_array, entry_array


# Buttons made at the button used to manipulate the program
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
# Save any changes
save(sorted_list)