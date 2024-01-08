import core

def pokemon_trivia(pokemons_data):
    """
        This function will process some validations in a pokemon
        list, to find some specific information and answer the
        given questions.

    Parameters
    ----------
    pokemons_data:
        The pokemon list as a dict type.

    Returns
    -------
    AnswerTrivia:
        Returns the results for the asked validations and puts
        then in variables so it can the called to be presented 
        to the user. 
         
    """
    highest_hp_trivia = {"index": 0, "value": 0}
    highest_attack_trivia = {"index": 0, "value": 0}
    highest_defense_trivia = {"index": 0, "value": 0}
    highest_speed_trivia = {"index": 0, "value": 0}
    for index, pokemon in enumerate(pokemons_data):

        hp_trivia_int = core.cast_to_int(pokemon["hp"])
        if hp_trivia_int > highest_hp_trivia["value"]:
            highest_hp_trivia["index"] = index
            highest_hp_trivia["value"] = hp_trivia_int

        attack_trivia_int = core.cast_to_int(pokemon["attack"])
        if attack_trivia_int > highest_attack_trivia["value"]:
            highest_attack_trivia["index"] = index
            highest_attack_trivia["value"] = attack_trivia_int

        defense_trivia_int = core.cast_to_int(pokemon["defense"])
        if defense_trivia_int > highest_defense_trivia["value"]:
            highest_defense_trivia["index"] = index
            highest_defense_trivia["value"] = defense_trivia_int

        speed_trivia_int = core.cast_to_int(pokemon["attack"])
        if speed_trivia_int > highest_speed_trivia["value"]:
            highest_speed_trivia["index"] = index
            highest_speed_trivia["value"] = speed_trivia_int

    return core.AnswersTrivia(
        total_trivia= str(len(pokemons_data)),
        hp_trivia_name= pokemons_data[highest_hp_trivia["index"]]["name"],
        hp_trivia_points= str(pokemons_data[highest_hp_trivia["index"]]["hp"]),
        atk_trivia_name= pokemons_data[highest_attack_trivia["index"]]["name"],
        atk_trivia_points= str(pokemons_data[highest_attack_trivia["index"]]["attack"]),
        def_trivia_name= pokemons_data[highest_attack_trivia["index"]]["name"],
        def_trivia_points= str(pokemons_data[highest_attack_trivia["index"]]["defense"]),
        spd_trivia_name= pokemons_data[highest_attack_trivia["index"]]["name"],
        spd_trivia_points= str(pokemons_data[highest_attack_trivia["index"]]["speed"])
    )
    
def digimon_trivia(digimon_data):
    """
        This function will process some validations in a digimon
        list, to find some specific information and answer the
        given questions.

    Parameters
    ----------
    digimon_data:
        The digimon list as a dict type.

    Returns
    -------
    AnswerTrivia:
        Returns the results for the asked validations and puts
        then in variables so it can the called to be presented 
        to the user. 
         
    """
    highest_attack_trivia = {"index": 0, "value": 0}
    lowest_attack_trivia = {"index": 0, "value": 1000}
    baby_dict = []
    rookie_dict = []
    champion_dict = []
    ultimate_dict = []
    mega_dict = []
    baby_digimon = 0
    rookie_digimon = 0
    champion_digimon = 0
    ultimate_digimon = 0
    mega_digimon = 0
    data_type = 0
    vaccine_type = 0
    virus_type = 0
    free_type = 0
    baby_strongest = {"index": 0, "value":0}
    rookie_strongest = {"index": 0, "value":0}
    champion_strongest = {"index": 0, "value":0}
    ultimate_strongest = {"index": 0, "value":0}
    mega_strongest = {"index": 0, "value":0}
    digimon_types = []
    
    for index, digimon in enumerate(digimon_data):
        highest_attack = core.cast_to_int(digimon["attack"])
        if highest_attack > highest_attack_trivia["value"]:
            highest_attack_trivia["index"] = index
            highest_attack_trivia["value"] = highest_attack
        
        lowest_attack = core.cast_to_int(digimon["attack"])
        if lowest_attack < lowest_attack_trivia["value"]:
            lowest_attack_trivia["index"] = index
            lowest_attack_trivia["value"] = lowest_attack
         
        if digimon["stage"] == "Baby":
            baby_digimon += 1
            baby_dict += [{key_list: value_list for key_list, value_list in digimon.items()}]
            
        elif digimon["stage"] == "Rookie":
            rookie_digimon += 1
            rookie_dict += [{key_list: value_list for key_list, value_list in digimon.items()}]

        elif digimon["stage"] == "Champion":
            champion_digimon += 1
            champion_dict += [{key_list: value_list for key_list, value_list in digimon.items()}]
            
        elif digimon["stage"] == "Ultimate":
            ultimate_digimon += 1
            ultimate_dict += [{key_list: value_list for key_list, value_list in digimon.items()}]
            
        elif digimon["stage"] == "Mega":
            mega_digimon += 1
            mega_dict += [{key_list: value_list for key_list, value_list in digimon.items()}]

        if digimon["type1"] == "Data":
            data_type += 1
        elif digimon["type1"] == "Vaccine":
            vaccine_type += 1
        elif digimon["type1"] == "Virus":
            virus_type += 1
        elif digimon["type1"] == "Free":
            free_type += 1
            
        if "Data" in digimon["type1"] ==:
            digimon_types.append("Data")
        elif "Vaccine" in digimon["type1"]:
            digimon_types.append("Vaccine")
        elif "Virus" in digimon["type1"]:
            digimon_types.append("Virus")
        elif "Free" in digimon["type1"]:
            digimon_types.append("Free")
    print(digimon_types )       
    baby_sorted = sorted(baby_dict, key = lambda strongest: strongest["attack"], reverse = True)
    baby_strongest = baby_sorted[0]
    rookie_sorted = sorted(rookie_dict, key = lambda strongest: strongest["attack"], reverse = True)
    rookie_strongest = rookie_sorted[0]
    champion_sorted = sorted(champion_dict, key = lambda strongest: strongest["attack"], reverse = True)
    champion_strongest = champion_sorted[0]
    ultimate_sorted = sorted(ultimate_dict, key = lambda strongest: strongest["attack"], reverse = True)
    ultimate_strongest = ultimate_sorted[0]
    mega_sorted = sorted(mega_dict, key = lambda strongest: strongest["attack"], reverse = True)
    mega_strongest = mega_sorted[0]

    return core.AnswersTrivia(
        total_trivia = str(len(digimon_data)),
        highest_atk_name= digimon_data[highest_attack_trivia["index"]]["name"],
        highest_atk_stage= digimon_data[highest_attack_trivia["index"]]["stage"],
        highest_atk_type= digimon_data[highest_attack_trivia["index"]]["type1"],
        lowest_atk_name= digimon_data[lowest_attack_trivia["index"]]["name"],
        lowest_atk_stage= digimon_data[lowest_attack_trivia["index"]]["stage"],
        lowest_atk_type= digimon_data[lowest_attack_trivia["index"]]["type1"],
        total_baby = str(baby_digimon),
        total_rookie = str(rookie_digimon),
        total_champion = str(champion_digimon),
        total_ultimate = str(ultimate_digimon),
        total_mega = str(mega_digimon),
        total_data = str(data_type),
        total_vaccine = str(vaccine_type),
        total_virus = str(virus_type),
        total_free = str(free_type),
        baby_strongest = baby_strongest["name"],
        rookie_strongest = rookie_strongest["name"],
        champion_strongest = champion_strongest["name"],
        ultimate_strongest = ultimate_strongest["name"],
        mega_strongest = mega_strongest["name"],
    )

