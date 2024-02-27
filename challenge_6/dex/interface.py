import json
import csv
import xmltodict
import yaml
import os
import sys

from typing import Dict, Union, List


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
            print(f"Error: File format not supported!\n{client_usage()}")
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

    1 - HELP
    To use Help type one of the following:
    1, H, Help
    
    2 - TRIVIA
    To use Trivia type one of the following:
    2, T, Trivia

    3 - INFO
    To use Info type one of the following:
    3, I, Info

    4 - BATTLE
    To use Battle type one of the following:
    4, B, Battle
    
    5 - EXIT
    To quit type one of the following:
    5, E, Exit


    """
    return client_usage_msg


def main() -> None:
            
    if sys.argv[0] == 'interface.py':
        
        interface = ("Hello, Welcome to the Dex!" + "\n") 
        interface += ("\n"+"OPTIONS" + "\n")
        interface += ("\n" + "1 - Help" + "\n")
        interface += ("2 - Trivia" + "\n")
        interface += ("3 - Info" + "\n")
        interface += ("4 - Battle" + "\n")
        interface += ("5 - Exit" + "\n\n")
        print(interface)
        main_menu_choice = input("Please insert the chosen option: ")
        
        if main_menu_choice == "1" or main_menu_choice.lower() == "h" or main_menu_choice.lower() == "help":
            print(client_helper())
            quit()
        elif main_menu_choice not in ["1", "2", "3", "4", "5", "help", "trivia", "info", "battle", "exit", "h", "t", "i", "b", "e"]:
            print(f"WARNING: This command does not exist.\n{client_usage()}")
            quit()
            
        monster_menu = "\n"
        monster_menu += ("Which category of monster you'll choose?" + "\n")
        monster_menu += ("1 - Pokemon" + "\n")
        monster_menu += ("2 - Digimon" + "\n")
        print(monster_menu)
        monster_category = input("Choose your monster category: ")
        
        if monster_category == "1" or monster_category.lower() == "p" or monster_category.lower() == "pokemon":
            monster_category = 'pokemon'
            
        elif monster_category == "2" or monster_category.lower() == "d" or monster_category.lower() == "digimon":
            monster_category = 'digimon'
        
        else:
            print(f"WARNING: This command does not exist.\n{client_usage()}")
            quit()
            
        monster_file = input("Type the archive name:")
        
        if "pokemon" in monster_file:
            if monster_category == "digimon":
                print(f"WARNING: Different type of monsters.\n{client_usage()}")
                quit()
        elif "digimon" in monster_file:
            if monster_category == "pokemon":
                print(f"WARNING: Different type of monsters.\n{client_usage()}")
                quit()
        else:
            print(f"WARNING: Different type of monsters.\n{client_usage()}")
            quit()
        
        path = "/home/samara/Projects/dex_challenge/data"
       
        if "json" in monster_file:
            file_format = "json"
        elif "xml" in monster_file:
            file_format = "xml"
        elif "csv" in monster_file:
            file_format = "csv"
        elif "yaml" in monster_file:
            file_format = "yaml"
        else:
            print(f"Error: File format not supported!\n{client_usage()}")
            quit()
        
        monster_path = f"{path}/{monster_category}/{file_format}/{monster_file}"
        
        if os.path.exists(monster_path):
            print(monster_path)
                
        else:
            print(f"WARNING: File {monster_file} does not exist.")
            quit()

        if main_menu_choice == "2" or main_menu_choice.lower() == "t" or main_menu_choice.lower() == "trivia":

            data_arch1 = read_file(monster_path)
            print(data_arch1)
            
            for idx in data_arch1:
                print(str(idx))
            
        elif main_menu_choice == "3" or main_menu_choice.lower() == "i" or main_menu_choice.lower() == "info":
            print("teste info")
            
        elif main_menu_choice == "4" or main_menu_choice.lower() == "b" or main_menu_choice.lower() == "battle":
            print("teste battle")
            
        elif main_menu_choice == "5" or main_menu_choice.lower() == "e" or main_menu_choice.lower() == "exit":
            quit()


if __name__ == "__main__":
    main()

# class Team:
#     team_1 = []
#     team_2 = []
    
#     def add_monsters(object):
        
# class Player:     

    
    
    
    
