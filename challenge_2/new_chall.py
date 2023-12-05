import os
import sys
import csv
from enum import Enum
from typing import Dict, Union, List, TypedDict, Optional



class Answers(TypedDict):
    p1_tot_info: int  
    p2_tot_info: int
    strgst_p1_info: str
    strgst_p2_info: str
    leg_1_info: int
    leg_2_info: int
    

   
def read_file(filepath): 
    with open(filepath, "r") as data:
        file = csv.DictReader(data, delimiter = ",")
        pokemons = [row for row in file]
        return pokemons
    

def cast_to_int(value):
    return int(value) if value is not None else 0    

def cast_to_bool(value):
    return True if value == "True" else False 

def cast_to_set():
    return

def start_battle():
    
    id = {"index": 0, "value": 0}
    name = {"index": 0, "value": 0}
    type_1 = {"index": 0, "value": 0}
    type_2 = {"index": 0, "value": 0}
    total = {"index": 0, "value": 0}
    hp = {"index": 0, "value": 0}
    attack = {"index": 0, "value": 0}
    defense = {"index": 0, "value": 0}
    sp_atk = {"index": 0, "value": 0}
    sp_def = {"index": 0, "value": 0}
    speed = {"index": 0, "value": 0}
    generation = {"index": 0, "value": 0}

def process_pokemons(process_poke1,process_poke2):
    
    strongest_p1 = {"index": 0, "value": 0}
    strongest_p2 = {"index": 0, "value": 0}
    legendary_1 = 0
    legendary_2 = 0
    tot_leg_1 = 0
    tot_leg_2 = 0
    
    
    
    for index, pokemon in enumerate(process_poke1):
        p1_total = (len(process_poke1)-1)
        #print("Arquivo 1: ",p1_total, "\n")
        
        
        attack = cast_to_int(pokemon["Attack"])
        if attack > strongest_p1["value"]:
            strongest_p1["index"] = index
            strongest_p1["value"] = attack
        
        legendary_1 = cast_to_bool(pokemon["Legendary"])     
        if legendary_1 == True:
            tot_leg_1 +=1  
        
             
    for index, pokemon in enumerate(process_poke2):
        p2_total = (len(process_poke2)-1)  
        #print("Arquivo 2: ",p2_total, "\n")
        
        attack = cast_to_int(pokemon["Attack"])
        if attack > strongest_p2["value"]:
            strongest_p2["index"] = index
            strongest_p2["value"] = attack

        legendary_2 = cast_to_bool(pokemon["Legendary"])
        if legendary_2 == True:
            tot_leg_2 +=1              
            
        
  
    return Answers(
        
        p1_tot_info = p1_total,
        p2_tot_info = p2_total,
        strgst_p1_info = process_poke1[strongest_p1["index"]]["Name"],
        strgst_p2_info = process_poke2[strongest_p2["index"]]["Name"],
        leg_1_info = tot_leg_1,
        leg_2_info = tot_leg_2
        
         
)

def show_info(process_pokemons):
    msg = """
                       | Player 1            | Player 2            |
    ------------------ | -------------------- -------------------- |
    Pokémons           |{p1_tot_info}                  |{p2_tot_info}                  |
    Strongest Pokémon  |{strgst_p1_info}|{strgst_p2_info}   |
    Legendaries        |{leg_1_info}                   |{leg_2_info}                   |
    Repeated Pokemons  |                                           | 
    Different Pokemons |                                           |
    ------------------ | ----------------------------------------- |
    """
    
    print(msg.format(**process_pokemons))
                  
def client_helper():
    helper_msg = """
    Hello! Welcome to the Pokedex.
    Here you can choose betweem two option, that are:
    
    -- info
    We'll show you comparative information about the two players pokemon lists.
    
    -- battle
    The two players will challenge each other and we'll provide information about the victorious. 
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
        
    elif len(sys.argv) == 2:
        command1 = sys.argv[1]
        if command1 == "--help":
            client_helper()
            quit()
        else:
            print(f"WARNING: This command does not exist.\n{client_usage()}")
            quit()
            
    elif len(sys.argv) > 6:
            print(f"WARNING! Incorrect amount of arguments.\n{client_usage()}")
            quit()

    command1 = sys.argv[1]

    if command1 == "--player1":
        if len(sys.argv) == 2:
            print(f"WARNING! Incorrect amount of arguments.\n{client_usage()}")
            quit()
    
        filepath_1 = sys.argv[2]
        if not os.path.exists(filepath_1):
                print(f"WARNING: File {filepath_1} does not exist.")
                quit()
        
        command2 = sys.argv[3]
        if command2 == "--player2":
            if len(sys.argv) == 4:
                print(f"WARNING! Incorrect amount of arguments.\n{client_usage()}")
                quit()
                
            filepath_2 = sys.argv[4]
            if not os.path.exists(filepath_2):
                    print(f"WARNING: File {filepath_2} does not exist.")
                    quit()
        else:
            print(f"WARNING: This command does not exist.\n{client_usage()}")
            quit()
    else:
        print(f"WARNING: This command does not exist.\n{client_usage()}")
        quit()            
        
    if len(sys.argv) == 5:
        print(f"WARNING! Incorrect amount of arguments.\n{client_usage()}")
        quit()
        
    file_csv_1 = read_file(filepath_1)
    file_csv_2 = read_file(filepath_2) 
            
    command3 = sys.argv[5]
    if command3 == "--info":   
        info = process_pokemons(file_csv_1,file_csv_2)
        show_info(info)
        
    elif command3 == "--battle":
        print("Batalha pokemon!")
    
    else:
        print(f"WARNING: This command does not exist.\n{client_usage()}")
        quit()

        
if __name__ == "__main__":
    main()      
                