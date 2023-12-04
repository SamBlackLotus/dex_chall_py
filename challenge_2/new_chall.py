import os
import sys
import csv
import enum
from typing import Dict, Union, List, TypedDict, Optional


class Attributes(TypedDict):
    Id: int
    Name: str
    Type1: str
    Type2: str
    Total: int
    HP: int
    Attack: int
    Defense: int
    Sp_Atk: int
    Sp_Def: int
    Speed: int
    Generation: str
    Legendary: bool
   
def read_file_1(filepath_1):
    with open((filepath_1), "r") as data_1:
        player_1_pokemons = csv.DictReader(data_1, delimiter = ",")
                

def show_info():
    info_table = print("""
                   | Player 1            | Player 2            |
------------------ | -------------------- -------------------- |
pokemons           | {pokemons_ammount}  | 2                   |
strongest pokemon  | charmander          | snorlax             |
legendaries        | 2                   | 0                   |
repeated pokemons  | 5                                         |
different pokemons | 50                                        |
------------------ | ----------------------------------------- |
""")
                    return info_table
                          

            
# def read_file_2(filepath_2):
#     with open((filepath_2), newline='') as data_2:

#         reader_2 = csv.DictReader(data_2)

#         for row in reader_2:
            
#             print(row)            
 
# def cast_to_int(value):
#     return int(value) if value is not None else 0


def process_pokemons(player_1_pokemons):
    
    Id = {"index": 0, "value": 0}
    Name = {"index": 0, "value": 0}
    Type1 = {"index": 0, "value": 0}
    Type2 = {"index": 0, "value": 0}
    Total = {"index": 0, "value": 0}
    HP = {"index": 0, "value": 0}
    Attack = {"index": 0, "value": 0}
    Defense = {"index": 0, "value": 0}
    Sp_Atk = {"index": 0, "value": 0}
    Sp_Def = {"index": 0, "value": 0}
    Speed = {"index": 0, "value": 0}
    Generation = {"index": 0, "value": 0}
    Legendary = {"index": 0, "value": 0}
    pokemons_ammount = 
    
    
    for index, pokemon in enumerate(pokemons_data):
        return

                  
def client_helper():
    helper_msg = """
    Hello! Welcome to the Pokedex.
    We will inform some statistic about your pokemon list.
    """
    return print(helper_msg)

def client_usage():
    client_usage_msg = """
    CLI usage:
        > python3 new_chall.py --player1 pokemons_1.csv 
        > python3 new_chall.py --help
        
    """
    return client_usage_msg 

def main():
    if len(sys.argv) == 1:
        client_usage()
        quit()
        
    elif len(sys.argv) > 5:
       print(f"WARNING! Incorrect amount of arguments.\n{client_usage()}")
       quit()

    command = sys.argv[1]

    if command == "--help":
        client_helper()
        quit()

    elif command == "--player1":
        if len(sys.argv) == 2:
            print(f"WARNING! Incorrect amount of arguments.\n{client_usage()}")
            quit()
    
        filepath_1 = sys.argv[2]
        if not os.path.exists(filepath_1):
                print(f"WARNING: File {filepath_1} does not exist.")
                quit()  
                
        # filepath_2 = sys.argv[4]
        # if not os.path.exists(filepath_2):
        #         print(f"WARNING: File {filepath_2} does not exist.")
        #         quit()           
                
                     

        data_1 = read_file_1(filepath_1)
        #data_2 = read_file_2(filepath_2)
        info = process_pokemon(data_1)
        #show_info(info)
    else:
        print(f"WARNING: This command does not exist.\n{client_usage()}")

        
if __name__ == "__main__":
    main()      
                