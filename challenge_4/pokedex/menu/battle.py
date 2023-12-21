import core
import os
from datetime import datetime

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
    
    for index, pokemon in enumerate(player_1_battle):
        
        name = pokemon["Name"]
        attack = core.cast_to_int(pokemon["Attack"])
        defense = core.cast_to_int(pokemon["Defense"])
        hp = core.cast_to_int(pokemon["HP"])
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
        attack = core.cast_to_int(pokemon["Attack"])
        defense = core.cast_to_int(pokemon["Defense"])
        hp = core.cast_to_int(pokemon["HP"])
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
    
    return core.AnswersBattle(
        
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
        
        p1_player = p1_pokemon_1["player"],
        p2_player = p2_pokemon_1["player"]
        
    )           
    
def pokemon_battle(start_battle):

    while_counter = 0
    
    p1_pkm_1_hp = core.cast_to_int(start_battle["p1_pkm_1_hp"])
    p1_pkm_2_hp = core.cast_to_int(start_battle["p1_pkm_2_hp"])
    p1_pkm_3_hp = core.cast_to_int(start_battle["p1_pkm_3_hp"])
    p2_pkm_1_hp = core.cast_to_int(start_battle["p2_pkm_1_hp"])
    p2_pkm_2_hp = core.cast_to_int(start_battle["p2_pkm_2_hp"])
    p2_pkm_3_hp = core.cast_to_int(start_battle["p2_pkm_3_hp"])
    
    damagep1poke1 = (0.5 * (core.cast_to_int(start_battle["p1_pkm_1_atk"]) / core.cast_to_int(start_battle["p2_pkm_1_dfs"])) + 1)         
    damagep1poke2 = (0.5 * (core.cast_to_int(start_battle["p1_pkm_2_atk"]) / core.cast_to_int(start_battle["p2_pkm_2_dfs"])) + 1) 
    damagep1poke3 = (0.5 * (core.cast_to_int(start_battle["p1_pkm_3_atk"]) / core.cast_to_int(start_battle["p2_pkm_3_dfs"])) + 1) 
    damagep2poke1 = (0.5 * (core.cast_to_int(start_battle["p2_pkm_1_atk"]) / core.cast_to_int(start_battle["p1_pkm_1_dfs"])) + 1) 
    damagep2poke2 = (0.5 * (core.cast_to_int(start_battle["p2_pkm_2_atk"]) / core.cast_to_int(start_battle["p1_pkm_2_dfs"])) + 1) 
    damagep2poke3 = (0.5 * (core.cast_to_int(start_battle["p2_pkm_3_atk"]) / core.cast_to_int(start_battle["p1_pkm_3_dfs"])) + 1)         

    while True:
        
        while_counter += 1 
        
        p1_pkm_1_hp -= damagep1poke1
        p1_pkm_2_hp -= damagep1poke2
        p1_pkm_3_hp -= damagep1poke3
        p2_pkm_1_hp -= damagep2poke1
        p2_pkm_2_hp -= damagep2poke2
        p2_pkm_3_hp -= damagep2poke3
        
        
        if p1_pkm_1_hp <= 0:
            first_pokemon_dead = start_battle["p1_pkm_1_name"]
            victorious_player = start_battle["p2_player"]
            break
        elif p1_pkm_2_hp <= 0:
            first_pokemon_dead = start_battle["p1_pkm_2_name"]
            victorious_player = start_battle["p2_player"]
            break
        elif p1_pkm_3_hp <= 0:
            first_pokemon_dead = start_battle["p1_pkm_3_name"]
            victorious_player = start_battle["p2_player"]
            break
        elif p2_pkm_1_hp <= 0:
            first_pokemon_dead = start_battle["p2_pkm_1_name"]
            victorious_player = start_battle["p1_player"]
            break
        elif p2_pkm_2_hp <= 0:
            first_pokemon_dead = start_battle["p2_pkm_2_name"]
            victorious_player = start_battle["p1_player"]
            break
        elif p2_pkm_3_hp <= 0:    
            first_pokemon_dead = start_battle["p2_pkm_3_name"]
            victorious_player = start_battle["p1_player"]
            break
    
    return core.AnswersBattle(
        winner = victorious_player,
        rounds = while_counter,
        loser_pokemon = first_pokemon_dead
    )

