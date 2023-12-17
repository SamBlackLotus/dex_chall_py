import os
import sys
import json
import csv
import xmltodict
import xml.etree.ElementTree as ET
import yaml
from datetime import datetime
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
    
#Receive and read json files 
def read_file_json(filepath): 
    with open((filepath), "r") as source_pokedex:
        return json.load(source_pokedex)
    
#Receive and read csv files       
def read_file_csv(filepath):
    with open(filepath, "r") as data:
        file = csv.DictReader(data, delimiter = ",")
        pokemons = [row for row in file]
        print(file)
        return pokemons

#Receive and read xml files    
def read_file_xml(filepath): 
    with open(filepath, "r") as data:
        file = data.read()
        pokemonsxml = xmltodict.parse(file)
        pokemonsid = {chave: valor for chave, valor in pokemonsxml['root'].items()}
        pokemons= {}
        for chave, valor in pokemonsid.items():
            pokemons = [{a: i for a, i in valor.items()}]
    return pokemons

#Receive and read yaml files 
def read_file_yaml(filepath):
    with open(filepath, "r") as data:
        file = data.read()
        pokemons = yaml.safe_load(file)
        return pokemons
    
#Cast the dict data received into a set
def cast_to_set(file_set_1):
    pokemon_set = set()
    for pokemon in file_set_1:
        pokemon_set.add(pokemon["Name"])
    return pokemon_set    

#Cast the needed values into integers
def cast_to_int(value):
    return int(value) if value is not None else 0
    
#Cast the needed values into boolean
def cast_to_bool(value):
    return True if value == "True" else False 

#Process and generate the answers to the trivia questions    
def process_trivia(pokemons_data):
    highest_hp_trivia = {"index":0, "value":0}
    highest_atk_trivia = {"index": 0, "value": 0}
    highest_def_trivia = {"index": 0, "value": 0}
    highest_spd_trivia = {"index": 0, "value": 0}
    for index, pokemon in enumerate(pokemons_data):

        hp_trivia_int = cast_to_int(pokemon["HP"])
        if hp_trivia_int > highest_hp_trivia["value"]:
            highest_hp_trivia["index"] = index
            highest_hp_trivia["value"] = hp_trivia_int
      
        attack_trivia_int = cast_to_int(pokemon["Attack"])
        if attack_trivia_int > highest_atk_trivia["value"]:
            highest_atk_trivia["index"] = index
            highest_atk_trivia["value"] = attack_trivia_int
            
        defense_trivia_int = cast_to_int(pokemon["Defense"])
        if defense_trivia_int > highest_def_trivia["value"]:
            highest_def_trivia["index"] = index
            highest_def_trivia["value"] = defense_trivia_int
      
        speed_trivia_int = cast_to_int(pokemon["Attack"])
        if speed_trivia_int > highest_spd_trivia["value"]:
            highest_spd_trivia["index"] = index
            highest_spd_trivia["value"] = speed_trivia_int    
            
  
            

    return Answers(
        total_trivia=len(pokemons_data),
        hp_trivia_name=pokemons_data[highest_hp_trivia["index"]]["Name"],
        hp_trivia_points=pokemons_data[highest_hp_trivia["index"]]["HP"],
        atk_trivia_name=pokemons_data[highest_atk_trivia["index"]]["Name"],
        atk_trivia_points=pokemons_data[highest_atk_trivia["index"]]["Attack"],
        def_trivia_name=pokemons_data[highest_atk_trivia["index"]]["Name"],
        def_trivia_points=pokemons_data[highest_atk_trivia["index"]]["Defense"],
        spd_trivia_name=pokemons_data[highest_atk_trivia["index"]]["Name"],
        spd_trivia_points=pokemons_data[highest_atk_trivia["index"]]["Speed"]
     
    )
