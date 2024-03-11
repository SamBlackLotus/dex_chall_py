import json
import csv
import xmltodict
import yaml
import os
import sys

from typing import Dict, Union, List

def read_file(filepath: str) -> List[Dict[str, Union[str, int]]]:
    """
    This function reads a file and acts according to its format
    it will fit in one of the conditionals.

    If its a .json it uses load.
    If its a .csv it uses DictReader.
    If its a .xml it uses xmltodict.
    If its a .yaml it uses safe load.

    Parameters
    ----------
    filepath:
        The file path, it can be the full path or relative path.

    Returns
    -------
    data_read:
        The file received will be returned in python data types.
    """
    with open((filepath), "r") as source_data:
        if ".json" in filepath:
            data_read = json.load(source_data)

        elif ".csv" in filepath:
            csv_file = csv.DictReader(source_data, delimiter=",")
            data_read = [row for row in csv_file]

        elif ".xml" in filepath:
            xml = source_data.read()
            xml_file = xmltodict.parse(xml)
            xml_dict = {key: value for key, value in xml_file["root"].items()}
            for key, value in xml_dict.items():
                data_read = value

        elif ".yaml" in filepath:
            yaml_file = source_data.read()
            data_read = yaml.safe_load(yaml_file)

        else:
            print(f"Error: File format not supported!\n{core.client_usage()}")
            quit()
        monster_list = []
        for key,value in enumerate(data_read):
            if "Legendary" in value:
                monster_list.append(Monster("Pokemon", value["Id"], value["Name"], "", value["Type 1"], value["Type 2"], value["Generation"], value["Legendary"], value["HP"], value["Attack"], value["Defense"], value["Speed"]))
            elif "Stage" in value:
                monster_list.append(Monster("Digimon", value["Id"], value["Name"], value["Stage"], value["Type"], "", "", "", value["HP"], value["Atk"], value["Def"], value["Spd"]))
    return monster_list


def client_helper() -> str:
    """
    This function prints the client helper in the CLI.

    Returns
    -------
    helper_msg:
        The client helper message.
    """

    helper_msg: str = """
    Hello! Welcome to the Monster Dex.

    Here you can choose between the following options, that are:

    --trivia
    --info
    --battle
    """
    return helper_msg


def client_usage() -> str:
    """
    This function prints the client usage in the CLI.

    Returns
    -------
    client_usage_msg:
        The client usage message.
    """
    client_usage_msg: str = """
    CLI usage examples:

    HELP
    > python3 dex/main.py --help


    TRIVIA
    > python3 dex/main.py --trivia ../data/pokemon/json/pokemons_1.json --id 1
    > python3 dex/main.py --trivia ../data/digimon/json/digimons_1.json --id 1

    INFO
    > python3 dex/main.py --player1 ../data/pokemon/json/pokemons_1.json
    --player2 ../data/pokemon/json/pokemons_2.json --id 1 --info
    > python3 dex/main.py --player1 ../data/digimon/json/digimons_1.json
    --player2 ../data/digimon/json/digimons_2.json --id 1 --info

    BATTLE
    > python3 dex/main.py --player1 ../data/pokemon/json/pokemons_1.json
    --player2 ../data/pokemon/json/pokemons_2.json --id 1 --battle
    > python3 dex/main.py --player1 ../data/digimon/json/digimons_1.json
    --player2 ../data/digimon/json/digimons_2.json --id 1 --battle
    

    """
    return client_usage_msg