#Show the information about wich pokemons participated in the battle, and wich player was the winner
# TODO: control the column width
# TODO: remove the line separation between attack and defense for player 2
# TODO: improve how we code the visualization
def show_battle_winner(start_battle,battle_result, id_number):
    datenow =  datetime.now()
    battle_msg =  "                                                                                     \n"
    battle_msg += "reported generated on:   " + datenow.isoformat() + "                                                  \n"
    battle_msg += "                                                                                     \n"
    battle_msg += "================================== POKéMON BATTLE ===================================\n"
    battle_msg += "                                                                                     \n"
    battle_msg += "-------------------------------------------------------------------------------------\n"
    battle_msg += "|                                    PLAYER 1                                        |\n"
    battle_msg += "-------------------------------------------------------------------------------------\n"
    battle_msg += "|Name:" + start_battle["p1_pkm_1_name"] + "   |Name:" + start_battle["p1_pkm_2_name"] + "    |Name:" + start_battle["p1_pkm_3_name"] + "  |\n"
    battle_msg += "|HP: " + str(start_battle["p1_pkm_1_hp"]) + "                      |HP: " + str(start_battle["p1_pkm_2_hp"]) + "                     |HP: " + str(start_battle["p1_pkm_3_hp"]) + "                    |\n"
    battle_msg += "|Attack: " + str(start_battle["p1_pkm_1_atk"]) + "                  |Attack: " + str(start_battle["p1_pkm_2_atk"]) + "                |Attack: " + str(start_battle["p1_pkm_3_atk"]) + "               |\n"
    battle_msg += "|Defense: " + str(start_battle["p1_pkm_1_dfs"]) + "                 |Defense: " + str(start_battle["p1_pkm_2_dfs"]) + "                |Defense: " + str(start_battle["p1_pkm_2_dfs"]) + "               |\n"
    battle_msg += "-------------------------------------------------------------------------------------\n"
    battle_msg += "|                                    PLAYER 2                                        |\n"
    battle_msg += "-------------------------------------------------------------------------------------\n"
    battle_msg += "|Name:" + start_battle["p2_pkm_1_name"] + "      |Name:" + start_battle["p2_pkm_2_name"] + "    |Name:" + start_battle["p2_pkm_3_name"] + "|\n"
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
    battle_msg += "|                                   Player " + str(battle_result["winner"]) + "                                         |\n"
    battle_msg += "|                        -----------------------------                               |\n"
    battle_msg += "|                                  --Rounds--                                        |\n"
    battle_msg += "|                                      " + str(battle_result["rounds"]) + "                                            |\n"
    battle_msg += "|                        -----------------------------                               |\n"
    battle_msg += "|                          --First pokemon to fall--                                 |\n"
    battle_msg += "|                              " + battle_result["loser_pokemon"] + "                                 |\n"
    battle_msg += "=====================================================================================\n"
    battle_msg += "                                                                                     \n"

    if os.path.exists(f"{id_number}_battle.txt"):
        
        user_choice_battle = input(f"Files {id_number}_battle.txt already exists, what do you prefer
                                   to do? [append|OVERWRITE] : ")
        
        # TODO: you could use:
        # if user_choice_battle.lower() == 'o' or user_choice_battle.lower() == 'overwrite'
        if user_choice_battle.lower() == 'o' or user_choice_battle.lower() == 'overwrite':
           
            os.remove(f"{id_number}_battle.txt")
            
            with open(f"{id_number}_battle.txt", "w") as target:
                target.write(battle_msg)
        elif user_choice_battle.lower() == 'a' or user_choice_battle.lower() == 'append':
           
            with open(f"{id_number}_battle.txt", "a") as target:
                target.write(battle_msg)  
        else:
            print(f"WARNING: Invalid Input.\n{core.client_usage()}")
            quit()
              
    else:
        
        with open(f"{id_number}_battle.txt", "w") as target:
            target.write(battle_msg)
    
    print(battle_msg.format(**start_battle))