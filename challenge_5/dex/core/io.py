import os
import core
from datetime import datetime
from typing import List, Set, SupportsIndex, Dict




def client_helper() -> str:
    
    """
    This function receives data in any python types
    and turns into a set.

    Parameters
    ----------
    file_set_1:
        The data to be converted in set.

    Returns
    -------
    pokemon_set:
        The data in a set type.
    """
    
    helper_msg: str = """
    Hello! Welcome to the Pokedex.

    Here you can choose between the following options, that are:

    --trivia

    If you choose trivia we'll show you some interesting  information
    about the pokemon list you provided, notice that this option only
    works with one file at time, so inform just one list for each time
    you use this option.

    For the next two options notice that we'll need two players,
    and each player will need to provide a list, since the
    functions work with comparisons:

    --info

    We'll show you some comparative information about the two players
    pokemon lists.

    --battle

    The two players will challenge each other, using their three strongest
    pokemon, where the first pokemon to fall decides the winner, and we'll
    show you the battle information.

    """
    return helper_msg


def client_usage() -> str:
    
    """
    This function receives data in any python types
    and turns into a set.

    Parameters
    ----------
    file_set_1:
        The data to be converted in set.

    Returns
    -------
    pokemon_set:
        The data in a set type.
    """
        
    client_usage_msg: str = """
    CLI usage:

    > python3 main.py --help
    > python3 pokedex/main.py --player1 pokemons_1.json --trivia  --id 1
    > python3 pokedex/main.py --player1 pokemons_1.json --player2 pokemons_2.json --id 1 --info
    > python3 pokedex/main.py --player1 pokemons_1.json --player2 pokemons_2.json --id 1 --battle

    ATTENTION:

    Where you read <pokemons_1.json> or <pokemons_2.json>
    Notice that both lists don't need to be in the same format, here you
    can use more than one file format at the same time, like a json and a
    csv list at the same time, it will work as well.
    You can use the formats that best suits your needs:
    Example --> pokemons_1.json  pokemons_2.json
                    pokemons_1.csv   pokemons_2.csv
                    pokemons_1.xml   pokemons_2.xml
                    pokemons_1.yaml  pokemons_2.yaml

    For all options you'll need to inform an id so the function can
    save the log in a text file, if you don't inform any id number it
    will be automatically set as 0. The id is a key name to make the file
    unique, making it possible have multiple files with different data
    across them.

    Before using the function you can choose what will be done with the
    information generated, answering the question that will be displayed:

    What do you prefer to do?

    [append|OVERWRITE]

    append -> This function will increment the file, keeping the
    information that already exists on the file and simply add
    the new one, to choose this type any of this:

    'a','A','Append','append','APPEND'

    OVERWRITE -> This option will delete the existing file and
    create a new one with the generated information, to choose
    this type any of this:

    'o','O','Overwrite','overwrite','OVERWRITE'.

    WARNING: If you don't choose an option, and just hit enter
    it will automatically use OVERWRITE option.
    """
    return client_usage_msg

def save_data(saved_data,archive_type,id_number):
    
    """
    This function receives data in any python types
    and turns into a set.

    Parameters
    ----------
    file_set_1:
        The data to be converted in set.

    Returns
    -------
    pokemon_set:
        The data in a set type.
    """
        
    if os.path.exists(f"{id_number}_{archive_type}.txt"):

        user_choice = input(\
            f"Files {id_number}_{archive_type}.txt already exists, " \
            + "what do you prefer to do? [append|OVERWRITE] : ")

        if user_choice.lower() == 'o' or user_choice.lower() == 'overwrite':

            os.remove(f"{id_number}_{archive_type}.txt")
            
            print("File Overwritten successfully!")

            with open(f"{id_number}_{archive_type}.txt", "w") as target:
                target.write(saved_data)
                
        elif user_choice.lower() == 'a' or user_choice.lower() == 'append':

            with open(f"{id_number}_{archive_type}.txt", "a") as target:
                target.write(saved_data)
                print("New entry added to the file successfully!")
        else:
            print(f"WARNING: Invalid Input.\n{client_usage()}")
            quit()

    else:

        with open(f"{id_number}_{archive_type}.txt", "w") as target:
            target.write(saved_data)