def main() -> None:
    if len(sys.argv) == 1:
        print(client_usage())
        quit()

    id_number: int = 0

    command_1: str = sys.argv[1]
    if command_1 == "--help":
        if len(sys.argv) == 2:
            print(client_helper())
            quit()

        else:
            print(f"WARNING! Incorrect amount of arguments.\n{client_usage()}")
            quit()

    elif command_1 == "--trivia":
        if len(sys.argv) == 3:
            filepath_1 = sys.argv[2]
            if not os.path.exists(filepath_1):
                print(f"WARNING: File {filepath_1} does not exist.")
                quit()
        elif len(sys.argv) == 5:
            command_2: str = sys.argv[3]
            if command_2 == "--id":
                id_number = int(sys.argv[4])

            else:
                print(f"WARNING: This command does not exist.\n{client_usage()}")
                quit()

            filepath_1 = sys.argv[2]
            if not os.path.exists(filepath_1):
                print(f"WARNING: File {filepath_1} does not exist.")
                quit()

        else:
            print(f"WARNING! Incorrect amount of arguments.\n{client_usage()}")
            quit()

        data_arch1: Dict[str, Union[str, int]] = read_file(filepath_1)
        

        for idx in data_arch1:
            print(str(idx))


        if "pokemon" in filepath_1:

        elif "digimon" in filepath_1:


    elif command_1 == "--player1":
        if len(sys.argv) <= 5:
            print(f"WARNING! Incorrect amount of arguments.\n{client_usage()}")
            quit()

        filepath_1 = sys.argv[2]
        if not os.path.exists(filepath_1):
            print(f"WARNING: File {filepath_1} does not exist.")
            quit()

        command_2 = sys.argv[3]

        if command_2 == "--player2":
            if len(sys.argv) >= 6:
                filepath_2 = sys.argv[4]
                if not os.path.exists(filepath_2):
                    print(f"WARNING: File {filepath_2} does not exist.")
                    quit()

        else:
            print(f"WARNING: This command does not exist.\n{client_usage()}")
            quit()

        command_3 = sys.argv[5]
        command_4 = "0"
        if command_3 == "--id":
            if len(sys.argv) == 8:
                id_number = int(sys.argv[6])
                command_4 = sys.argv[7]

            else:
                print(f"WARNING! Incorrect amount of arguments.\n{client_usage()}")
                quit()

        elif command_3 != "--info" and command_3 != "--battle":
            print(f"WARNING: This command does not exist.\n{client_usage()}")
            quit()

        if "pokemon" in filepath_1:
            monster_type1 = "pokemon"
            if "pokemon" in filepath_2:
                monster_type2 = "pokemon"
            elif "digimon" in filepath_2:
                print(f"WARNING: Different type of monsters.\n{client_usage()}")
                quit()
        elif "digimon" in filepath_1:
            monster_type1 = "digimon"
            if "pokemon" in filepath_2:
                print(f"WARNING: Different type of monsters.\n{client_usage()}")
                quit()
            elif "digimon" in filepath_2:
                monster_type2 = "digimon"

        data_arch1 = read_file(filepath_1)
        data_arch2 = read_file(filepath_2)

        if command_3 == "--info" or command_4 == "--info":

        elif command_3 == "--battle" or command_4 == "--battle":
            
    else:
        print(f"WARNING: This command does not exist.\n{client_usage()}")
        quit()

if __name__ == "__main__":
    main()
    
class Monster:
    def __init__(self, category, id, name, stage, type, type2, generation, legendary, hp, attack, defense, speed):
        self.category = category
        self.id = id
        self.name = name
        self.stage = stage
        self.type = type
        self.type2 = type2
        self.generation = generation
        self.legendary = legendary
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.current_hp = hp

    def __str__(self):
        return f'{self.id} {self.name} {self.stage} {self.type} {self.type2} {self.generation} {self.legendary} {self.hp} {self.attack} {self.defense} {self.speed}'
    
    def info_self(self):
        if self.category == "Digimon":
            print("INFO CARD", "\n"
                "Id:" + str(self.id), "\n"
                "Name:" + self.name, "\n"
                "Stage:" + self.stage, "\n"
                "Type:" + self.type, "\n"
                "HP:" + str(self.hp), "\n"
                "Attack:" + str(self.attack), "\n"
                "Defense:" + str(self.defense), "\n"
                "Speed:" + str(self.speed), "\n")
        elif self.category == "Pokemon":
            print("INFO CARD", "\n"
                "Id:" + str(self.id), "\n"
                "Name:" + self.name, "\n"
                "Generation:" + str(self.generation), "\n"
                "Legendary:" + self.legendary, "\n"
                "HP:" + str(self.hp), "\n"
                "Attack:" + str(self.attack), "\n"
                "Defense:" + str(self.defense), "\n"
                "Speed:" + str(self.speed), "\n")

# class Team:
#     team_1 = []
#     team_2 = []
    
#     def add_monsters(object):
        
# class Player:     

    
    
    
    
