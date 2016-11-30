import json
import house
import pygame

pygame.init()
clock = pygame.time.Clock()



class Game:
    """
    docstring
    """
    def __init__(self, save):
        self.save = save

    def loadGame(self):
        """
        Parameters: self (the objects name)
        Function: loads data from the saves.json file and returns that data
        """
        json_dict = json.loads(open("saves.json","r").read())
        if(self.save == 'all'):
            player_state_save = list(json_dict.keys())

        else:
            player_state_save = json_dict.get(self.save)
            player_state_save = {self.save : player_state_save}

        return player_state_save


    def saveGame(self, new_save):
        """
        Parameters: self (the objects name), new_save (the game data that you want to save)
        Function: Saves the new data to the saves.json without deleating other saves and overwrites the save of the same name if found
        """
        read_json_file = open("saves.json","r")
        old_data = json.loads(read_json_file.read())
        read_json_file.close

        old_data[self.save] = new_save

        write_json_file = open("saves.json","w")
        json.dump(old_data, write_json_file, indent=4)
        write_json_file.close()

    def upgrade(self, improvement):
        """
        docstrings
        """
        save_dict = self.loadGame()
        info = save_dict.get(self)
        value = info.get(improvement) + 1 #this needs to be fixed
        self.saveGame(info)

    def housePositions(self):
        """
        Parameters: self (the objects name)
        Function: Opens the level_data.json file and returns the values of the houses as a list
        """
        houses = self.loadGame()
        json_dict = json.loads(open("level_data.json","r").read())
        houses = json_dict.get("level_" + str(houses.get("level")))
        house_list = []
        for i in houses:
            single_house = houses.get(i)
            single_house = house.House(single_house.get('x'), single_house.get('y'), single_house.get('player_pop'), single_house.get('player_control'), single_house.get('connections'))
            house_list.append(single_house)
        return house_list
