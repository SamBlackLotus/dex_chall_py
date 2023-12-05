import os
import sys
import csv
from enum import Enum
from typing import Dict, Union, List, TypedDict, Optional


class Answers(TypedDict):
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
    strongest_p1: str
    
  
   
def read_file(filepath_1): 
    with open(filepath_1, "r") as data_1:
        file_1 = csv.DictReader(data_1, delimiter = ",")
        p1_pokemons = [row for row in file_1]
        return p1_pokemons
    

def cast_to_int(value):
    return int(value) if value is not None else 0    


def process_pokemons(process_poke1,process_poke2):
    name = {"index": 0, "value": 0}
    type_1 = {"index": 0, "value": 0}
    type_2 = {"index": 0, "value": 0}
    total = {"index": 0, "value": 0}
    hp = {"index": 0, "value": 0}
    defense = {"index": 0, "value": 0}
    sp_atk = {"index": 0, "value": 0}
    sp_def = {"index": 0, "value": 0}
    speed = {"index": 0, "value": 0}
    generation = {"index": 0, "value": 0}
    legendary = {"index": 0, "value": 0}
    strongest_p1 = {"index": 0, "value": 0}
    strongest_p2 = {"index": 0, "value": 0}
    
    
    
    for index, pokemon in enumerate(process_poke1):
        p1_total = (len(process_poke1)-1)
        #print("Arquivo 1: ",p1_total, "\n")
        
        
        attack = cast_to_int(pokemon["Attack"])
        if attack > strongest_p1["value"]:
            strongest_p1["index"] = index
            strongest_p1["value"] = attack
            
        
             
    for index, pokemon in enumerate(process_poke2):
        p2_total = (len(process_poke2)-1)  
        #print("Arquivo 2: ",p2_total, "\n")
        
        attack = cast_to_int(pokemon["Attack"])
        if attack > strongest_p2["value"]:
            strongest_p2["index"] = index
            strongest_p2["value"] = attack
        
  
    return Answers(
        
        p1_tot_info = p1_total,
        p2_tot_info = p2_total,
        strgst_p1_info = strongest_p1["index"],
        strgst_p2_info = strongest_p2["index"]
         
)

def show_info(process_pokemons):
    msg = """
                       | Player 1            | Player 2            |
    ------------------ | -------------------- -------------------- |
    Pokémons           | {p1_tot_info}                 | {p2_tot_info}                 |
    Strongest Pokémon  | {strgst_p1_info}                  | {strgst_p2_info}                 |
    Legendaries        |                     |                     |
    Repeated Pokemons  |                                           |
    Different Pokemons |                                           |
    ------------------ | ----------------------------------------- |
    """
    
    print(msg.format(**process_pokemons))
                  
def client_helper():
    helper_msg = """
    Hello! Welcome to the Pokedex.
    We will inform some statistic about your pokemon list.
    """
    return print(helper_msg)

def client_usage():
    client_usage_msg = """
    CLI usage:
        > python3 new_chall.py --player1 pokemons_1.csv --player2 pokemons_2.csv --info
        > python3 new_chall.py --player1 pokemons_1.csv --player2 pokemons_2.csv --battle
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
                
        filepath_2 = sys.argv[4]
        if not os.path.exists(filepath_2):
                 print(f"WARNING: File {filepath_2} does not exist.")
                 quit()           
                
                     
        
        file_csv_1 = read_file(filepath_1)
        file_csv_2 = read_file(filepath_2)
        info = process_pokemons(file_csv_1,file_csv_2)
        show_info(info)
    else:
        print(f"WARNING: This command does not exist.\n{client_usage()}")

        
if __name__ == "__main__":
    main()      
                