#Show the information gathered inn the trivia function    
def show_trivia(pokemons_info, idnumber):
    datenow =  datetime.now()
    msg  = "reported generated on:   " + datenow.isoformat() + "                                                  \n"
    msg += "                                                                           \n"
    msg += "                             Welcome to the Pokedex!                       \n"
    msg += "        ⣷⣿⣿⣶⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⢠⣴⣶⣷⣿⣿    \n"
    msg += "       ⠀⠹⣿⣿⣿⡄⠀⠈⠓⠦⣄ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠖⠊⠉⠀⣸⣿⣿⣽⠃    \n"
    msg += "       ⠀⠀⠘⣿⣿⣇⠀⠀⠀⠀⠀⠘⠶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⣿⣿⣿⠃⠀    \n"
    msg += "       ⠀⠀⠀⠈⢻⣿ ⠀⠀⠀⠀⠀⠀⠈⠳⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠙⠁⠀⠀⠀⠀⠀⠀⡸⣿⠟⠁⠀⠀    \n"
    msg += "       ⠀⠀⠀⠀⠀⠁⢾⡄⠀⠀⠀⠀⠀⠀⠀⠈⠱⣦⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⣠⠟⠁⠀⠀⠀     \n"
    msg += "       ⠀⠀⠀⠀⠀⠀⠀⠉⠳⡄⠀⠀⠀⠀⠀⠀⠀⠈⠳⡆⣤⠴⠞⠛⠉⠉⠉⠉⠉⠉⠉⠳⠆⣤⣤⠞⠁⠀⠀⠀⠀⠀⠀⢀⣠⠖⠁⠀⠀⠀⠀⠀     \n"
    msg += "       ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠖⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀    \n"
    msg += "       ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢳⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢇⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    \n"
    msg += "       ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    \n"
    msg += "        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   \n"
    msg += "        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⣠⣶⠖⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠴⠶⣦⡄⠀⠀⢈⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   \n"
    msg += "        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠾⠀⠀⢰⣾⣷⣀⣰⡧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣀⣠⣾⣿⠀⠀⠀⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   \n"
    msg += "        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⠀⠀⠈⠻⣍⡩⠜⠃⠀⠀⠀⠠⣤⡤⠀⠀⠀⠀⠹⠭⣉⠽⠏⠀⠀⠀⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   \n"
    msg += "        ⠀⠀⠀⠀⠀⠀⠀⢀⣤⠴⠴⣤⣠⣇⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⣤⣤⣼⣀⡴⢴⢦⣄⠀⠀⠀⠀⠀⠀⠀   \n"
    msg += "        ⠀⠀⠀⠀⠀⠀⢸⠃⠀⠀⠀⠀⢹⡁⣀⡀⠙⣱⡀⠀⠀⠀⠲⣄⣠⡴⣒⢒⣤⣤⠴⠂⠀⠀⠀⢠⡞⢁⣀⡀⢨⠃⠀⠀⠀⠀⢹⠀⠀⠀⠀⠀⠀   \n"
    msg += "        ⠀⠀⠀⠀⠀⠀⠈⠉⠀⠉⠀⠈⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠈⠀⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠁⠈⠈⠈⠀⠉⠀⠀⠀⠀⠀⠀   \n"    
    msg += "Here we have some useful information gathered from the list you provided us:\n"
    msg += "                                                                            \n"
    msg += "1. How many pokemons there is in this list:                                 \n"
    msg += "    > " + str(pokemons_info["total_trivia"]) + " pokemons.                         \n"
    msg += "                                                                            \n"
    msg += "2. The pokemon with the highest HP point is:                                \n"
    msg += "    >" + pokemons_info["hp_trivia_name"] + " with " + str(pokemons_info["hp_trivia_points"]) + " HP points                     \n"
    msg += "                                                                            \n"
    msg += "3. Which one has the strongest attack:                                      \n"
    msg += "    >" + pokemons_info["atk_trivia_name"] + " with " + str(pokemons_info["atk_trivia_points"]) + " attack points.              \n"
    msg += "                                                                            \n"
    msg += "4. Which one has the strongest defense:                                     \n"
    msg += "    >" + pokemons_info["def_trivia_name"] + " with " + str(pokemons_info["def_trivia_points"]) + " defense points.             \n"
    msg += "                                                                            \n"
    msg += "5. Which one is the fastest:                                                \n"
    msg += "    >" + pokemons_info["spd_trivia_name"] + " with " + str(pokemons_info["spd_trivia_points"]) + " speed points.               \n"
    msg += "                                                                            \n"
    msg += "                                                                            \n"
    msg += "Thanks for using this pokedex!                                              \n"
    
    if os.path.exists(f"{idnumber}_trivia.txt"):
        
        choice = input(f"Files {idnumber}_trivia.txt already exists, what do you prefer to do? [append|OVERWRITE] : ")
        
        if choice == 'o' or choice == 'O' or choice == 'Overwrite' or choice == 'overwrite' or choice == 'OVERWRITE':
           
            os.remove(f"{idnumber}_trivia.txt")
            
            with open(f"{idnumber}_trivia.txt", "w") as target:
                target.write(msg)
        elif choice == 'a' or choice == 'A' or choice == 'Append' or choice == 'append' or choice == 'APPEND':
           
            with open(f"{idnumber}_trivia.txt", "a") as target:
                target.write(msg)  
    else:
        
        with open(f"{idnumber}_trivia.txt", "w") as target:
            target.write(msg)
    
    print(msg.format(**pokemons_info))
       
#Process the information read in the files and generate the info table 
def process_info(process_poke1,process_poke2,pokemon_set_1,pokemon_set_2):
    
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
    
