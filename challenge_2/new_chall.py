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
    intersec_pokemon: int
    diff_pokemon: int 

   
def read_file(filepath: str) -> List[Dict[str, Union[str, int]]]:
    with open(filepath, "r") as data:
        file = csv.DictReader(data, delimiter = ",")
        pokemons = [row for row in file]
        return pokemons

def cast_to_set(file_set_1: str) -> List[str]:
    pokemon_set = set()
    for pokemon in file_set_1:
        pokemon_set.add(pokemon["Name"])
    return pokemon_set    

def cast_to_int(value: Optional[str]) -> int:
    return int(value) if value is not None else 0    

def cast_to_bool(value: Optional[str]) -> bool:
    return True if value == "True" else False 
    

def process_pokemons(process_poke1,process_poke2,pokemon_set_1,pokemon_set_2: List[Dict[str, Union[str, int]]]) -> Dict[str, str]:
    
    strongest_p1 = {"index": 0, "value": 0}
    strongest_p2 = {"index": 0, "value": 0}
    legendary_1 = 0
    legendary_2 = 0
    tot_leg_1 = 0
    tot_leg_2 = 0
    intersec_pokemon = (pokemon_set_1.intersection(pokemon_set_2))
    diff_pokemon = (pokemon_set_1.difference(pokemon_set_2)) 
    
    
    
    for index, pokemon in enumerate(process_poke1):
        p1_total = len(process_poke1)
        
        attack = cast_to_int(pokemon["Attack"])
        if attack > strongest_p1["value"]:
            strongest_p1["index"] = index
            strongest_p1["value"] = attack
        
        legendary_1 = cast_to_bool(pokemon["Legendary"])     
        if legendary_1 == True:
            tot_leg_1 +=1  
        
             
    for index, pokemon in enumerate(process_poke2):
        p2_total = len(process_poke2) 
        
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
        leg_2_info = tot_leg_2,
        rep_pok_info = len(intersec_pokemon),
        diff_pok_info = len(diff_pokemon)
         
         
)

def show_info(process_pokemons: Answers) -> None:
    msg = """
                       | Player 1            | Player 2            |
    ------------------ | -------------------- -------------------- |
    Pokémons           |{p1_tot_info}                  |{p2_tot_info}                  |
    Strongest Pokémon  |{strgst_p1_info}|{strgst_p2_info}   |
    Legendaries        |{leg_1_info}                   |{leg_2_info}                   |
    Repeated Pokemons  |{rep_pok_info}                                        | 
    Different Pokemons |{diff_pok_info}                                        |
    ------------------ | ----------------------------------------- |
    """
    
    print(msg.format(**process_pokemons))
    
def start_battle(player_1_battle,player_2_battle):
    
    id = {"index": 0, "value": 0}
    name = {"index": 0, "value": 0}
    hp = {"index": 0, "value": 0}
    attack = {"index": 0, "value": 0}
    defense = {"index": 0, "value": 0}  
    p1_pokemon_1= {"index": 0, "value": 0}
    p1_pokemon_2 = {"index": 0, "value": 0}
    p1_pokemon_3 = {"index": 0, "value": 0}
    p2_pokemon_1 = {"index": 0, "value": 0}
    p2_pokemon_2 = {"index": 0, "value": 0}
    p2_pokemon_3 = {"index": 0, "value": 0}
    
    for index, pokemon in enumerate(player_1_battle):
        
        attack = cast_to_int(sorted(pokemon["Attack"]))
        if attack > p1_pokemon_1["value"]:
            p1_pokemon_1["index"] = index
            p1_pokemon_1["value"] = attack
            
         
        if attack > p1_pokemon_2["value"]:
            p1_pokemon_2["index"] = index
            p1_pokemon_2["value"] = attack
            
            
        if attack > p1_pokemon_3["value"]:
            p1_pokemon_3["index"] = index
            p1_pokemon_3["value"] = attack        
            
    
    for index, pokemon in enumerate(player_2_battle):
        
        attack = cast_to_int(pokemon["Attack"])
        if attack > p2_pokemon_1["value"]:
            p2_pokemon_1["index"] = index
            p2_pokemon_1["value"] = attack

        if attack > p2_pokemon_2["value"]:
            p2_pokemon_2["index"] = index
            p2_pokemon_2["value"] = attack
            
            
        if attack > p2_pokemon_3["value"]:
            p2_pokemon_3["index"] = index
            p2_pokemon_3["value"] = attack        
                    
         
    return Answers(
        
        p1_pkm_1 =  player_1_battle[p1_pokemon_1["index"]]["Name"],
        p1_pkm_2 =  player_1_battle[p1_pokemon_2["index"]]["Name"],
        p1_pkm_3 =  player_1_battle[p1_pokemon_3["index"]]["Name"],
        p2_pkm_1 =  player_2_battle[p2_pokemon_1["index"]]["Name"],
        p2_pkm_2 =  player_2_battle[p2_pokemon_2["index"]]["Name"],
        p2_pkm_3 =  player_2_battle[p2_pokemon_3["index"]]["Name"]
         
         
)        

def show_battle_info(start_battle): 
    battle_msg = """
----- Battle -----

Player 1 pokemons: {p1_pkm_1}, {p1_pkm_2}, {p1_pkm_3}
Player 2 pokemons: {p2_pkm_1}, {p2_pkm_2}, {p2_pkm_3}

----- Result -----
Winner: Player 1
Rounds: 50
Pokemon that died: Archeops
    """
    
    print(battle_msg.format(**start_battle))      
    
                  
def client_helper() -> None:
    helper_msg = """
    Hello! Welcome to the Pokedex.
    Here you can choose betweem two option, that are:
    
    -- info
    We'll show you comparative information about the two players pokemon lists.
    
    -- battle
    The two players will challenge each other and we'll provide information about the victorious. 
    """
    return print(helper_msg)

def client_usage() -> str:
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
    file_set_1 = cast_to_set(file_csv_1)
    file_set_2 = cast_to_set(file_csv_2)
               
    command3 = sys.argv[5]
    if command3 == "--info":   
        info = process_pokemons(file_csv_1,file_csv_2,file_set_1,file_set_2)
        show_info(info)
        
    elif command3 == "--battle":
        battle = start_battle(file_csv_1,file_csv_2)
        show_battle_info(battle)
        
        
    
    else:
        print(f"WARNING: This command does not exist.\n{client_usage()}")
        quit()

        
if __name__ == "__main__":
    main()      
                