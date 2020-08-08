##========= GameTable ========##
#---------- Version 1 ---------#
#::::::::::Contributers::::::::#
#         Josh Peacocke        #
#------------------------------#
#============Changes===========#
"""
 Change date: 8/8/2020
 Change Branch: GUI-rework
 GUI structure to be changed into standard
 object oriented
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
class gametable_ui(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.game_list = sort_games(load())
        self.games_frame = LabelFrame(root)
        self.games_frame.grid(row=0,column=0)
        self.size_image = PhotoImage(width=10,height=10)
        #Table Creation
        row_num = 1
        column_num = 0
        # Make sure the length of the list is larger than one
        if len(self.game_list) > 0:
            for game in self.game_list:
                self.var_array = []
                self.entry_array = []
                # Create a row for each game in the list
                for i in range(0,len(self.game_list)):
                    self.var_array.append([])
                    self.entry_array.append([])
                # Create a column for each data entry
                    for j in range(0,4):
                        if j == 0:
                            self.var_array[i].append(StringVar())
                        elif j != 0:
                            self.var_array[i].append(DoubleVar())
                        # Create an entry into a table
                        # with specific coordinates (i,j)
                        self.entry_array[i].append(Entry(self.games_frame,
                        textvariable = self.var_array[i][j]))
        # If not, then make empty arrays
        else:
            self.var_array = []
            self.entry_array = []
        game_num = 0
        self.exit_array = []
        # Titles for the table
        # Title for game name
        self.table_title_gamename = ttk.Label(self.games_frame,
                                             text = "Game Name")
        self.table_title_gamename.grid(row=0 , column=0, padx=10, pady=2)

        #Title for total hours
        self.table_title_totalhours = ttk.Label(self.games_frame,
                                                 text = "Total Hours")
        self.table_title_totalhours.grid(row=0,column=1, padx=10, pady=2)

        #Title for played hours
        self.table_title_playedhours = ttk.Label(self.games_frame,
                                                 text = "Played Hours")
        self.table_title_playedhours.grid(row=0,column=2, padx=10, pady=2)

        #Title for priority
        self.table_title_priority = ttk.Label(self.games_frame,
                                             text = "Priority")
        self.table_title_priority.grid(row=0,column=3, padx=10, pady=2)
        # Placement of each section of data
        for game in self.var_array:
            # Set all shown variables
            game[0].set(self.game_list[game_num].game_name)
            game[1].set(self.game_list[game_num]._total_hours)
            game[2].set(self.game_list[game_num].played_hours)
            game[3].set(self.game_list[game_num].priority)
            for entry in game:
                #Place the grid into it's correct place
                self.entry_array[game_num][column_num].grid(
                                    row = game_num + 1, column = column_num)
                column_num += 1
            # Create and grid a delete button
            self.exit_array.append(Button(self.games_frame, 
                        image = self.size_image, bg = '#ff8888',
                         command=lambda row=game_num: delete(row)))
            self.exit_array[game_num].grid(row = game_num + 1,
                                         column = column_num)
            column_num = 0
            game_num += 1


        # Buttons made at the button used to manipulate the program
        self.button_frame = ttk.LabelFrame(self.games_frame)
        self.button_frame.grid(row = len(sorted_list) + 2, columnspan = 4)    
        self.add_button = ttk.Button(self.button_frame,
                                    text = "Add a new game",
                                    command = self.add_game)
        self.add_button.grid(row=1, column=0)
        self.confirm_game = ttk.Button(self.button_frame,
                                    text = "Confirm game", 
                                    command = self.collect_game)
        self.change_confirm = ttk.Button(self.button_frame, 
                                    text = "Confirm Changes", 
                                    command = self.confirm_changes)
        self.change_confirm.grid(row = 1, column = 1)
        self.find_game = ttk.Button(self.button_frame, 
                                    text = "Find what to play", 
                                    command = self.present_game)
        self.find_game.grid(row = 1, column = 2)
        self.message_str = StringVar()
        self.message_label = Label(root, textvariable = self.message_str)
        self.message_label.grid(row = 1, columnspan = 4)
    # Add in a new game
    def add_game(self):
        self.add_button.grid_forget()
        self.confirm_game.grid(row=1,column=0)
        # Create a new row for the new game in each array
        self.var_array.append([])
        self.entry_array.append([])
        for j in range(0,4):
            if j == 0:
                # If first column use a string(game name)
                self.var_array[-1].append(StringVar())
            elif j != 0:
                # If other column us a number
                self.var_array[-1].append(DoubleVar())
            # Add in the entry box
            self.entry_array[-1].append(ttk.Entry(self.games_frame,
                         textvariable = var_array[-1][j]))
        col_num = 0
        for entry in self.entry_array[-1]:
            # Place the new entries in the last row
            entry.grid(row = len(sorted_list) + 1, column = col_num)
            col_num += 1
        # Add in a delete button at the end of te row
        self.exit_array.append(Button(self.games_frame, 
                            command=lambda row=len(sorted_list): delete(row)))
        self.exit_array[-1].grid(row = len(sorted_list) + 1, column = 4)
        self.button_frame.grid(row = len(sorted_list) + 2)

    # Collect in a new game from the user
    def collect_game(self):
        # Remove the confirm button
        self.confirm_game.grid_forget()
        # Take information from the entry array and add it into a new object
        new_game = Game(self.var_array[-1][0].get(),
                        self.var_array[-1][1].get(),
                        self.var_array[-1][2].get(),
                        self.var_array[-1][3].get())
        # Add the object into the array
        self.game_list.append(new_game)
        # Sort this array to find the 'best option'
        self.game_list = sort_games(self.game_list)
        # Add the add button back
        self.add_button.grid(row=1,column=0)

    # Delete a game if user desires
    def delete(self, array_loc):
        # Remove each entry row
        for entry in self.entry_array[array_loc]:
            entry.grid_forget()
        # Remove the delete button
        self.exit_array[array_loc].grid_forget()
        # Remove this from any related tables
        self.game_list.pop(array_loc)
        self.entry_array.pop(array_loc)
        self.var_array.pop(array_loc)

    # Show the user what the program reccomends
    def present_game(self):
        # Save all the changes made to the list
        self.confirm_changes()
        new_list = sort_games(self.game_list)
        # Show the new list
        self.message_str.set("Gametable recommends: " + new_list[0].game_name)

    # Allow the user to add in new values
    def confirm_changes(self):
        game_num = 0
        # For each game, change the values using the entries
        for game in self.game_list:
            if self.var_array[game_num][3].get() <= 0:
                self.message_str.set("Please set priority above 0")
                self.entry_array[game_num][3].config(bg = '#ff5555')
                break
            if (self.var_array[game_num][1].get() 
                < self.var_array[game_num][2].get()):
                self.message_str.set(
                    "Please set total hours to be higher than played")
                self.entry_array[game_num][1].config(bg = '#ff5555')
                self.entry_array[game_num][2].config(bg = '#ff5555')
                break
            game.change_values(
            self.var_array[game_num][0].get(),
            self.var_array[game_num][1].get(),
            self.var_array[game_num][2].get(),
            self.var_array[game_num][3].get())
            game_num += 1
            self.message_str.set("Changes Saved")

if __name__ == "__main__":
    root = Tk()
    gametable_ui(root).grid(row=0,column=0)
    root.title("GameTable")
    root.mainloop()
# Save any changes
save(sorted_list)