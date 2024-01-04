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
    pokemons_data:
        The digimon list as a dict type.

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
    for index, digimon in enumerate(digimon_data):

        hp_trivia_int = core.cast_to_int(digimon["hp"])
        if hp_trivia_int > highest_hp_trivia["value"]:
            highest_hp_trivia["index"] = index
            highest_hp_trivia["value"] = hp_trivia_int

        attack_trivia_int = core.cast_to_int(digimon["attack"])
        if attack_trivia_int > highest_attack_trivia["value"]:
            highest_attack_trivia["index"] = index
            highest_attack_trivia["value"] = attack_trivia_int

        defense_trivia_int = core.cast_to_int(digimon["defense"])
        if defense_trivia_int > highest_defense_trivia["value"]:
            highest_defense_trivia["index"] = index
            highest_defense_trivia["value"] = defense_trivia_int

        speed_trivia_int = core.cast_to_int(digimon["attack"])
        if speed_trivia_int > highest_speed_trivia["value"]:
            highest_speed_trivia["index"] = index
            highest_speed_trivia["value"] = speed_trivia_int

    return core.AnswersTrivia(
        total_trivia_dg = str(len(digimon_data)),
    )    

