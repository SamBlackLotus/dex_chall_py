import os
import sys
import csv
import xmltodict
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
    p1_pkm_1_name: str   
    p1_pkm_2_name: str  
    p1_pkm_3_name: str  
    p2_pkm_1_name: str  
    p2_pkm_2_name: str  
    p2_pkm_3_name: str
    p1_pkm_1_hp: int
    p1_pkm_2_hp: int 
    p1_pkm_3_hp: int
    p2_pkm_1_hp: int
    p2_pkm_2_hp: int
    p2_pkm_3_hp: int 
    p1_pkm_1_atk: int
    p1_pkm_2_atk: int
    p1_pkm_3_atk: int
    p2_pkm_1_atk: int
    p2_pkm_2_atk: int
    p2_pkm_3_atk: int
    p1_pkm_1_dfs: int
    p1_pkm_2_dfs: int
    p1_pkm_3_dfs: int
    p2_pkm_1_dfs: int
    p2_pkm_2_dfs: int
    p2_pkm_3_dfs: int
    winner: int
    rounds: int
    loser_pokemon: str

   
def read_file_csv(filepath: str) -> List[Dict[str, Union[str, int]]]:
    with open(filepath, "r") as data:
        file = csv.DictReader(data, delimiter = ",")
        pokemons = [row for row in file]
        return pokemons

