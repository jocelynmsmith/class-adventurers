# *******************************************************************************************************************
# * Author: Jocelyn Smith
# * Created: February 15, 2021
# * Purpose: This program creates a class with functions that performs and returns tasks.
# ******************************************************************************************************************/
class Adventurers:
    """A class is created to represent a group of adventurers that have different
    available roles."""
    def __init__(self, barbarian):
        self.__barbarian =  barbarian
        self.__bard =  None
        self.__wizards = []

    def get_barbarian(self):
        return self.__barbarian
    def set_barbarian(self, new_barbarian):
        self.__barbarian = new_barbarian
    def get_bard(self):
        return self.__bard
    def set_bard(self, new_bard):
        self.__bard = new_bard

    def add_wizard(self, new_wizard):
        self.__wizards.append(new_wizard)

    def kill_all_wizards(self):
        self.__wizards = []

    def get_wizards(self):
        """When called, a new temp list is created. A for-loop iterates through all of the wizards
        and appends the index value into the duplicate list. The new list is returned."""
        temp = []
        for player in self.__wizards:
            temp.append(player)
        return temp

    def fight_goblins(self):
        if self.__bard is not None:
            print("Here comes the healing!")

        for i in self.__wizards:
                print("Fireball!")

