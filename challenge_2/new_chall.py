import os
import sys
import json
from enum import Enum

class Answers(TypedDict):
    
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
    

def show_info(pokemons_info):
    msg = """ """
    
    
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
                