#Show the information gathered in the info process function
def show_info(process_pokemons, idnumber):
    
    datenow =  datetime.now()
    msg  = "reported generated on:   " + datenow.isoformat() + "                                                  \n"
    msg += "                   | PLAYER 1            | PLAYER 2            |\n"
    msg += "------------------ | -------------------- -------------------- |\n"
    msg += "Pokémons           |" + str(process_pokemons["p1_tot_info"]) + "                  |" + str(process_pokemons["p2_tot_info"]) + "                  |\n"
    msg += "Strongest Pokémon  |" + process_pokemons["strgst_p1_info"] + "|" + process_pokemons["strgst_p2_info"] + "   |\n"
    msg += "Legendaries        |" + str(process_pokemons["leg_1_info"]) + "                   |" + str(process_pokemons["leg_2_info"]) + "                   |\n"
    msg += "Repeated Pokemons  |" + str(process_pokemons["rep_pok_info"]) + "                                        |\n"
    msg += "Different Pokemons |" + str(process_pokemons["diff_pok_info"]) + "                                        |\n"
    msg += "------------------ | ----------------------------------------- |\n"
    
    if os.path.exists(f"{idnumber}_info.txt"):
        
        choice = input(f"Files {idnumber}_info.txt already exists, what do you prefer to do? [append|OVERWRITE] : ")
        
        if choice == 'o' or choice == 'O' or choice == 'Overwrite' or choice == 'overwrite' or choice == 'OVERWRITE':
           
            os.remove(f"{idnumber}_info.txt")
            
            with open(f"{idnumber}_info.txt", "w") as target:
                target.write(msg)
        elif choice == 'a' or choice == 'A' or choice == 'Append' or choice == 'append' or choice == 'APPEND':
           
            with open(f"{idnumber}_info.txt", "a") as target:
                target.write(msg)  
    else:
        
        with open(f"{idnumber}_info.txt", "w") as target:
            target.write(msg)
    
    print(msg.format(**process_pokemons))
    

#Process the information read in the files, compare the pokemons in each list to define
#wich three of each player will participate in the battle 
def select_pokemons_for_battle(player_1_battle,player_2_battle):
    
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
#Show the information about wich pokemons participated in the battle, and wich player was the winner
def show_battle_winner(start_battle, idnumber):
    
    datenow =  datetime.now()
    battle_msg  = "reported generated on:   " + datenow.isoformat() + "                                                  \n"
    battle_msg +=  "================================== POKéMON BATTLE ===================================\n"
    battle_msg += "                                                                                     \n"
    battle_msg += "-------------------------------------------------------------------------------------\n"
    battle_msg += "|                                    PLAYER 1                                        |\n"
    battle_msg += "-------------------------------------------------------------------------------------\n"
    battle_msg += "|Name: " + start_battle["p1_pkm_1_name"] + "  |Name: " + start_battle["p1_pkm_2_name"] + "   |Name: " + start_battle["p1_pkm_3_name"] + " |\n"
    battle_msg += "|HP: " + str(start_battle["p1_pkm_1_hp"]) + "                      |HP: " + str(start_battle["p1_pkm_2_hp"]) + "                     |HP: " + str(start_battle["p1_pkm_3_hp"]) + "                    |\n"
    battle_msg += "|Attack: " + str(start_battle["p1_pkm_1_atk"]) + "                  |Attack: " + str(start_battle["p1_pkm_2_atk"]) + "                |Attack: " + str(start_battle["p1_pkm_3_atk"]) + "               |\n"
    battle_msg += "|Defense: " + str(start_battle["p1_pkm_1_dfs"]) + "                 |Defense: " + str(start_battle["p1_pkm_2_dfs"]) + "                |Defense: " + str(start_battle["p1_pkm_2_dfs"]) + "               |\n"
    battle_msg += "-------------------------------------------------------------------------------------\n"
    battle_msg += "|                                    PLAYER 2                                        |\n"
    battle_msg += "-------------------------------------------------------------------------------------\n"
    battle_msg += "|Name: " + start_battle["p2_pkm_1_name"] + "     |Name: " + start_battle["p2_pkm_2_name"] + "   |Name: " + start_battle["p2_pkm_3_name"] + "|\n"
    battle_msg += "|HP: " + str(start_battle["p2_pkm_1_hp"]) + "                       |HP: " + str(start_battle["p2_pkm_2_hp"]) + "                    |HP: " + str(start_battle["p2_pkm_3_hp"]) + "                    |\n"
    battle_msg += "|Attack: " + str(start_battle["p2_pkm_1_atk"]) + "                  |Attack: " + str(start_battle["p2_pkm_2_atk"]) + "                |Attack: " + str(start_battle["p2_pkm_3_atk"]) + "               |\n"
    battle_msg += "-------------------------------------------------------------------------------------\n"
    battle_msg += "|Defense: " + str(start_battle["p2_pkm_1_dfs"]) + "                  |Defense: " + str(start_battle["p2_pkm_2_dfs"]) + "               |Defense: " + str(start_battle["p2_pkm_2_dfs"]) + "              |\n"
    battle_msg += "-------------------------------------------------------------------------------------\n"
    battle_msg += "=====================================================================================\n"
    battle_msg += "|                              +++++ RESULT +++++                                    |\n"
    battle_msg += "=====================================================================================\n"
    battle_msg += "|                        -----------------------------                               |\n"
    battle_msg += "|                                  --Winner--                                        |\n"
    battle_msg += "|                                   Player " + str(start_battle["winner"]) + "                                         |\n"
    battle_msg += "|                        -----------------------------                               |\n"
    battle_msg += "|                                  --Rounds--                                        |\n"
    battle_msg += "|                                      " + str(start_battle["rounds"]) + "                                            |\n"
    battle_msg += "|                        -----------------------------                               |\n"
    battle_msg += "|                          --First pokemon to fall--                                 |\n"
    battle_msg += "|                              " + start_battle["loser_pokemon"] + "                                    |\n"
    battle_msg += "=====================================================================================\n"

    if os.path.exists(f"{idnumber}_battle.txt"):
        
        choice = input(f"Files {idnumber}_battle.txt already exists, what do you prefer to do? [append|OVERWRITE] : ")
        
        if choice == 'o' or choice == 'O' or choice == 'Overwrite' or choice == 'overwrite' or choice == 'OVERWRITE':
           
            os.remove(f"{idnumber}_battle.txt")
            
            with open(f"{idnumber}_battle.txt", "w") as target:
                target.write(battle_msg)
        elif choice == 'a' or choice == 'A' or choice == 'Append' or choice == 'append' or choice == 'APPEND':
           
            with open(f"{idnumber}_battle.txt", "a") as target:
                target.write(battle_msg)  
    else:
        
        with open(f"{idnumber}_battle.txt", "w") as target:
            target.write(battle_msg)
    
    print(battle_msg.format(**start_battle))
    
     
    

    
                  
