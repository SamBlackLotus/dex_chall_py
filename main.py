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


def read_file(filepath):
    with open((filepath), "r") as source_pokedex:
        return json.load(source_pokedex)
    

def cast_to_int(value):
    return int(value) if value is not None else 0


def process_pokemons(pokemons):
    highest = {"idx": 0, "value": 0}
    heaviest = {"idx": 0, "value": 0}
    more_experience = {"idx": 0, "value": 0}
    total_alolas = 0
    snorlax_height = 0
    charizard_height = 0

    for idx, pokemon in enumerate(pokemons):
        height_int = cast_to_int(pokemon["height"])
        if height_int > highest["value"]:
            highest["idx"] = idx
            highest["value"] = height_int

        weight_int = cast_to_int(pokemon["weight"])
        if weight_int > heaviest["value"]:
            heaviest["idx"] = idx
            heaviest["value"] = weight_int

        base_experience_int = cast_to_int(pokemon["base_experience"])
        if base_experience_int > more_experience["value"]:
            more_experience["idx"] = idx
            more_experience["value"] = base_experience_int
        
        if "alola" in pokemon["name"]:
            total_alolas += 1
        
        if pokemon["name"] == "snorlax":
            snorlax_height = pokemon["height"]
        
        if pokemon["name"] == "charizard":
            charizard_height = pokemon["height"]

    return Answers(
        total=len(pokemons),
        highest_pokemon_name=pokemons[highest["idx"]]["name"],
        highest_pokemon_value=pokemons[highest["idx"]]["height"],
        heaviest_pokemon_name=pokemons[heaviest["idx"]]["name"],
        heaviest_pokemon_value=pokemons[heaviest["idx"]]["weight"],
        more_experience_pokemon_name=pokemons[more_experience["idx"]]["name"],
        more_experience_pokemon_value=pokemons[more_experience["idx"]]["base_experience"],
        total_alolas=total_alolas,
        final_question=YesNo.YES if snorlax_height > charizard_height else YesNo.NO
    )


def show_info(pokemons_info):
    msg = """
    Pokedex information:

    1. How many pokemons there is:
        > {total} pokemons.
    2. Which one is the highest:
        > Pokemon {highest_pokemon_name} with {highest_pokemon_value} decimetres.
    3. Which one is the heaviest:
        > Pokemon {heaviest_pokemon_name} with {heaviest_pokemon_value} hectograms.
    4. Which one is more worthy of defeating based on the experience gained from defeating them:
        > Pokemon {more_experience_pokemon_name} with {more_experience_pokemon_value} base experience.
    5. How many alola pokemons there is:
        > {total_alolas} alola pokemons.
    6. Is snorlax bigger than charizard:
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
                print(f"WARNING: File {filepath} don't exist.")
                quit()        

        data = read_file(filepath)
        info = process_pokemons(data)
        show_info(info)
    else:
        print(f"WARNING: This command don't exist.\n{client_usage()}")

        
if __name__ == "__main__":
    main()      
    