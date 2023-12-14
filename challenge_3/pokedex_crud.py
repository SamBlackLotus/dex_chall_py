import os
import sys
import json
import csv
import xmltodict
import yaml
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

def read_file_json(filepath): #função pra processar arquivos json
    with open((filepath), "r") as source_pokedex:
        return json.load(source_pokedex)
   
def read_file_csv(filepath: str) -> List[Dict[str, Union[str, int]]]:
    with open(filepath, "r") as data:
        file = csv.DictReader(data, delimiter = ",")
        pokemons = [row for row in file]
        return pokemons

def read_file_xml(filepath: str) -> List[Dict[str, Union[str, int]]]: #função pra processar arquivos xml
    with open(filepath, "r", encoding= "UTF-8") as data:
        file = data.read()
        pokemons = xmltodict.parse(file)
        print(pokemons)
        return pokemons

def read_file_yaml(filepath: str) -> List[Dict[str, Union[str, int]]]: #função pra processar arquivos yaml
    with open(filepath, "r") as data:
        file = data.read()
        pokemons = yaml.safe_load(file)
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
    
def poke_trivia(pokemons_data):
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
    
def show_trivia(pokemons_info):
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
    pokemon, where the first pokemon to fall decides the winner, and we'll
    show you the battle information.
    """
    return print(helper_msg)

def client_usage() -> str:
    client_usage_msg = """
    CLI usage:
    
        > python3 pokedex_crud.py --help
        > python3 pokedex_crud.py --player1 pokemons_1.json --trivia
        > python3 pokedex_crud.py --player1 pokemons_1.json --player2 pokemons_2.json --info
        > python3 pokedex_crud.py --player1 pokemons_1.json --player2 pokemons_2.json --battle
        
        ATENTION:
        
        Where you read <pokemons_1.json> or <pokemons_2.json> 
        You can use the file format that best suits your needs
        Example --> pokemons_1.json  pokemons_2.json 
                    pokemons_1.csv   pokemons_2.csv
                    pokemons_1.xml   pokemons_2.xml
                    pokemons_1.yaml  pokemons_2.yaml
        
        
    """
    return print(client_usage_msg) 

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
        elif len(sys.argv) == 3:
            print(f"WARNING! Incorrect amount of arguments.\n{client_usage()}")
            quit()    
    
        filepath_1 = sys.argv[2]
        if not os.path.exists(filepath_1):
                print(f"WARNING: File {filepath_1} does not exist.")
                quit()
        
        command2 = sys.argv[3]
        
        if command2 == "--trivia":
            if len(sys.argv) >= 5:
                print(f"WARNING! Incorrect amount of arguments.\n{client_usage()}")
                quit()
            
            if '.json' in filepath_1:    
                data_1 = read_file_json(filepath_1)
            elif '.csv' in filepath_1:    
                data_1 = read_file_json(filepath_1)
            elif '.xml' in filepath_1:    
                data_1 = read_file_json(filepath_1)
            elif '.yaml' in filepath_1:    
                data_1 = read_file_json(filepath_1)
            else:
                print("Erro formato de arquivo não suportado")
                
            info = poke_trivia(data_1)
            show_trivia(info)
            
        elif command2 == "--player2":
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
        
        if len(sys.argv) == 5:
            print(f"WARNING! Incorrect amount of arguments.\n{client_usage()}")
            quit()
    
        if '.json' in filepath_1:
            data_1 = read_file_json(filepath_1)
            dataset_1 = cast_to_set(data_1)
        elif '.csv' in filepath_1:
            data_1 = read_file_csv(filepath_1)
            dataset_1 = cast_to_set(data_1)
        elif '.xml' in filepath_1:
            data_1 = read_file_xml(filepath_1)
            dataset_1 = cast_to_set(data_1)
        elif '.yaml' in filepath_1:
            data_1 = read_file_yaml(filepath_1)
            dataset_1 = cast_to_set(data_1)
        
        if '.json' in filepath_2:
            data_2= read_file_json(filepath_2)
            dataset_2 = cast_to_set(data_2)
        elif '.csv' in filepath_2:
            data_2 = read_file_csv(filepath_2)
            dataset_2 = cast_to_set(data_2)
        elif '.xml' in filepath_2:
            data_2 = read_file_xml(filepath_2)
            dataset_2 = cast_to_set(data_2)
        elif '.yaml' in filepath_2:
            data_2 = read_file_yaml(filepath_2)
            dataset_2 = cast_to_set(data_2)
        
        command3 = sys.argv[5]
        
        if command3 == "--info":   
            info = process_pokemons(data_1,data_2,dataset_1,dataset_2)
            show_info(info)
            
        elif command3 == "--battle":
            battle = start_battle(data_1,data_2)
            show_battle_info(battle)      
    else:
        print(f"WARNING: This command does not exist.\n{client_usage()}")
        quit()
       
if __name__ == "__main__":
    main()      
                