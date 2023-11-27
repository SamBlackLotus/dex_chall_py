import os
import sys
import json

def read_file(filename):
    with open((filename), "r") as source_pokedex:
        data = json.load(source_pokedex)


def client_helper():
    helper_msg = """
    Hi! Welcome to the pokedex.
    We will inform some statistic about your pokemon list.

    To use it, please inform the filename that contains your pokemon list.
    It should be a json file and each pokemon should be described as an item in a list with the following attributes:

    - id: The identifier for this resource. integer
    - name: The name for this resource. string
    - base_experience: The base experience gained for defeating this Pokémon. integer
    - height: The height of this Pokémon in decimetres. integer
    - weight: The weight of this Pokémon in hectograms. integer
    """
    print(helper_msg)

def client_usage():
    client_usage_msg = """
    CLI usage:
        > python3 main.py --filename pokemons.json 
        > python3 main.py --help
    """
    return client_usage_msg

def main():
    if len(sys.argv) == 1:
        print(client_usage())
        quit()
        
    elif len(sys.argv) > 3:
        print("Warning! Incorrect amount of arguments.")
        quit()

    command = sys.argv[1]

    if command == "--help":
        client_helper()
        quit()

    elif command == "--filename":
        if len(sys.argv) == 2:
            print("Warning! Incorrect amount of arguments.")
            quit()
            

if __name__ == "__main__":
    main()            