def show_trivia(pokemons_info, id_number):
    """
    This function will print a message in the CLI.

    Parameters
    ----------
    pokemons_info:
        Bring the treated variables which will be used to answer
        the questions

    Returns
    -------
        Create a file with a id value in the name and print the
        same message from the file in the CLI interface.
    """
    datenow = datetime.now()
    msg =  ((" " * 80) + "\n")
    msg += "reported generated on: " + datenow.isoformat() + (" " * 31  ) + "\n"
    msg += ((" " * 80) + "\n")
    msg += (("=" * 29) + " Welcome to the Dex! " + ("=" * 30) + "\n")
    msg += ((" " * 80) + "\n")    
    msg += "Here we have some useful information gathered from the list you provided us:    \n"
    msg += ((" " * 80) + "\n")
    msg += "1. How many pokemons there is in this list:" + (" " * 37) + "\n"
    msg += (" " * 4) + "> " + pokemons_info["total_trivia"] + " pokemons" + \
        (" " * (25 - len(pokemons_info["total_trivia"]))) + "\n"
    msg += ((" " * 80) + "\n")
    msg += "2. The pokemon with the highest HP point is:" + (" " * 36) + "\n"
    msg += (" " * 4) + ">" + pokemons_info["hp_trivia_name"] + " with " + pokemons_info["hp_trivia_points"] + \
        " HP points" + (" " * ((59 - len(pokemons_info["hp_trivia_name"])) - \
        len(pokemons_info["hp_trivia_points"]))) + "\n"
    msg += ((" " * 80) + "\n")
    msg += "3. Which one has the strongest attack:" + (" " * 42) + "\n"
    msg += (" " * 4) + ">" + pokemons_info["atk_trivia_name"] + " with " + \
        pokemons_info["atk_trivia_points"] + " attack points." + \
        (" " * ((54 - len(pokemons_info["atk_trivia_name"])) - \
        len(pokemons_info["atk_trivia_points"]))) + "\n"
    msg += ((" " * 80) + "\n")
    msg += "4. Which one has the strongest defense:" + (" " * 41) + "\n"
    msg += (" " * 4) + ">" + pokemons_info["def_trivia_name"] + " with " + \
        pokemons_info["def_trivia_points"] + " defense points." + \
        (" " * ((53 - len(pokemons_info["def_trivia_name"])) - \
        len(pokemons_info["def_trivia_points"]))) + "\n"
    msg += ((" " * 80) + "\n")
    msg += "5. Which one is the fastest:" + (" " * 52) + "\n"
    msg += (" " * 4) + ">" + pokemons_info["spd_trivia_name"] + " with " + \
        pokemons_info["spd_trivia_points"] + " speed points." + \
        (" " * ((55 - len(pokemons_info["spd_trivia_name"])) - \
        len(pokemons_info["spd_trivia_points"]))) + "\n"
    msg += ((" " * 80) + "\n")
    msg += "Thanks for using this pokedex!" + (" " * 50) + "\n"
    msg += ((" " * 80) + "\n")    
    msg += (("=" * 80) + "\n")
    msg += ((" " * 80) + "\n")
    
    print(msg.format(**pokemons_info))
    
    save_data(msg,"trivia",id_number)

