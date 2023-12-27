import core
import os
from datetime import datetime


def process_info(process_poke1, process_poke2, pokemon_set_1, pokemon_set_2):

    strongest_pokemon_player1 = {"index": 0, "value": 0}
    strongest_pokemon_player2 = {"index": 0, "value": 0}
    legendary_1 = 0
    legendary_2 = 0
    total_legendary_player1 = 0
    total_legendary_player2 = 0
    intersec_pokemon = (pokemon_set_1.intersection(pokemon_set_2))
    diff_pokemon = (pokemon_set_1.difference(pokemon_set_2))

    for index, pokemon in enumerate(process_poke1):
        player1_total_pokemons = len(process_poke1)

        attack = core.cast_to_int(pokemon["Attack"])
        if attack > strongest_pokemon_player1["value"]:
            strongest_pokemon_player1["index"] = index
            strongest_pokemon_player1["value"] = attack

        legendary_1 = core.cast_to_bool(pokemon["Legendary"])
        # TODO: there is no need to check for True
        if legendary_1 is True:
            total_legendary_player1 += 1

    for index, pokemon in enumerate(process_poke2):
        player2_total_pokemons = len(process_poke2)

        attack = core.cast_to_int(pokemon["Attack"])
        if attack > strongest_pokemon_player2["value"]:
            strongest_pokemon_player2["index"] = index
            strongest_pokemon_player2["value"] = attack

        legendary_2 = core.cast_to_bool(pokemon["Legendary"])
        if legendary_2 is True:
            total_legendary_player2 += 1

    return core.AnswersInfo(

        player1_total_pokemons_info = str(player1_total_pokemons),
        player2_total_pokemons_info = str(player2_total_pokemons),
        strongest_pokemon_player1_info = process_poke1[strongest_pokemon_player1["index"]]["Name"],
        strongest_pokemon_player2_info = process_poke2[strongest_pokemon_player2["index"]]["Name"],
        legendary_player1_info = str(total_legendary_player1),
        legendary_player2_info = str(total_legendary_player2),
        repeated_pokemon_info = str(len(intersec_pokemon)),
        different_pokemon_info = str(len(diff_pokemon)))


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

    if os.path.exists(f"{id_number}_info.txt"):

        user_choice_info = input(f"Files {id_number}_info.txt already exists, what do you prefer to do? [append|OVERWRITE] : ")

        if user_choice_info.lower() == 'o' or user_choice_info.lower() == 'overwrite':

            os.remove(f"{id_number}_info.txt")

            with open(f"{id_number}_info.txt", "w") as target:
                target.write(msg)
        elif user_choice_info.lower() == 'a' or user_choice_info.lower() == 'append':

            with open(f"{id_number}_info.txt", "a") as target:
                target.write(msg)
        else:
            print(f"WARNING: Invalid Input.\n{core.client_usage()}")
            quit()

    else:

        with open(f"{id_number}_info.txt", "w") as target:
            target.write(msg)

    print(msg.format(**process_pokemons))