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
        total_trivia= str(len(pokemons_data)),
        hp_trivia_name= pokemons_data[highest_hp_trivia["index"]]["Name"],
        hp_trivia_points= str(pokemons_data[highest_hp_trivia["index"]]["HP"]),
        atk_trivia_name= pokemons_data[highest_attack_trivia["index"]]["Name"],
        atk_trivia_points= str(pokemons_data[highest_attack_trivia["index"]]["Attack"]),
        def_trivia_name= pokemons_data[highest_attack_trivia["index"]]["Name"],
        def_trivia_points= str(pokemons_data[highest_attack_trivia["index"]]["Defense"]),
        spd_trivia_name= pokemons_data[highest_attack_trivia["index"]]["Name"],
        spd_trivia_points= str(pokemons_data[highest_attack_trivia["index"]]["Speed"])
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

        hp_trivia_int = core.cast_to_int(digimon["HP"])
        if hp_trivia_int > highest_hp_trivia["value"]:
            highest_hp_trivia["index"] = index
            highest_hp_trivia["value"] = hp_trivia_int

        attack_trivia_int = core.cast_to_int(digimon["Attack"])
        if attack_trivia_int > highest_attack_trivia["value"]:
            highest_attack_trivia["index"] = index
            highest_attack_trivia["value"] = attack_trivia_int

        defense_trivia_int = core.cast_to_int(digimon["Defense"])
        if defense_trivia_int > highest_defense_trivia["value"]:
            highest_defense_trivia["index"] = index
            highest_defense_trivia["value"] = defense_trivia_int

        speed_trivia_int = core.cast_to_int(digimon["Attack"])
        if speed_trivia_int > highest_speed_trivia["value"]:
            highest_speed_trivia["index"] = index
            highest_speed_trivia["value"] = speed_trivia_int

    return core.AnswersTrivia(
        total_trivia_dg = str(len(digimon_data)),
    )    

