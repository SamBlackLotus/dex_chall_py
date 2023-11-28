import os
import sys
import json
from enum import Enum
from typing import Dict, Union, List, TypedDict, Optional

class YesNo(str, Enum):
    YES = "Yes"
    NO = "No"


class Answers(TypedDict):
    total: int
    highest_pokemon_name: str
    highest_pokemon_value: int
    heaviest_pokemon_name: str
    heaviest_pokemon_value: int
    more_experience_pokemon_name: str
    more_experience_pokemon_value: int
    total_alolas: int
    final_question: YesNo
    smallest_pokemon_name: str
    smallest_pokemon_value: int


def read_file(filepath):
    with open((filepath), "r") as source_pokedex:
        return json.load(source_pokedex)
    

def cast_to_int(value):
    return int(value) if value is not None else 0


def process_pokemons(pokemons_data):
    highest = {"index": 0, "value": 0}
    smallest = {"index": 0, "value": 0}
    heaviest = {"index": 0, "value": 0}
    lightest = {"index": 0, "value": 0}
    more_experience = {"index": 0, "value": 0}
    total_alolas = 0
    snorlax_height = 0
    charizard_height = 0

    for index, pokemon in enumerate(pokemons_data):
        height_int = cast_to_int(pokemon["height"])
        if height_int > highest["value"]:
            highest["index"] = index
            highest["value"] = height_int
            
        if height_int < smallest["value"] or smallest["value"] <= 0:
            smallest["index"] = index
            smallest["value"] = height_int    

        weight_int = cast_to_int(pokemon["weight"])
        if weight_int > heaviest["value"]:
            heaviest["index"] = index
            heaviest["value"] = weight_int
        
        if weight_int < lightest["value"] or lightest["value"] <= 0:
            lightest["index"] = index
            lightest["value"] = weight_int   
            
        base_experience_int = cast_to_int(pokemon["base_experience"])
        if base_experience_int > more_experience["value"]:
            more_experience["index"] = index
            more_experience["value"] = base_experience_int
        
        if "alola" in pokemon["name"]:
            total_alolas += 1
        
        if pokemon["name"] == "snorlax":
            snorlax_height = pokemon["height"]
        
        if pokemon["name"] == "charizard":
            charizard_height = pokemon["height"]

    return Answers(
        total=len(pokemons_data),
        highest_pokemon_name=pokemons_data[highest["index"]]["name"],
        highest_pokemon_value=pokemons_data[highest["index"]]["height"],
        smallest_pokemon_name=pokemons_data[smallest["index"]]["name"],
        smallest_pokemon_value=pokemons_data[smallest["index"]]["height"],         
        heaviest_pokemon_name=pokemons_data[heaviest["index"]]["name"],
        heaviest_pokemon_value=pokemons_data[heaviest["index"]]["weight"],
        lightest_pokemon_name=pokemons_data[lightest["index"]]["name"],
        lightest_pokemon_value=pokemons_data[lightest["index"]]["weight"],        
        more_experience_pokemon_name=pokemons_data[more_experience["index"]]["name"],
        more_experience_pokemon_value=pokemons_data[more_experience["index"]]["base_experience"],
        total_alolas=total_alolas,
        final_question=YesNo.YES if snorlax_height > charizard_height else YesNo.NO,
       
    )