# TODO: control the column width
# TODO: improve how we code the visualization
def show_battle_winner(battle_result, id_number):
    datenow =  datetime.now()
    battle_msg =  ((" " * 80) + "\n")
    battle_msg += "reported generated on:   " + datenow.isoformat() + (" " * 31  ) + "\n"
    battle_msg += ((" " * 80) + "\n")
    battle_msg += "" + (("=" * 32) + " POKéMON BATTLE " + ("=" * 32) + "\n")
    battle_msg += ((" " * 80) + "\n")
    battle_msg += " " + ("-" * 78) + " \n"
    battle_msg += "|" + (" " * 35) + "PLAYER 1" + (" " * 35) + "|\n"
    battle_msg += " " + ("-" * 78) + " \n"
    battle_msg += "|Name:" + battle_result["p1_pkm_1_name"] + (" " * (21 - len(battle_result["p1_pkm_1_name"]))) + \
        "|Name:" + battle_result["p1_pkm_2_name"] + (" " * (20 - len(battle_result["p1_pkm_2_name"]))) + "|Name:" + \
        battle_result["p1_pkm_3_name"] + (" " * (20 - len(battle_result["p1_pkm_3_name"]))) + "|\n"
    battle_msg += "|HP: " + str(battle_result["p1_pkm_1_hp"]) + "                      |HP: " + str(battle_result["p1_pkm_2_hp"]) + "                     |HP: " + str(battle_result["p1_pkm_3_hp"]) + "                    |\n"
    battle_msg += "|Attack: " + str(battle_result["p1_pkm_1_atk"]) + "                  |Attack: " + str(battle_result["p1_pkm_2_atk"]) + "                |Attack: " + str(battle_result["p1_pkm_3_atk"]) + "               |\n"
    battle_msg += "|Defense: " + str(battle_result["p1_pkm_1_dfs"]) + "                 |Defense: " + str(battle_result["p1_pkm_2_dfs"]) + "                |Defense: " + str(battle_result["p1_pkm_2_dfs"]) + "               |\n"
    battle_msg += "-------------------------------------------------------------------------------------\n"
    battle_msg += "|                                    PLAYER 2                                        |\n"
    battle_msg += "-------------------------------------------------------------------------------------\n"
    battle_msg += "|Name:" + battle_result["p2_pkm_1_name"] + "      |Name:" + battle_result["p2_pkm_2_name"] + "    |Name:" + battle_result["p2_pkm_3_name"] + "|\n"
    battle_msg += "|HP: " + str(battle_result["p2_pkm_1_hp"]) + "                       |HP: " + str(battle_result["p2_pkm_2_hp"]) + "                    |HP: " + str(battle_result["p2_pkm_3_hp"]) + "                    |\n"
    battle_msg += "|Attack: " + str(battle_result["p2_pkm_1_atk"]) + "                  |Attack: " + str(battle_result["p2_pkm_2_atk"]) + "                |Attack: " + str(battle_result["p2_pkm_3_atk"]) + "               |\n"
    battle_msg += "|Defense: " + str(battle_result["p2_pkm_1_dfs"]) + "                  |Defense: " + str(battle_result["p2_pkm_2_dfs"]) + "               |Defense: " + str(battle_result["p2_pkm_2_dfs"]) + "              |\n"
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
    
    print(battle_msg.format(**battle_result))
    
    save_data(battle_msg,"battle",id_number)
    
def show_info(process_pokemons, id_number):
    
    datenow = datetime.now()
    msg =  ((" " * 80) + "\n")
    msg += "reported generated on: " + datenow.isoformat() + (" " * 31  ) + "\n"
    msg += " " +(("=" * 32) + " POKEMON INFO " + ("=" * 32) + " \n")
    msg += "|" + (" " * 18) + "| PLAYER 1" + (" " * 20) + "| PLAYER 2" + (" " * 20) + "|\n"
    msg += "|" + ("-" * 18) + "|" + ("-" * 29) + "|" + ("-" * 29) + "|\n"
    msg += "|Pokémons" + (" " * 10) + "| " + process_pokemons["player1_total_pokemons_info"] + \
        (" " * (28 - len(process_pokemons["player1_total_pokemons_info"]))) +  "| " + \
        process_pokemons["player2_total_pokemons_info"] + \
        (" " * (28 - len(process_pokemons["player1_total_pokemons_info"]))) + "|\n"
    msg += "|Strongest Pokémon" + " | " + process_pokemons["strongest_pokemon_player1_info"] + \
        (" " * (28 - len(process_pokemons["strongest_pokemon_player1_info"]))) +  "| " + \
        process_pokemons["strongest_pokemon_player2_info"] + \
        (" " * (28 - len(process_pokemons["strongest_pokemon_player2_info"]))) + "|\n"
    msg += "|Legendaries" + (" " * 7) + "| " + process_pokemons["legendary_player1_info"] + \
        (" " * (28 - len(process_pokemons["legendary_player1_info"]))) +  \
        "| " + process_pokemons["legendary_player2_info"] + \
        (" " * (28 - len(process_pokemons["legendary_player2_info"]))) +  "|\n"
    msg += "|Repeated Pokemons" + " | " + process_pokemons["repeated_pokemon_info"] + \
        (" " * (58 - len(process_pokemons["repeated_pokemon_info"]))) +  "|\n"
    msg += "|Different Pokemons" + "| " + process_pokemons["different_pokemon_info"] + \
        (" " * (58 - len(process_pokemons["different_pokemon_info"]))) +  "|\n"
    msg += "|" + ("-" * 18) + "|" + ("-" * 59) + "|\n"
    msg += " " + (("=" * 78) + " \n")
    msg += ((" " * 80) + "\n")

    print(msg.format(**process_pokemons))
    
    save_data(msg,"info",id_number)
    
    
