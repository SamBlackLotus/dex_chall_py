import json
import csv
import xmltodict
import yaml
import os
import sys

from datetime import datetime
from typing import Dict, Union, List

id_number = 0


class Monster:
    def __init__(self, category, id, name, stage, type, type2, generation, legendary, hp, attack, defense, speed, cur_hp):
        self.category = category
        self.monster_id = id
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
        self.current_hp = cur_hp

    def __str__(self):
        return f'{self.monster_id} {self.name} {self.stage} {self.type} {self.type2} \
        {self.generation} {self.legendary} {self.hp} {self.attack} {self.defense} {self.speed}'

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


class TeamMonster(Monster):
    def __init__(self, category, id, name, stage, type, type2, generation, legendary, hp, attack, 
                defense, speed, cur_hp, team_id, team_name):
        super().__init__(category, id, name, stage, type, type2, generation, legendary, hp, attack,
                         defense, speed, cur_hp)
        self.team_id = team_id
        self.team_name = team_name


class Player(TeamMonster):
    def __init__(self, category, id, name, stage, type, type2, generation, legendary, hp, attack,
                 defense, speed, cur_hp, team_id, team_name, player_id, player_name):
        super().__init__(category, id, name, stage, type, type2, generation, legendary, hp, attack,
                         defense, speed, cur_hp, team_id, team_name)
        self.player_id = player_id
        self.player_name = player_name


class Trivia():
    monster_list = {}
    monster_sum = "0"
    highest_hp_monster = {}
    highest_atk_monster = {}
    lowest_atk_monster = {}
    highest_def_monster = {}
    highest_spd_monster = {}