def show_info(pokemons_info):
    msg = """
    
                Welcome to the Pokedex!     
 ⣷⣿⣿⣶⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⢠⣴⣶⣷⣿⣿
⠀⠹⣿⣿⣿⡄⠀⠈⠓⠦⣄ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠖⠊⠉⠀⣸⣿⣿⣽⠃
⠀⠀⠘⣿⣿⣇⠀⠀⠀⠀⠀⠘⠶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⣿⣿⣿⠃⠀
⠀⠀⠀⠈⢻⣿ ⠀⠀⠀⠀⠀⠀⠈⠳⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠙⠁⠀⠀⠀⠀⠀⠀⡸⣿⠟⠁⠀⠀
⠀⠀⠀⠀⠀⠁⢾⡄⠀⠀⠀⠀⠀⠀⠀⠈⠱⣦⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⣠⠟⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠳⡄⠀⠀⠀⠀⠀⠀⠀⠈⠳⡆⣤⠴⠞⠛⠉⠉⠉⠉⠉⠉⠉⠳⠆⣤⣤⠞⠁⠀⠀⠀⠀⠀⠀⢀⣠⠖⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠖⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢳⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢇⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⣠⣶⠖⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠴⠶⣦⡄⠀⠀⢈⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠾⠀⠀⢰⣾⣷⣀⣰⡧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣀⣠⣾⣿⠀⠀⠀⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⠀⠀⠈⠻⣍⡩⠜⠃⠀⠀⠀⠠⣤⡤⠀⠀⠀⠀⠹⠭⣉⠽⠏⠀⠀⠀⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣤⠴⠴⣤⣠⣇⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⣤⣤⣼⣀⡴⢴⢦⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⠃⠀⠀⠀⠀⢹⡁⣀⡀⠙⣱⡀⠀⠀⠀⠲⣄⣠⡴⣒⢒⣤⣤⠴⠂⠀⠀⠀⢠⡞⢁⣀⡀⢨⠃⠀⠀⠀⠀⢹⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠉⠀⠉⠀⠈⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠈⠀⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠁⠈⠈⠈⠀⠉⠀⠀⠀⠀⠀⠀     
    Here we have some useful information gathered from the list you provided us:

    1. How many pokemons there is:
        > {total} pokemons.
    2. Which one is the highest:
        > Pokemon {highest_pokemon_name} with {highest_pokemon_value} decimetres.
    3. Which one is the smallest:
        > Pokemon {smallest_pokemon_name} with {smallest_pokemon_value} decimetres.    
    4. Which one is the heaviest:
        > Pokemon {heaviest_pokemon_name} with {heaviest_pokemon_value} hectograms.
    5. Which one is the lightest:
        > Pokemon {lightest_pokemon_name} with {lightest_pokemon_value} hectograms.            
    6. Which one is more worthy of defeating based on the experience gained from defeating them:
        > Pokemon {more_experience_pokemon_name} with {more_experience_pokemon_value} base experience.
    7. How many alola pokemons there is:
        > {total_alolas} alola pokemons.
    8. Is snorlax bigger than charizard:
        > {final_question}
    
    Thanks for using this pokedex!
    """
    print(msg.format(**pokemons_info))
    

       
def client_helper():
    helper_msg = """
    Hello! Welcome to the Pokedex.
    We will inform some statistic about your pokemon list.

    To use it, please inform the filename that contains your pokemon list.
    It should be a json file and each pokemon should be described as an item in a list with the following attributes:

    - id: The identifier for this resource. integer
    - name: The name for this resource. string
    - base_experience: The base experience gained for defeating this Pokémon. integer
    - height: The height of this Pokémon in decimetres. integer
    - weight: The weight of this Pokémon in hectograms. integer
    """
    return print(helper_msg)

def client_usage():
    client_usage_msg = """
    CLI usage:
        > python3 main.py --filename pokemons.json 
        > python3 main.py --help
        
    """
    return print(client_usage_msg)

def main():
    if len(sys.argv) == 1:
        client_usage()
        quit()
        
    elif len(sys.argv) > 3:
       print(f"WARNING! Incorrect amount of arguments.\n{client_usage()}")
       quit()

    command = sys.argv[1]

    if command == "--help":
        client_helper()
        quit()

    elif command == "--filename":
        if len(sys.argv) == 2:
            print(f"WARNING! Incorrect amount of arguments.\n{client_usage()}")
            quit()
    
        filepath = sys.argv[2]
        if not os.path.exists(filepath):
                print(f"WARNING: File {filepath} does not exist.")
                quit()        

        data = read_file(filepath)
        info = process_pokemons(data)
        show_info(info)
    else:
        print(f"WARNING: This command does not exist.\n{client_usage()}")

        
if __name__ == "__main__":
    main()      
    