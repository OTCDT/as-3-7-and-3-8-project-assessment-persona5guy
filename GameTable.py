##========= GameTable ========##
#---------- Version 1 ---------#
#::::::::::Contributers::::::::#
#         Josh Peacocke        #
#------------------------------#
#============Changes===========#
"""
 Change date: 10/8/2020
 Change Branch: GUI-rework
 GUI structure to be changed into standard
 object oriented design
 """

#============Imports===========#
import pickle as pkl
# pickle rick lmao
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


#===========Functions==========# 

def boolean_input(user_input):
    while True:
        message = input(user_input)
            # This will transform a string input into a true or false
            # haha funny number line
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
    with open("resources/game.dat", "wb") as output:
        pkl.dump(object_array, output)
def load():
    # Load game into the file
    try:
        with open("resources/game.dat", "rb") as input:
         return pkl.load(input)
    except FileNotFoundError:
        return []
#============GUI===============#

#-------GUI functions----------#
class gametable_ui(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        # Call in the main game list, make a frame, and image for the
        # size of the delete button
        self.game_list = sort_games(load())
        self.games_frame = LabelFrame(root)
        self.games_frame.grid(row=0,column=0)
        self.size_image = PhotoImage(width=10,height=10,
                                    file = "resources\delete.gif")
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
        # Created labels, to look like:
        # Game Name | Total Hours | Played Hours | Priority

        # Buttons made at the button used to manipulate the program
        self.button_frame = ttk.LabelFrame(self.games_frame)
        self.button_frame.grid(row = len(self.game_list) + 2, columnspan = 4)    
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
        self.save_close_button = ttk.Button(self.button_frame,
                                    text = "Save and Close",
                                    command = self.save_close)
        self.save_close_button.grid(row=1,column = 3)
        self.message_str = StringVar()
        self.message_label = Label(root, textvariable = self.message_str)
        self.message_label.grid(row = 1, columnspan = 4)

        # Create a table of each data
        self.table_make()

        # Save after all data is loaded
        save(self.game_list)

    def table_make(self):
        #Table Creation
        column_num = 0
        # Make sure the length of the list is larger than one
        if len(self.game_list) > 0:
            # Make a list that corresponds to the tables for both
            # entry labels and variables in the entry
            self.var_array = []
            self.entry_array = []
            # Create a row for each game in the list
            for i in range(0,len(self.game_list)):
                self.var_array.append([])
                self.entry_array.append([])
            # Create a column for each data entry
                for j in range(0,4):
                    # If it is in the first row,
                    # use string var for a name
                    if j == 0:
                        self.var_array[i].append(StringVar())
                    # If not, use double var for numbers
                    elif j != 0:
                        self.var_array[i].append(DoubleVar())
                    # Create an entry into a table
                    # with specific coordinates (i,j)
                    self.entry_array[i].append(Entry(self.games_frame,
                     textvariable = self.var_array[i][j]))
                # Intended result: variable list = [String, Num, Num, Num]
                #                  entry = [entry, entry, entry, entry]
                # Repeated rows for each game added
        # If not, then make empty arrays to be appended to
        else:
            self.var_array = []
            self.entry_array = []
            self.message_str.set("Add a game using the [Add Game] Button")
        game_num = 0
        # Placement of each section of data
        # Repeat for each game as a row
        for game in self.var_array:
            # Set all shown variables to the variable array
            game[0].set(self.game_list[game_num].game_name)
            game[1].set(self.game_list[game_num]._total_hours)
            game[2].set(self.game_list[game_num].played_hours)
            game[3].set(self.game_list[game_num].priority)
            # Intended Result:
            # variables = [game name,total hours, played hours, priority]
            # Repeated row for each game
            for entry in game:
                #Place the grid into it's correct place long the row
                self.entry_array[game_num][column_num].grid(
                                    row = game_num + 1, column = column_num)
                column_num += 1
            # Create and grid a delete button
            column_num = 0
            game_num += 1
        self.delete_button()
    # Add in a new game
    def delete_button(self):
        self.exit_array = []
        for row_num in range(0,len(self.game_list)):
            # Create and grid a delete button
            self.exit_array.append(Button(self.games_frame, 
                            image = self.size_image, bg = '#ff8888',
                            command=lambda row=row_num: self.delete(row)))
            # Add delete button to end of row
            self.exit_array[row_num].grid(row = row_num + 1,
                                          column = 4)
        
    def add_game(self):
        # Remove the add button, load confirm button in place
        self.add_button.grid_forget()
        self.confirm_game.grid(row=1,column=0)
        # Create a new row for the new game in each array
        self.var_array.append([])
        self.entry_array.append([])
        # Repeated process from table making, adding to the 
        # end of the arrays
        for j in range(0,4):
            if j == 0:
                # If first column use a string (game name)
                self.var_array[-1].append(StringVar())
            elif j != 0:
                # If other column use a number
                self.var_array[-1].append(DoubleVar())
            # Add in the entry box
            self.entry_array[-1].append(Entry(self.games_frame,
                         textvariable = self.var_array[-1][j]))
        col_num = 0
        for entry in self.entry_array[-1]:
            # Place the new entries in the last row
            entry.grid(row = len(self.game_list) + 1, column = col_num)
            col_num += 1
        # Add in a delete button at the end of the row
        self.exit_array.append(Button(self.games_frame, image = self.size_image,
        bg = '#ff8888', command=lambda row=len(self.game_list): self.delete(row)))
        self.exit_array[-1].grid(row = len(self.game_list) + 1, column = 4)
        self.button_frame.grid(row = len(self.game_list) + 2)
        if self.error():
            return
        save(self.game_list)

    # Collect in a new game from the user
    def collect_game(self):
        if self.error():
            return
        # Remove confirm button
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
        save(self.game_list)

    # Delete a game if user desires
    def delete(self, array_loc):
        # Remove each entry row
        for entry in self.entry_array[array_loc]:
            entry.destroy()
        # Remove the delete button array
        for button in self.exit_array:
            button.destroy()
        self.exit_array.clear()
        # Remove this from any related tables
        self.game_list.pop(array_loc)
        self.entry_array.pop(array_loc)
        self.var_array.pop(array_loc)
        # Reconstruct the delete buttons
        self.delete_button()
        if self.error():
            return
        save(self.game_list)



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
        if self.error():
            return
        # For each game, change the values using the entries
        for game in self.game_list:
            game.change_values(
            self.var_array[game_num][0].get(),
            self.var_array[game_num][1].get(),
            self.var_array[game_num][2].get(),
            self.var_array[game_num][3].get())
            game_num += 1
            # Feedback to user that values have been saved
            self.message_str.set("Changes Saved")
            save(self.game_list)

    def save_close(self):
        if self.error():
            return
        save(self.game_list)
        root.destroy()

    def error(self):
        for game_num in range(0,len(self.game_list)):
            # Error Handling
            # If the user set the priority to be 0 or lower
            # Present error
            for i in range(0,3):
                if self.var_array[game_num][i].get() == "":
                    self.message_str.set("Please enter a value in the cell")
                    self.entry_array[game_num][i].config(bg = "#ff5555")
                    return True
                self.entry_array[game_num][i].config(bg = "#ffffff")
            
            if self.var_array[game_num][3].get() <= 0:
                self.message_str.set("Please set priority above 0")
                self.entry_array[game_num][3].config(bg = '#ff5555')
                return True
            # If the user has made the played hours greater than total
            # then present error
            if (self.var_array[game_num][1].get() 
                < self.var_array[game_num][2].get()):
                self.message_str.set(
                    "Please set total hours to be higher than played")
                self.entry_array[game_num][1].config(bg = '#ff5555')
                self.entry_array[game_num][2].config(bg = '#ff5555')
                return True
            elif (self.var_array[game_num][1].get()
                 == self.var_array[game_num][2].get()):
                self.message_str.set(
                    "The total hours is equal to played," +
                    " delete or change this")
                self.entry_array[game_num][1].config(bg = '#ff5555')
                self.entry_array[game_num][2].config(bg = '#ff5555')
                return True
            
                

if __name__ == "__main__":
    root = Tk()
    gametable_ui(root).grid(row=0,column=0)
    root.title("GameTable")
    root.mainloop()