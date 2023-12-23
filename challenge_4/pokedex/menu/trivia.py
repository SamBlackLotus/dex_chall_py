import core
import os
from datetime import datetime


def process_trivia(pokemons_data):
    """
    This function will get the data provided from main 
    and slice the information to transform the data in 
    specific info about the pokemons inside the archive.

    Parameters
    ----------
    pokemons_data:
        Will bring the treated dictionary with the pokemons
        information 

    Returns
    -------
    AnswerTrivia:
        It returns the answers to the trivia questions
    """
    highest_hp_trivia = {"index": 0, "value": 0}
    highest_attack_trivia = {"index": 0, "value": 0}
    highest_defense_trivia = {"index": 0, "value": 0}
    highest_speed_trivia = {"index": 0, "value": 0}
    for index, pokemon in enumerate(pokemons_data):

        hp_trivia_int = core.cast_to_int(pokemon["HP"])
        if hp_trivia_int > highest_hp_trivia["value"]:
            highest_hp_trivia["index"] = index
            highest_hp_trivia["value"] = hp_trivia_int

        attack_trivia_int = core.cast_to_int(pokemon["Attack"])
        if attack_trivia_int > highest_attack_trivia["value"]:
            highest_attack_trivia["index"] = index
            highest_attack_trivia["value"] = attack_trivia_int

        defense_trivia_int = core.cast_to_int(pokemon["Defense"])
        if defense_trivia_int > highest_defense_trivia["value"]:
            highest_defense_trivia["index"] = index
            highest_defense_trivia["value"] = defense_trivia_int

        speed_trivia_int = core.cast_to_int(pokemon["Attack"])
        if speed_trivia_int > highest_speed_trivia["value"]:
            highest_speed_trivia["index"] = index
            highest_speed_trivia["value"] = speed_trivia_int

    return core.AnswersTrivia(
        total_trivia=len(pokemons_data),
        hp_trivia_name=pokemons_data[highest_hp_trivia["index"]]["Name"],
        hp_trivia_points=pokemons_data[highest_hp_trivia["index"]]["HP"],
        atk_trivia_name=pokemons_data[highest_attack_trivia["index"]]["Name"],
        atk_trivia_points=pokemons_data[highest_attack_trivia["index"]]["Attack"],
        def_trivia_name=pokemons_data[highest_attack_trivia["index"]]["Name"],
        def_trivia_points=pokemons_data[highest_attack_trivia["index"]]["Defense"],
        spd_trivia_name=pokemons_data[highest_attack_trivia["index"]]["Name"],
        spd_trivia_points=pokemons_data[highest_attack_trivia["index"]]["Speed"]
    )


# TODO: break into show and write files
# TODO: move to io.py
def show_trivia(pokemons_info, id_number):
    """
    This function will receive the data saved earlier in the
    process_trivia and use them to save a file with the questions 
    and print it too in the CLI interface.

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
    msg =  "                                                                            \n"
    msg += "reported generated on:   " + datenow.isoformat() + "                                                  \n"
    msg += "                                                                           \n"
    msg += "========================= Welcome to the Pokedex! =========================\n"
    msg += "                                                                           \n"
    msg += "        ⣷⣿⣿⣶⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⢠⣴⣶⣷⣿⣿    \n"
    msg += "       ⠀⠹⣿⣿⣿⡄⠀⠈⠓⠦⣄ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠖⠊⠉⠀⣸⣿⣿⣽⠃    \n"
    msg += "       ⠀⠀⠘⣿⣿⣇⠀⠀⠀⠀⠀⠘⠶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⣿⣿⣿⠃     \n"
    msg += "       ⠀⠀⠀⠈⢻⣿ ⠀⠀⠀⠀⠀⠀⠈⠳⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠙⠁⠀⠀⠀⠀⠀⠀⡸⣿⠟⠁⠀⠀    \n"
    msg += "       ⠀⠀⠀⠀⠀⠁⢾⡄⠀⠀⠀⠀⠀⠀⠀⠈⠱⣦⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⣠⠟⠁⠀⠀⠀     \n"
    msg += "       ⠀⠀⠀⠀⠀⠀⠀⠉⠳⡄⠀⠀⠀⠀⠀⠀⠀⠈⠳⡆⣤⠴⠞⠛⠉⠉⠉⠉⠉⠉⠉⠳⠆⣤⣤⠞⠁⠀⠀⠀⠀⠀⠀⢀⣠⠖⠁⠀⠀⠀⠀⠀     \n"
    msg += "       ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠖⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀    \n"
    msg += "       ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢳⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢇⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    \n"
    msg += "       ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    \n"
    msg += "        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠃⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   \n"
    msg += "        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀ ⣠⣶⠖⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠴⠶⣦⡄⠀⠀⢈⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   \n"
    msg += "        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠾ ⠀⠀⢰⣾⣷⣀⣰⡧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣀⣠⣾⣿⠀⠀⠀⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   \n"
    msg += "        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟ ⠀⠀⠈⠻⣍⡩⠜⠃⠀⠀⠀⠠⣤⡤⠀⠀⠀⠀⠹⠭⣉⠽⠏⠀⠀⠀⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   \n"
    msg += "        ⠀⠀⠀⠀⠀⠀⢀⣤⠴⠴⣤⣠⣇⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⣤⣤⣼⣀⡴⢴⢦⣄⠀⠀⠀⠀⠀⠀⠀   \n"
    msg += "        ⠀⠀⠀⠀⠀⠀⢸⠃⠀⠀⠀⠀⢹⡁⣀⡀⠙⣱⡀⠀⠀⠲⣄⣠⡴⣒⢒⣤⣤⠴⠂⠀⠀⠀⢠⡞⢁⣀⡀⢨⠃⠀⠀⠀⠀⢹⠀⠀⠀ ⠀⠀⠀   \n"
    msg += "        ⠀⠀⠀⠀⠀⠀⠈⠉⠀⠉⠀⠈⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠈⠀⠉⠉⠉⠉⠉⠉⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠁⠈⠈⠈⠀⠉⠀⠀⠀⠀ ⠀⠀   \n"
    msg += "                                                                            \n"    
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
    msg += "                                                                            \n"    
    msg += "============================================================================\n"
    msg += "                                                                            \n"

    if os.path.exists(f"{id_number}_trivia.txt"):

        user_choice_trivia = input(f"Files {id_number}_info.txt already exists, what do you prefer to do? [append|OVERWRITE] : ")

        if user_choice_trivia.lower() == 'o' or user_choice_trivia.lower() == 'overwrite':

            os.remove(f"{id_number}_info.txt")

            with open(f"{id_number}_info.txt", "w") as target:
                target.write(msg)
        elif user_choice_trivia.lower() == 'a' or user_choice_trivia.lower() == 'append':

            with open(f"{id_number}_info.txt", "a") as target:
                target.write(msg)
        else:
            print(f"WARNING: Invalid Input.\n{core.client_usage()}")
            quit()

    else:

        with open(f"{id_number}_trivia.txt", "w") as target:
            target.write(msg)

    print(msg.format(**pokemons_info))