def read_file_xml(filepath: str) -> List[Dict[str, Union[str, int]]]:
    with open(filepath, "r", encoding= 'utf-8') as data:
        file = data.read()
        pokemons = xmltodict.parse(file, process_namespaces= True)
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
                       | PLAYER 1            | PLAYER 2            |
    ------------------ | -------------------- -------------------- |
    Pokémons           |{p1_tot_info}                  |{p2_tot_info}                  |
    Strongest Pokémon  |{strgst_p1_info}|{strgst_p2_info}   |
    Legendaries        |{leg_1_info}                   |{leg_2_info}                   |
    Repeated Pokemons  |{rep_pok_info}                                        | 
    Different Pokemons |{diff_pok_info}                                        |
    ------------------ | ----------------------------------------- |
    """
    
    print(msg.format(**process_pokemons))
    
def start_battle(player_1_battle,player_2_battle: List[Dict[str, Union[str, int]]]) -> Dict[str, int]:
    
    hp = {"index": 0, "value": 0}
    attack = {"index": 0, "value": 0}
    defense = {"index": 0, "value": 0}  
    p1_pokemon_1 = {"player": 1, "index": 0, "name": 0, "attack": 0, "defense": 0, "hp": 0}
    p1_pokemon_2 = {"player": 1, "index": 0, "name": 0,  "attack": 0, "defense": 0, "hp": 0}
    p1_pokemon_3 = {"player": 1, "index": 0, "name": 0,  "attack": 0, "defense": 0, "hp": 0}
    p2_pokemon_1 = {"player": 2, "index": 0, "name": 0,  "attack": 0, "defense": 0, "hp": 0}
    p2_pokemon_2 = {"player": 2, "index": 0, "name": 0,  "attack": 0, "defense": 0, "hp": 0}
    p2_pokemon_3 = {"player": 2, "index": 0, "name": 0,  "attack": 0, "defense": 0, "hp": 0}
    first_pokemon_dead = {"player": 0, "index": 0, "name": 0,  "attack": 0, "defense": 0, "hp": 0}
    victorious_player = {"player": 0, "index": 0, "name": 0,  "attack": 0, "defense": 0, "hp": 0}
    while_counter = 0
    
    
    for index, pokemon in enumerate(player_1_battle):
        
        name = pokemon["Name"]
        attack = cast_to_int(pokemon["Attack"])
        defense = cast_to_int(pokemon["Defense"])
        hp = cast_to_int(pokemon["HP"])
        if attack > p1_pokemon_1["attack"]:
            p1_pokemon_1["index"] = index
            p1_pokemon_1["name"] = name
            p1_pokemon_1["attack"] = attack
            p1_pokemon_1["defense"] = defense
            p1_pokemon_1["hp"] = hp
            
         
        if attack > p1_pokemon_2["attack"] and index is not p1_pokemon_1["index"]:
            p1_pokemon_2["index"] = index
            p1_pokemon_2["name"] = name
            p1_pokemon_2["attack"] = attack
            p1_pokemon_2["defense"] = defense
            p1_pokemon_2["hp"] = hp
            
        if attack > p1_pokemon_3["attack"] and index is not p1_pokemon_1["index"] and index is not p1_pokemon_2["index"]:
            p1_pokemon_3["index"] = index
            p1_pokemon_3["name"] = name
            p1_pokemon_3["attack"] = attack        
            p1_pokemon_3["defense"] = defense
            p1_pokemon_3["hp"] = hp
    
    for index, pokemon in enumerate(player_2_battle):
        
        name = pokemon["Name"]
        attack = cast_to_int(pokemon["Attack"])
        defense = cast_to_int(pokemon["Defense"])
        hp = cast_to_int(pokemon["HP"])
        if attack > p2_pokemon_1["attack"]:
            p2_pokemon_1["index"] = index
            p2_pokemon_1["name"] = name
            p2_pokemon_1["attack"] = attack
            p2_pokemon_1["defense"] = defense
            p2_pokemon_1["hp"] = hp

        if attack > p2_pokemon_2["attack"] and index is not p2_pokemon_1["index"]:
            p2_pokemon_2["index"] = index
            p2_pokemon_2["name"] = name
            p2_pokemon_2["attack"] = attack
            p2_pokemon_2["defense"] = defense
            p2_pokemon_2["hp"] = hp
            
            
        if attack > p2_pokemon_3["attack"] and index is not p2_pokemon_1["index"] and index is not p2_pokemon_2["index"]:
            p2_pokemon_3["index"] = index
            p2_pokemon_3["name"] = name
            p2_pokemon_3["attack"] = attack        
            p2_pokemon_3["defense"] = defense
            p2_pokemon_3["hp"] = hp       
            
    damagep1poke1 = (0.5 * (p1_pokemon_1["attack"] / p2_pokemon_1["defense"]) + 1)         
    damagep1poke2 = (0.5 * (p1_pokemon_2["attack"] / p2_pokemon_2["defense"]) + 1) 
    damagep1poke3 = (0.5 * (p1_pokemon_3["attack"] / p2_pokemon_3["defense"]) + 1) 
    damagep2poke1 = (0.5 * (p2_pokemon_1["attack"] / p1_pokemon_1["defense"]) + 1) 
    damagep2poke2 = (0.5 * (p2_pokemon_2["attack"] / p1_pokemon_2["defense"]) + 1) 
    damagep2poke3 = (0.5 * (p2_pokemon_3["attack"] / p1_pokemon_3["defense"]) + 1)         
                     
    while True:
        
        while_counter += 1 
        
        p2_pokemon_1["hp"] -= damagep1poke1
        p2_pokemon_2["hp"] -= damagep1poke2
        p2_pokemon_3["hp"] -= damagep1poke3
        p1_pokemon_1["hp"] -= damagep2poke1
        p1_pokemon_2["hp"] -= damagep2poke2
        p1_pokemon_3["hp"] -= damagep2poke3
        
        
        if p1_pokemon_1["hp"] <= 0:
            first_pokemon_dead = p1_pokemon_1
            victorious_player = p2_pokemon_1
            break
        elif p1_pokemon_2["hp"] <= 0:
            first_pokemon_dead = p1_pokemon_2
            victorious_player = p2_pokemon_2
            break
        elif p1_pokemon_3["hp"] <= 0:
            first_pokemon_dead = p1_pokemon_3
            victorious_player = p2_pokemon_3
            break
        elif p2_pokemon_1["hp"] <= 0:
            first_pokemon_dead = p2_pokemon_1
            victorious_player = p1_pokemon_1
            break
        elif p2_pokemon_2["hp"] <= 0:
            first_pokemon_dead = p2_pokemon_2
            victorious_player = p1_pokemon_2
            break
        elif p2_pokemon_3["hp"] <= 0:    
            first_pokemon_dead = p2_pokemon_3
            victorious_player = p1_pokemon_3
            break
            
            
    return Answers(
        
        p1_pkm_1_name =  player_1_battle[p1_pokemon_1["index"]]["Name"],
        p1_pkm_2_name =  player_1_battle[p1_pokemon_2["index"]]["Name"],
        p1_pkm_3_name =  player_1_battle[p1_pokemon_3["index"]]["Name"],
        p2_pkm_1_name =  player_2_battle[p2_pokemon_1["index"]]["Name"],
        p2_pkm_2_name =  player_2_battle[p2_pokemon_2["index"]]["Name"],
        p2_pkm_3_name =  player_2_battle[p2_pokemon_3["index"]]["Name"],
        
        p1_pkm_1_hp =  player_1_battle[p1_pokemon_1["index"]]["HP"],
        p1_pkm_2_hp =  player_1_battle[p1_pokemon_2["index"]]["HP"],
        p1_pkm_3_hp =  player_1_battle[p1_pokemon_3["index"]]["HP"],
        p2_pkm_1_hp =  player_2_battle[p2_pokemon_1["index"]]["HP"],
        p2_pkm_2_hp =  player_2_battle[p2_pokemon_2["index"]]["HP"],
        p2_pkm_3_hp =  player_2_battle[p2_pokemon_3["index"]]["HP"],
        
        p1_pkm_1_atk =  player_1_battle[p1_pokemon_1["index"]]["Attack"],
        p1_pkm_2_atk =  player_1_battle[p1_pokemon_2["index"]]["Attack"],
        p1_pkm_3_atk =  player_1_battle[p1_pokemon_3["index"]]["Attack"],
        p2_pkm_1_atk =  player_2_battle[p2_pokemon_1["index"]]["Attack"],
        p2_pkm_2_atk =  player_2_battle[p2_pokemon_2["index"]]["Attack"],
        p2_pkm_3_atk =  player_2_battle[p2_pokemon_3["index"]]["Attack"],
        
        p1_pkm_1_dfs =  player_1_battle[p1_pokemon_1["index"]]["Defense"],
        p1_pkm_2_dfs =  player_1_battle[p1_pokemon_2["index"]]["Defense"],
        p1_pkm_3_dfs =  player_1_battle[p1_pokemon_3["index"]]["Defense"],
        p2_pkm_1_dfs =  player_2_battle[p2_pokemon_1["index"]]["Defense"],
        p2_pkm_2_dfs =  player_2_battle[p2_pokemon_2["index"]]["Defense"],
        p2_pkm_3_dfs =  player_2_battle[p2_pokemon_3["index"]]["Defense"],
        
        winner = victorious_player["player"],
        rounds = while_counter,
        loser_pokemon = first_pokemon_dead["name"]
                  
)        

def show_battle_info(start_battle: Answers) -> None:
    battle_msg = """