# é possível usar o stage list como um dict, para somar quantas chaves tem e no valor da chave ter quantos digimons tem em cada
    training_dict = []
    baby_dict = []
    rookie_dict = []
    champion_dict = []
    ultimate_dict = []
    mega_dict = []
    ultra_dict = []
    armor_dict = []
    none_dict = []
    data_dict = []
    vaccine_dict = []
    virus_dict = []
    free_dict = []
    baby_digimon = 0
    rookie_digimon = 0
    champion_digimon = 0
    ultimate_digimon = 0
    mega_digimon = 0
    ultra_digimon = 0
    data_type = 0
    vaccine_type = 0
    virus_type = 0
    free_type = 0
    training_strongest = {}
    baby_strongest = {}
    rookie_strongest = {}
    champion_strongest = {}
    ultimate_strongest = {}
    mega_strongest = {}
    ultra_strongest = {}
    armor_strongest = {}
    none_strongest = {}
    data_strongest = {}
    vaccine_strongest = {}
    virus_strongest = {}
    free_strongest = {}
    digimon_types = []
    digimon_stages = []

    def get_hp(self):

        return int(self.hp)

    def get_atk(self):

        return int(self.attack)

    def get_def(self):

        return int(self.defense)

    def get_spd(self):

        return int(self.speed)

    def show_pokemon_trivia() -> None:
        """
        This function will print a message in the CLI.

        Parameters
        ----------
        pokemons_info:
            Bring the treated variables which will be used to answer
            the questions

        id_number:
            The id provided by the user, in case its not provided
            it will be filled with 0.

        """
        break_line: str = (" " * 80) + "\n"

        datenow = datetime.now()
        msg = break_line
        msg += "reported generated on: " + datenow.isoformat() + (" " * 31) + "\n"
        msg += break_line
        msg += ("=" * 29) + " Welcome to the Dex! " + ("=" * 30) + "\n"
        msg += break_line
        msg += "Here we have some useful information gathered from the list you provided us:    \n"
        msg += break_line
        msg += "1. How many pokemons there is in this list:" + (" " * 37) + "\n"
        msg += (
            (" " * 4)
            + "> "
            + Trivia.monster_sum
            + " pokemons"
            + (" " * (25 - len(Trivia.monster_sum)))
            + "\n"
        )
        msg += break_line
        msg += "2. The pokemon with the highest HP point is:" + (" " * 36) + "\n"
        msg += (
            (" " * 4)
            + "> "
            + Trivia.highest_hp_monster.name
            + " with "
            + str(Trivia.highest_hp_monster.hp)
            + " HP points"
            + (
                " "
                * (
                    (59 - len(Trivia.highest_hp_monster.name))
                    - len(str(Trivia.highest_hp_monster.hp))
                )
            )
            + "\n"
        )
        msg += break_line
        msg += "3. Which one has the strongest attack:" + (" " * 42) + "\n"
        msg += (
            (" " * 4)
            + "> "
            + Trivia.highest_atk_monster.name
            + " with "
            + str(Trivia.highest_atk_monster.attack)
            + " attack points."
            + (
                " "
                * (
                    (54 - len(Trivia.highest_atk_monster.name))
                    - len(str(Trivia.highest_atk_monster.attack))
                )
            )
            + "\n"
        )
        msg += break_line
        msg += "4. Which one has the strongest defense:" + (" " * 41) + "\n"
        msg += (
            (" " * 4)
            + "> "
            + Trivia.highest_def_monster.name
            + " with "
            + str(Trivia.highest_def_monster.defense)
            + " defense points."
            + (
                " "
                * (
                    (53 - len(Trivia.highest_def_monster.name))
                    - len(str(Trivia.highest_def_monster.defense))
                )
            )
            + "\n"
        )
        msg += break_line
        msg += "5. Which one is the fastest:" + (" " * 52) + "\n"
        msg += (
            (" " * 4)
            + "> "
            + Trivia.highest_spd_monster.name
            + " with "
            + str(Trivia.highest_spd_monster.speed)
            + " speed points."
            + (
                " "
                * (
                    (55 - len(Trivia.highest_spd_monster.name))
                    - len(str(Trivia.highest_spd_monster.speed))
                )
            )
            + "\n"
        )
        msg += break_line
        msg += "Thanks for using this Dex!" + (" " * 50) + "\n"
        msg += break_line
        msg += break_line
        msg += break_line

        print(msg)

        id_number = input("Type the ID of the file to be saved: ")

        data_saver(msg, "pokemon-trivia", id_number)

    def show_digimon_trivia() -> None:
        """
        This function will print a message about in the CLI.

        Parameters
        ----------
        digimon_info:
            Bring the treated variables which will be used to answer
            the questions

        id_number:
            The id provided by the user, in case its not provided
            it will be filled with 0.

        """
        break_line: str = (" " * 80) + "\n"

        datenow = datetime.now()
        msg = break_line
        msg += "reported generated on: " + datenow.isoformat() + (" " * 31) + "\n"
        msg += break_line
        msg += ("=" * 29) + " Welcome to the Dex! " + ("=" * 30) + "\n"
        msg += break_line
        msg += "Here we have some useful information gathered from the list you provided us:    \n"
        msg += break_line
        msg += "1. How many Digimon there is in this list:" + (" " * 37) + "\n"
        msg += (
            (" " * 4)
            + "> "
            + Trivia.monster_sum
            + " digimon"
            + (" " * (25 - len(Trivia.monster_sum)))
            + "\n"
        )
        msg += break_line
        msg += "2. How many different stages a digimon have?" + (" " * 36) + "\n"
        msg += (
            (" " * 4)
            + "> In this list we have "
            + str(len(Trivia.digimon_stages))
            + " stages of digimon, they're "
            + " ".join(Trivia.digimon_stages)
            + "\n"
        )
        msg += break_line
        msg += "3. How many digimon in each stage there are?" + (" " * 36) + "\n"
        msg += (
            (" " * 4)
            + "> "
            + "In-Training: "
            + str(len(Trivia.training_dict))
            + " digimon"
            + (" " * (53 - len(Trivia.training_dict)))
            + "\n"
        )
        msg += (
            (" " * 4)
            + "> "
            + "Baby: "
            + str(len(Trivia.baby_dict))
            + " digimon"
            + (" " * (60 - len(Trivia.baby_dict)))
            + "\n"
        )
        msg += (
            (" " * 4)
            + "> "
            + "Rookie: "
            + str(len(Trivia.rookie_dict))
            + " digimon"
            + (" " * (60 - len(Trivia.rookie_dict)))
            + "\n"
        )
        msg += (
            (" " * 4)
            + "> "
            + "Champion: "
            + str(len(Trivia.champion_dict))
            + " digimon"
            + (" " * (60 - len(Trivia.champion_dict)))
            + "\n"
        )
        msg += (
            (" " * 4)
            + "> "
            + "Ultimate: "
            + str(len(Trivia.ultimate_dict))
            + " digimon"
            + (" " * (60 - len(Trivia.ultimate_dict)))
            + "\n"
        )
        msg += (
            (" " * 4)
            + "> "
            + "Mega: "
            + str(len(Trivia.mega_dict))
            + " digimon"
            + (" " * (60 - len(Trivia.mega_dict)))
            + "\n"
        )
        msg += (
            (" " * 4)
            + "> "
            + "Ultra: "
            + str(len(Trivia.ultra_dict))
            + " digimon"
            + (" " * (60 - len(Trivia.ultra_dict)))
            + "\n"
        )
        msg += (
            (" " * 4)
            + "> "
            + "Armor: "
            + str(len(Trivia.armor_dict))
            + " digimon"
            + (" " * (60 - len(Trivia.armor_dict)))
            + "\n"
        )
        msg += (
            (" " * 4)
            + "> "
            + "None: "
            + str(len(Trivia.none_dict))
            + " digimon"
            + (" " * (60 - len(Trivia.none_dict)))
            + "\n"
        )
        msg += break_line
        msg += (
            "4. The strongest digimon in each stage based on the Atk attribute is:"
            + (" " * 11)
            + "\n"
        )
        msg += (
            (" " * 4)
            + "> "
            + "In-Training: "
            + Trivia.training_strongest.name
            + ", "
            + str(Trivia.training_strongest.attack)
            + (
                " "
                * (
                    65
                    - len(Trivia.training_strongest.name)
                    - len(str(Trivia.training_strongest.attack))
                )
            )
            + "\n"
        )
        msg += (
            (" " * 4)
            + "> "
            + "Baby: "
            + Trivia.baby_strongest.name
            + ", "
            + str(Trivia.baby_strongest.attack)
            + (
                " "
                * (
                    65
                    - len(Trivia.baby_strongest.name)
                    - len(str(Trivia.baby_strongest.attack))
                )
            )
            + "\n"
        )
        msg += (
            (" " * 4)
            + "> "
            + "Rookie: "
            + Trivia.rookie_strongest.name
            + ", "
            + str(Trivia.rookie_strongest.attack)
            + (
                " "
                * (
                    63
                    - len(Trivia.rookie_strongest.name)
                    - len(str(Trivia.rookie_strongest.attack))
                )
            )
            + "\n"
        )
        msg += (
            (" " * 4)
            + "> "
            + "Champion: "
            + Trivia.champion_strongest.name
            + ", "
            + str(Trivia.champion_strongest.attack)
            + (
                " "
                * (
                    61
                    - len(Trivia.champion_strongest.name)
                    - len(str(Trivia.champion_strongest.attack))
                )
            )
            + "\n"
        )
        msg += (
            (" " * 4)
            + "> "
            + "Ultimate: "
            + Trivia.ultimate_strongest.name
            + ", "
            + str(Trivia.ultimate_strongest.attack)
            + (
                " "
                * (
                    61
                    - len(Trivia.ultimate_strongest.name)
                    - len(str(Trivia.ultimate_strongest.attack))
                )
            )
            + "\n"
        )
        msg += (
            (" " * 4)
            + "> "
            + "Mega: "
            + Trivia.mega_strongest.name
            + ", "
            + str(Trivia.mega_strongest.attack)
            + (
                " "
                * (
                    63
                    - len(Trivia.mega_strongest.name)
                    - len(str(Trivia.mega_strongest.attack))
                )
            )
            + "\n"
        )
        msg += (
            (" " * 4)
            + "> "
            + "Ultra: "
            + Trivia.ultra_strongest.name
            + ", "
            + str(Trivia.ultra_strongest.attack)
            + (
                " "
                * (
                    64
                    - len(Trivia.ultra_strongest.name)
                    - len(str(Trivia.ultra_strongest.attack))
                )
            )
            + "\n"
        )
        msg += (
            (" " * 4)
            + "> "
            + "Armor: "
            + Trivia.armor_strongest.name
            + ", "
            + str(Trivia.armor_strongest.attack)
            + (
                " "
                * (
                    64
                    - len(Trivia.armor_strongest.name)
                    - len(str(Trivia.armor_strongest.attack))
                )
            )
            + "\n"
        )
        msg += (
            (" " * 4)
            + "> "
            + "None: "
            + Trivia.none_strongest.name
            + ", "
            + str(Trivia.none_strongest.attack)
            + (
                " "
                * (
                    65
                    - len(Trivia.none_strongest.name)
                    - len(str(Trivia.none_strongest.attack))
                )
            )
            + "\n"
        )
        msg += break_line
        msg += "5. How many different types of digimon there is?" + (" " * 32) + "\n"
        msg += (
            (" " * 4)
            + "> In this list we have "
            + str(len(Trivia.digimon_types))
            + " types of digimon, they're "
            + " ".join(Trivia.digimon_types)
            + "\n"
        )
        msg += break_line
        msg += "6. How many digimon in each type there is:" + (" " * 38) + "\n"
        msg += (
            (" " * 4)
            + "> "
            + "Data: "
            + str(len(Trivia.data_dict))
            + (" " * (68 - len(str(Trivia.data_dict))))
            + "\n"
        )
        msg += (
            (" " * 4)
            + "> "
            + "Vaccine: "
            + str(len(Trivia.vaccine_dict))
            + (" " * (65 - len(str(Trivia.vaccine_dict))))
            + "\n"
        )
        msg += (
            (" " * 4)
            + "> "
            + "Virus: "
            + str(len(Trivia.virus_dict))
            + (" " * (67 - len(str(Trivia.virus_dict))))
            + "\n"
        )
        msg += (
            (" " * 4)
            + "> "
            + "Free: "
            + str(len(Trivia.free_dict))
            + (" " * (68 - len(str(Trivia.free_dict))))
            + "\n"
        )
        msg += break_line
        msg += (
            "7. The strongest digimon in each type based on the Atk attribute is:"
            + (" " * 11)
            + "\n"
        )
        msg += (
            (" " * 4)
            + "> "
            + "Data: "
            + Trivia.data_strongest.name
            + ", "
            + str(Trivia.data_strongest.attack)
            + (
                " "
                * (
                    65
                    - len(Trivia.data_strongest.name)
                    - len(str(Trivia.data_strongest.attack))
                )
            )
            + "\n"
        )
        msg += (
            (" " * 4)
            + "> "
            + "Vaccine: "
            + Trivia.vaccine_strongest.name
            + ", "
            + str(Trivia.vaccine_strongest.attack)
            + (
                " "
                * (
                    63
                    - len(Trivia.vaccine_strongest.name)
                    - len(str(Trivia.vaccine_strongest.attack))
                )
            )
            + "\n"
        )
        msg += (
            (" " * 4)
            + "> "
            + "Virus: "
            + Trivia.virus_strongest.name
            + ", "
            + str(Trivia.virus_strongest.attack)
            + (
                " "
                * (
                    61
                    - len(Trivia.virus_strongest.name)
                    - len(str(Trivia.virus_strongest.attack))
                )
            )
            + "\n"
        )
        msg += (
            (" " * 4)
            + "> "
            + "Free: "
            + Trivia.free_strongest.name
            + ", "
            + str(Trivia.free_strongest.attack)
            + (
                " "
                * (
                    61
                    - len(Trivia.free_strongest.name)
                    - len(str(Trivia.free_strongest.attack))
                )
            )
            + "\n"
        )
        msg += break_line
        msg += (
            "8. Which is the weakest digimon of all, based on the Atk attribute is:"
            + (" " * 10)
            + "\n"
        )
        msg += (
            (" " * 4)
            + "> "
            + Trivia.lowest_atk_monster.name
            + ", on "
            + Trivia.lowest_atk_monster.stage
            + " stage, "
            + Trivia.lowest_atk_monster.type
            + " type."
            + "\n"
        )
        msg += break_line
        msg += (
            "9. Which is the strongest digimon of all, based on the Atk attribute is:"
            + (" " * 8)
            + "\n"
        )
        msg += (
            (" " * 4)
            + "> "
            + Trivia.highest_atk_monster.name
            + ", on "
            + Trivia.highest_atk_monster.stage
            + " stage, "
            + Trivia.highest_atk_monster.type
            + " type."
            + "\n"
        )
        msg += break_line
        msg += "Thanks for using this Dex!" + (" " * 50) + "\n"
        msg += break_line
        msg += break_line
        msg += break_line

        print(msg)

        id_number = input("Type the ID of the file to be saved: ")

        data_saver(msg, "pokemon-trivia", id_number)


