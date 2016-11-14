import json

class Game:
    """docstring here"""
    def __init__(self, save):
        self.save = save

    def loadGame(self):
        """docstring"""
        json_str = json.loads(open("saves.json","r").read())
        player_state_save = json_str.get(self.save)

        return player_state_save


    def saveGame(self, new_save):
        """docstring"""
        #opens entire file to read, records all file data, closes file
        read_json_file = open("saves.json","r")
        old_data = json.loads(read_json_file.read())
        read_json_file.close

        #saves over old file data
        old_data[self.save] = new_save

        #opens file to write, writes in new save data, closes file
        write_json_file = open("saves.json","w")
        json.dump(old_data, write_json_file, indent=4)
        write_json_file.close()
