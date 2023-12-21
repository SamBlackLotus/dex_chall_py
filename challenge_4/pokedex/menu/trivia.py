import core
import os
from datetime import datetime

#Process and generate the answers to the trivia questions    
def process_trivia(pokemons_data):
    highest_hp_trivia = {"index":0, "value":0}
    highest_atk_trivia = {"index": 0, "value": 0}
    highest_def_trivia = {"index": 0, "value": 0}
    highest_spd_trivia = {"index": 0, "value": 0}
    for index, pokemon in enumerate(pokemons_data):

        hp_trivia_int = core.cast_to_int(pokemon["HP"])
        if hp_trivia_int > highest_hp_trivia["value"]:
            highest_hp_trivia["index"] = index
            highest_hp_trivia["value"] = hp_trivia_int
      
        attack_trivia_int = core.cast_to_int(pokemon["Attack"])
        if attack_trivia_int > highest_atk_trivia["value"]:
            highest_atk_trivia["index"] = index
            highest_atk_trivia["value"] = attack_trivia_int
            
        defense_trivia_int = core.cast_to_int(pokemon["Defense"])
        if defense_trivia_int > highest_def_trivia["value"]:
            highest_def_trivia["index"] = index
            highest_def_trivia["value"] = defense_trivia_int
      
        speed_trivia_int = core.cast_to_int(pokemon["Attack"])
        if speed_trivia_int > highest_spd_trivia["value"]:
            highest_spd_trivia["index"] = index
            highest_spd_trivia["value"] = speed_trivia_int    

    return core.Answers(
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
    
    if os.path.exists(f"{idnumber}_trivia.txt"):
        
        choice = input(f"Files {idnumber}_trivia.txt already exists, what do you prefer to do? [append|OVERWRITE] : ")
        print(len(choice))
        if choice == 'o' or choice == 'O' or choice == 'Overwrite' or choice == 'overwrite' or choice == 'OVERWRITE' or choice == '':
           
            os.remove(f"{idnumber}_trivia.txt")
            
            with open(f"{idnumber}_trivia.txt", "w") as target:
                target.write(msg)
                
        elif choice == 'a' or choice == 'A' or choice == 'Append' or choice == 'append' or choice == 'APPEND':
           
            with open(f"{idnumber}_trivia.txt", "a") as target:
                target.write(msg)
        else:
            print(f"WARNING: Invalid Input.\n{core.client_usage()}")
            quit()
              
    else:
        
        with open(f"{idnumber}_trivia.txt", "w") as target:
            target.write(msg)
    
    print(msg.format(**pokemons_info))