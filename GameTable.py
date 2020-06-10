##========= GameTable ========##
#---------- Version 0 ---------#
#::::::::::Contributers::::::::#
#         Josh Peacocke        #
#------------------------------#
#============Changes===========#
## Change date: 10/6/2020
## Change Branch: Collection
# Created basic class

#=======Dummy Variables========#

#==========Game Class==========#

class Game:
    def __init__(self, game_name, _total_hours, played_hours, priority):
        self.game_name = game_name
        self._total_hours = _total_hours
        self.played_hours = played_hours
        self.priority = priority

    def remaining_hours(self, _total_hours, played_hours):
        return(_total_hours - played_hours)
        