================================== POKéMON BATTLE ===================================

-------------------------------------------------------------------------------------
|                                    PLAYER 1                                       |
-------------------------------------------------------------------------------------
|Name:{p1_pkm_1_name}  |Name: {p1_pkm_2_name}  |Name: {p1_pkm_3_name}  |
|HP:{p1_pkm_1_hp}                      |HP:{p1_pkm_2_hp}                     |HP:{p1_pkm_3_hp}                      |
|Attack:{p1_pkm_1_atk}                  |Attack:{p1_pkm_2_atk}                |Attack:{p1_pkm_3_atk}                 | 
|Defense:{p1_pkm_1_dfs}                 |Defense:{p1_pkm_2_dfs}                |Defense:{p1_pkm_2_dfs}                 |
-------------------------------------------------------------------------------------

-------------------------------------------------------------------------------------
|                                    PLAYER 2                                       |
-------------------------------------------------------------------------------------
|Name:{p2_pkm_1_name}     |Name: {p2_pkm_2_name}  |Name: {p2_pkm_3_name}|
|HP:{p2_pkm_1_hp}                       |HP:{p2_pkm_2_hp}                    |HP:{p2_pkm_3_hp}                      |
|Attack:{p2_pkm_1_atk}                  |Attack:{p2_pkm_2_atk}                |Attack:{p2_pkm_3_atk}                 | 
|Defense:{p2_pkm_1_dfs}                  |Defense:{p2_pkm_2_dfs}               |Defense:{p2_pkm_2_dfs}                |
-------------------------------------------------------------------------------------
=====================================================================================
|                              +++++ RESULT +++++                                   |
=====================================================================================
|                        -----------------------------                              |
|                                  --Winner--                                       |
|                                   Player {winner}                                        |
|                        -----------------------------                              |
|                                  --Rounds--                                       |
|                                      {rounds}                                           |
|                        -----------------------------                              |
|                          --First pokemon to fall--                                |
|                              {loser_pokemon}                                   |
=====================================================================================
    """
    
    print(battle_msg.format(**start_battle))      
    
                  
def client_helper() -> None:
    helper_msg = """
    Hello! Welcome to the Pokedex.
    
    Here you can choose betweem the following options, that are:
    
    --trivia
    
    If you choose trivia we'll show you some interesting  information
    about the pokemon list you provided, notice that this option only
    works with one file at time, so inform just one list for each time 
    you use this option.
    
    For the next two options notice that we'll need two players, 
    and each player will need to provide a list, since the
    functions work with comparisons:
    
    -- info
    
    We'll show you some comparative information about the two players
    pokemon lists.
    
    -- battle
    
    The two players will challenge each other, using their three strongest
    pokemon, where the firts pokemon to fall decides the winner, and we'll
    show you the battle information.
    """
    return print(helper_msg)

def client_usage() -> str:
    client_usage_msg = """
    CLI usage:
    
        > python3 pokedex_crud.py --help
        > python3 pokedex_crud.py --player <player file and format> --trivia
        > python3 pokedex_crud.py --player1 <player 1 file and format> --player2 <player 2 file and format> --info
        > python3 pokedex_crud.py --player1 <player 1 file and format> --player2 <player 2 file and format> --battle
        
        ATENTION:
        
        Where you read <player file and format> follow the example --> pokemon_1.json 
                                                                       pokemon_1.csv
                                                                       pokemon_1.xml
                                                                       pokemon_1.yaml 
        
        
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
    
    if '.csv' in filepath_1:
        file_csv_1 = read_file_csv(filepath_1)
        file_set_1 = cast_to_set(file_csv_1)
    elif '.xml' in filepath_1:
        file_xml_1 = read_file_xml(filepath_1)
        print(file_xml_1)
        file_set_1 = cast_to_set(file_xml_1)
    
    if '.csv' in filepath_2:
        file_csv_2 = read_file_csv(filepath_2)
        file_set_2 = cast_to_set(file_csv_2)
    elif '.xml' in filepath_2:
        file_xml_2 = read_file_xml(filepath_2)
        file_set_2 = cast_to_set(file_xml_2)
    
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
                