def data_saver(
    data_to_be_saved: str,
    monster_type: str,
    id_number: str,
) -> None:
    """
    This function creates a .txt file that stores the generated
    information.

    Parameters
    ----------
    saved_data:
        The information generated by one of the given commands.

    archive_type:
        The command selected by the user that will compose the
        file name and specify what kind it is.

    id_number:
        The id provided by the user, in case its not provided
        it will be filled with 0.

    """
    if id_number == '':
        id_number = 0

    if os.path.exists(f"{id_number}_{monster_type}.txt"):
        user_choice: str = input(
            f"File {id_number}_{monster_type}.txt already exists, "
            + "what do you prefer to do? [append|OVERWRITE] : "
        )

        if (
            user_choice.lower() == "o"
            or user_choice.lower() == "overwrite"
            or user_choice == ""
        ):
            os.remove(f"{id_number}_{monster_type}.txt")

            print("File Overwritten successfully!")

            with open(f"{id_number}_{monster_type}.txt", "w") as target:
                target.write(data_to_be_saved)

        elif user_choice.lower() == "a" or user_choice.lower() == "append":
            with open(f"{id_number}_{monster_type}.txt", "a") as target:
                target.write(data_to_be_saved)
                print("New entry added to the file successfully!")
        else:
            print(user_choice)
            print(f"WARNING: Invalid Input.\n{client_usage()}")
            quit()

    else:
        with open(f"{id_number}_{monster_type}.txt", "w") as target:
            target.write(data_to_be_saved)


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
        data_read = []

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
                data_read += [
                    {key_list: value_list for key_list, value_list in value.items()}
                ]

        elif ".yaml" in filepath:
            yaml_file = source_data.read()
            data_read = yaml.safe_load(yaml_file)

        else:
            print(f"Error: File format not supported!\n{client_usage()}")
            quit()

        monster_list = []
        if ".xml" in filepath:
            for key,value in enumerate(data_read):
                if "Legendary" in value:
                    monster_list.append(Monster("Pokemon", value["Id"],value["Name"],
                    "", value["Type1"], value["Type2"],value["Generation"], value["Legendary"],
                    value["HP"], value["Attack"], value["Defense"], value["Speed"], value["HP"]))
                elif "Stage" in value:
                    monster_list.append(Monster("Digimon", value["Id"], value["Name"],
                    value["Stage"], value["Type"], "", "", "",
                    value["HP"], value["Atk"],value["Def"], value["Spd"], value["HP"]))
        else:
            for key,value in enumerate(data_read):
                if "Legendary" in value:
                    monster_list.append(Monster("Pokemon", value["Id"], value["Name"],
                    "", value["Type 1"], value["Type 2"], value["Generation"], value["Legendary"],
                    value["HP"], value["Attack"], value["Defense"], value["Speed"], value["HP"]))
                elif "Stage" in value:
                    monster_list.append(Monster("Digimon", value["Id"], value["Name"],
                    value["Stage"], value["Type"], "", "", "",
                    value["HP"], value["Atk"], value["Def"], value["Spd"], value["HP"]))
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
        elif main_menu_choice not in ["1", "2", "3", "4", "5", "help", "trivia", "info", "battle",
                                     "exit", "h", "t", "i", "b", "e"]:
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
            pass

        else:
            print(f"WARNING: File {monster_file} does not exist.")
            quit()

        if main_menu_choice == "2" or main_menu_choice.lower() == "t" or main_menu_choice.lower() == "trivia":

            if "pokemon" in monster_file:

                data_arch1 = read_file(monster_path)

                Trivia.monster_sum = str(len(data_arch1))
                monster_order = sorted(data_arch1, key=Trivia.get_hp, reverse=True)
                Trivia.highest_hp_monster = monster_order[0]
                monster_order = sorted(data_arch1, key=Trivia.get_atk, reverse=True)
                Trivia.highest_atk_monster = monster_order[0]
                monster_order = sorted(data_arch1, key=Trivia.get_def, reverse=True)
                Trivia.highest_def_monster = monster_order[0]
                monster_order = sorted(data_arch1, key=Trivia.get_spd, reverse=True)
                Trivia.highest_spd_monster = monster_order[0]

                Trivia.show_pokemon_trivia()

            elif "digimon" in monster_file:

                data_arch1 = read_file(monster_path)

                Trivia.monster_sum = str(len(data_arch1))
                monster_order = sorted(data_arch1, key=Trivia.get_atk, reverse=True)
                Trivia.highest_atk_monster = monster_order[0]
                monster_order = sorted(data_arch1, key=Trivia.get_atk)
                Trivia.lowest_atk_monster = monster_order[0]
                monster_order = sorted(data_arch1, key=Trivia.get_def, reverse=True)

                for idx in data_arch1:
                    if idx.stage not in Trivia.digimon_stages:
                        Trivia.digimon_stages.append(idx.stage)
                        
                    if idx.type not in Trivia.digimon_types:
                        Trivia.digimon_types.append(idx.type)

                    if idx.stage == "In-Training":
                        Trivia.training_dict.append(idx)
                    elif idx.stage == "Baby":
                        Trivia.baby_dict.append(idx)
                    elif idx.stage == "Rookie":
                        Trivia.rookie_dict.append(idx)
                    elif idx.stage == "Champion":
                        Trivia.champion_dict.append(idx)
                    elif idx.stage == "Ultimate":
                        Trivia.ultimate_dict.append(idx)
                    elif idx.stage == "Mega":
                        Trivia.mega_dict.append(idx)
                    elif idx.stage == "Ultra":
                        Trivia.ultra_dict.append(idx)
                    elif idx.stage == "Armor":
                        Trivia.armor_dict.append(idx)
                    elif idx.stage == "None":
                        Trivia.none_dict.append(idx)
                        
                    if idx.type == "Data":
                        Trivia.data_dict.append(idx)
                    elif idx.type == "Vaccine":
                        Trivia.vaccine_dict.append(idx)
                    elif idx.type == "Virus":
                        Trivia.virus_dict.append(idx)
                    elif idx.type == "Free":
                        Trivia.free_dict.append(idx)

                monster_order = sorted(Trivia.training_dict, key=Trivia.get_atk, reverse=True)
                Trivia.training_strongest = monster_order[0]
                monster_order = sorted(Trivia.baby_dict, key=Trivia.get_atk, reverse=True)
                Trivia.baby_strongest = monster_order[0]
                monster_order = sorted(Trivia.rookie_dict, key=Trivia.get_atk, reverse=True)
                Trivia.rookie_strongest = monster_order[0]
                monster_order = sorted(Trivia.champion_dict, key=Trivia.get_atk, reverse=True)
                Trivia.champion_strongest = monster_order[0]
                monster_order = sorted(Trivia.ultimate_dict, key=Trivia.get_atk, reverse=True)
                Trivia.ultimate_strongest = monster_order[0]
                monster_order = sorted(Trivia.mega_dict, key=Trivia.get_atk, reverse=True)
                Trivia.mega_strongest = monster_order[0]
                monster_order = sorted(Trivia.ultra_dict, key=Trivia.get_atk, reverse=True)
                Trivia.ultra_strongest = monster_order[0]
                monster_order = sorted(Trivia.armor_dict, key=Trivia.get_atk, reverse=True)
                Trivia.armor_strongest = monster_order[0]
                monster_order = sorted(Trivia.none_dict, key=Trivia.get_atk, reverse=True)
                Trivia.none_strongest = monster_order[0]
                
                monster_order = sorted(Trivia.data_dict, key=Trivia.get_atk, reverse=True)
                Trivia.data_strongest = monster_order[0]
                monster_order = sorted(Trivia.vaccine_dict, key=Trivia.get_atk, reverse=True)
                Trivia.vaccine_strongest = monster_order[0]
                monster_order = sorted(Trivia.virus_dict, key=Trivia.get_atk, reverse=True)
                Trivia.virus_strongest = monster_order[0]
                monster_order = sorted(Trivia.free_dict, key=Trivia.get_atk, reverse=True)
                Trivia.free_strongest = monster_order[0]

                Trivia.show_digimon_trivia()

        elif main_menu_choice == "3" or main_menu_choice.lower() == "i" or main_menu_choice.lower() == "info":
            print("test info")

        elif main_menu_choice == "4" or main_menu_choice.lower() == "b" or main_menu_choice.lower() == "battle":
            print("test battle")

        elif main_menu_choice == "5" or main_menu_choice.lower() == "e" or main_menu_choice.lower() == "exit":
            quit()


if __name__ == "__main__":
    main()