def client_helper():
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

def client_usage():
    client_usage_msg = """
    CLI usage:
    
        > python3 pokedex_crud.py --help
        > python3 pokedex_crud.py --player1 pokemons_1.json --trivia  --id 1
        > python3 pokedex_crud.py --player1 pokemons_1.json --player2 pokemons_2.json --id 1 --info
        > python3 pokedex_crud.py --player1 pokemons_1.json --player2 pokemons_2.json --id 1 --battle
        
        ATENTION:
        
        Where you read <pokemons_1.json> or <pokemons_2.json> 
        You can use the file format that best suits your needs:
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
            
    elif len(sys.argv) > 8:
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
            if len(sys.argv) >= 7:
                print(f"WARNING! Incorrect amount of arguments.\n{client_usage()}")
                quit()
            
            
            
            if '.json' in filepath_1:    
                data_1 = read_file_json(filepath_1)
            elif '.csv' in filepath_1:    
                data_1 = read_file_csv(filepath_1)
            elif '.xml' in filepath_1:    
                data_1 = read_file_xml(filepath_1)
            elif '.yaml' in filepath_1:    
                data_1 = read_file_yaml(filepath_1)
            else:
                print("Error: File format not supported! ")
            
            if len(sys.argv) == 6:
                idnumber = sys.argv[5]
            else:
                idnumber = 0
            info = process_trivia(data_1)
            show_trivia(info,idnumber)
            quit()
            
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
            
        command3 = sys.argv[5]
        
        if command3 == "--id":
        
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
            
            idnumber = sys.argv[6]
            command4 = sys.argv[7]     

            if command4 == "--info":   
                info = process_info(data_1,data_2,dataset_1,dataset_2)
                show_info(info,idnumber)
                
            elif command4 == "--battle":
                battle = select_pokemons_for_battle(data_1,data_2)
                show_battle_winner(battle,idnumber)
        else:
        
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
            
            idnumber = 0
        
            if command3 == "--info":   
                info = process_info(data_1,data_2,dataset_1,dataset_2)
                show_info(info,idnumber)
                
            elif command3 == "--battle":
                battle = select_pokemons_for_battle(data_1,data_2)
                show_battle_winner(battle,idnumber)    
    else:
        print(f"WARNING: This command does not exist.\n{client_usage()}")
        quit()
       
if __name__ == "__main__":
    main()      
                