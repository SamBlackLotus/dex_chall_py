import core
import os
from datetime import datetime


def process_info(process_poke1, process_poke2, pokemon_set_1, pokemon_set_2):

    strongest_p1 = {"index": 0, "value": 0}
    strongest_p2 = {"index": 0, "value": 0}
    legendary_1 = 0
    legendary_2 = 0
    total_legendary_player1 = 0
    total_legendary_player2 = 0
    intersec_pokemon = (pokemon_set_1.intersection(pokemon_set_2))
    diff_pokemon = (pokemon_set_1.difference(pokemon_set_2))

    for index, pokemon in enumerate(process_poke1):
        player1_total_pokemons = len(process_poke1)

        attack = core.cast_to_int(pokemon["Attack"])
        if attack > strongest_p1["value"]:
            strongest_p1["index"] = index
            strongest_p1["value"] = attack

        legendary_1 = core.cast_to_bool(pokemon["Legendary"])
        # TODO: there is no need to check for True
        if legendary_1 is True:
            total_legendary_player1 += 1

    for index, pokemon in enumerate(process_poke2):
        player2_total_pokemons = len(process_poke2)

        attack = core.cast_to_int(pokemon["Attack"])
        if attack > strongest_p2["value"]:
            strongest_p2["index"] = index
            strongest_p2["value"] = attack

        legendary_2 = core.cast_to_bool(pokemon["Legendary"])
        if legendary_2 is True:
            total_legendary_player2 += 1

    return core.AnswersInfo(

        p1_total_info = str(player1_total_pokemons),
        p2_total_info = str(player2_total_pokemons),
        strongest_p1_info = process_poke1[strongest_p1["index"]]["Name"],
        strongest_p2_info = process_poke2[strongest_p2["index"]]["Name"],
        legendary_p1_info = str(total_legendary_player1),
        legendary_p2_info = str(total_legendary_player2),
        repeated_pokemon_info = str(len(intersec_pokemon)),
        different_pokemon_info = str(len(diff_pokemon)))


def show_info(process_pokemons, id_number):
    
    datenow = datetime.now()
    msg =  ((" " * 70) + "\n")
    msg += "reported generated on:   " + datenow.isoformat() + "                                                  \n"
    msg += " " +(("=" * 35 - len(" POKEMON INFO ")) + " POKEMON INFO " + ("=" * 35 - len(" POKEMON INFO ")) + " \n")
    msg += "|" + (" " * 18) + "| PLAYER 1" + (" " * 16) + "| PLAYER 2" + (" " * 16) + "|\n"
    msg += "|" + ("-" * 18) + "| " + ("-" * 24) + "|" + ("-" * 25) + "|\n"
    msg += "|Pokémons" + (" " * 10) + "| " + process_pokemons["p1_total_info"] + (" " * (24 - len(process_pokemons["p1_total_info"]))) +  "| " + process_pokemons["p2_total_info"] + (" " * (24 - len(process_pokemons["p1_total_info"]))) + "|\n"
    msg += "|Strongest Pokémon" + " | " + process_pokemons["strongest_p1_info"] + (" " * (24 - len(process_pokemons["strongest_p1_info"]))) +  "| " + process_pokemons["strongest_p2_info"] + (" " * (24 - len(process_pokemons["strongest_p2_info"]))) + "|\n"
    msg += "|Legendaries" + (" " * 7) + "| " + process_pokemons["legendary_p1_info"] + "                   | " + process_pokemons["legendary_p2_info"] + "                   |\n"
    msg += "|Repeated Pokemons" + " | " + process_pokemons["repeated_pokemon_info"] + "                                        |\n"
    msg += "|Different Pokemons" + "| " + process_pokemons["different_pokemon_info"] + "                                        |\n"
    msg += "|------------------|---------------------------------------------------|\n"
    msg += " " + (("=" * 70) + " \n")(" " * (24 - len(process_pokemons["strongest_p1_info"])))
    msg += ((" " * 72) + "\n")

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