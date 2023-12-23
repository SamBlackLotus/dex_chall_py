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

        player1_total_pokemons_info=player1_total_pokemons,
        player2_total_pokemons_info=player2_total_pokemons,
        strongest_pokemon_player1_info=process_poke1[strongest_pokemon_player1["index"]]["Name"],
        strongest_pokemon_player2_info=process_poke2[strongest_pokemon_player2["index"]]["Name"],
        legendary_player1_info=total_legendary_player1,
        legendary_player2_info=total_legendary_player2,
        repeated_pokemon_info=len(intersec_pokemon),
        different_pokemon_info=len(diff_pokemon))


def show_info(process_pokemons, id_number):

    datenow = datetime.now()
    msg = "                                                                  \n"
    msg += "reported generated on:   " + datenow.isoformat() + "                                                  \n"
    msg += "========================= POKEMON INFO ==========================\n"
    msg += "|                   | PLAYER 1            | PLAYER 2            |\n"
    msg += "|------------------ | -------------------- -------------------- |\n"
    msg += "|Pokémons           |" + str(process_pokemons["player1_total_pokemons_info"]) + "                  |" + str(process_pokemons["player2_total_pokemons_info"]) + "                  |\n"
    msg += "|Strongest Pokémon  |" + process_pokemons["strongest_pokemon_player1_info"] + "|" + process_pokemons["strongest_pokemon_player2_info"] + "   |\n"
    msg += "|Legendaries        |" + str(process_pokemons["legendary_player1_info"]) + "                   |" + str(process_pokemons["legendary_player2_info"]) + "                   |\n"
    msg += "|Repeated Pokemons  |" + str(process_pokemons["repeated_pokemon_info"]) + "                                        |\n"
    msg += "|Different Pokemons |" + str(process_pokemons["different_pokemon_info"]) + "                                        |\n"
    msg += "|------------------ | ----------------------------------------- |\n"
    msg += "=================================================================\n"
    msg += "                                                                 \n"

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
