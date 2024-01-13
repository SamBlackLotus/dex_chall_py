import core
from typing import Dict,Union

def pokemon_trivia(pokemons_data: Dict[str, Union[str, int]]) -> Dict[str, str]:
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
        Returns the results for the asked questions and stores
        then in variables.

    """
    highest_hp_trivia = {"index": 0, "value": 0}
    highest_attack_trivia = {"index": 0, "value": 0}
    highest_defense_trivia = {"index": 0, "value": 0}
    highest_speed_trivia = {"index": 0, "value": 0}
    pokemon_dict = []

    for index, pokemon in enumerate(pokemons_data):
        pokemon_dict += [
            {key_list:   value_list for key_list, value_list in pokemon.items()}
        ]

        if pokemon_dict:
            pokemon_hp = sorted(
                pokemon_dict, key=lambda highest: highest["hp"], reverse=True
            )
            highest_hp_trivia = pokemon_hp[0]

            pokemon_attack = sorted(
                pokemon_dict, key=lambda highest: highest["attack"], reverse=True
            )
            highest_attack_trivia = pokemon_attack[0]

            pokemon_defense = sorted(
                pokemon_dict, key=lambda highest: highest["defense"], reverse=True
            )
            highest_defense_trivia = pokemon_defense[0]

            pokemon_speed = sorted(
                pokemon_dict, key=lambda highest: highest["speed"], reverse=True
            )
            highest_speed_trivia = pokemon_speed[0]

    return core.AnswersPokemonTrivia(
        total_trivia=str(len(pokemons_data)),
        hp_trivia_name=highest_hp_trivia["name"],
        hp_trivia_points=str(highest_hp_trivia["hp"]),
        atk_trivia_name=highest_attack_trivia["name"],
        atk_trivia_points=str(highest_attack_trivia["attack"]),
        def_trivia_name=highest_defense_trivia["name"],
        def_trivia_points=str(highest_defense_trivia["defense"]),
        spd_trivia_name=highest_speed_trivia["name"],
        spd_trivia_points=str(highest_speed_trivia["speed"]),
    )


def digimon_trivia(digimon_data: Dict[str, Union[str, int]]) -> Dict[str, str]:
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
        Returns the results for the asked questions and stores
        then in variables.

    """
    highest_attack_trivia = {"index": 0, "value": 0}
    lowest_attack_trivia = {"index": 0, "value": 1000}
    baby_dict = []
    rookie_dict = []
    champion_dict = []
    ultimate_dict = []
    mega_dict = []
    ultra_dict = []
    data_dict = []
    vaccine_dict = []
    virus_dict = []
    free_dict = []
    baby_digimon = 0
    rookie_digimon = 0
    champion_digimon = 0
    ultimate_digimon = 0
    mega_digimon = 0
    ultra_digimon = 0
    data_type = 0
    vaccine_type = 0
    virus_type = 0
    free_type = 0
    baby_strongest = {"index": 0, "value": 0}
    rookie_strongest = {"index": 0, "value": 0}
    champion_strongest = {"index": 0, "value": 0}
    ultimate_strongest = {"index": 0, "value": 0}
    mega_strongest = {"index": 0, "value": 0}
    ultra_strongest = {"index": 0, "value": 0}
    data_strongest = {"index": 0, "value": 0}
    vaccine_strongest = {"index": 0, "value": 0}
    virus_strongest = {"index": 0, "value": 0}
    free_strongest = {"index": 0, "value": 0}
    digimon_types = []
    digimon_stages = []
    digimon_dict = []

    for index, digimon in enumerate(digimon_data):
        digimon_dict += [
            {key_list:   value_list for key_list, value_list in digimon.items()}
        ]

        if digimon_dict:
            digimon_highest_attack = sorted(
                digimon_dict, key=lambda highest: highest["attack"], reverse=True
            )
            highest_attack_trivia = digimon_highest_attack[0]
            
            digimon_lowest_attack = sorted(
                digimon_dict, key=lambda lowest: lowest["attack"]
            )
            lowest_attack_trivia = digimon_lowest_attack[0]

        if digimon["stage"] == "Baby":
            baby_digimon += 1
            baby_dict += [
                {key_list: value_list for key_list, value_list in digimon.items()}
            ]
            if digimon["stage"] not in digimon_stages:
                digimon_stages.append(digimon["stage"])

        elif digimon["stage"] == "Rookie":
            rookie_digimon += 1
            rookie_dict += [
                {key_list: value_list for key_list, value_list in digimon.items()}
            ]
            if digimon["stage"] not in digimon_stages:
                digimon_stages.append(digimon["stage"])

        elif digimon["stage"] == "Champion":
            champion_digimon += 1
            champion_dict += [
                {key_list: value_list for key_list, value_list in digimon.items()}
            ]
            if digimon["stage"] not in digimon_stages:
                digimon_stages.append(digimon["stage"])

        elif digimon["stage"] == "Ultimate":
            ultimate_digimon += 1
            ultimate_dict += [
                {key_list: value_list for key_list, value_list in digimon.items()}
            ]
            if digimon["stage"] not in digimon_stages:
                digimon_stages.append(digimon["stage"])

        elif digimon["stage"] == "Mega":
            mega_digimon += 1
            mega_dict += [
                {key_list: value_list for key_list, value_list in digimon.items()}
            ]
            if digimon["stage"] not in digimon_stages:
                digimon_stages.append(digimon["stage"])

        elif digimon["stage"] == "Ultra":
            ultra_digimon += 1
            ultra_dict += [
                {key_list: value_list for key_list, value_list in digimon.items()}
            ]
            if digimon["stage"] not in digimon_stages:
                digimon_stages.append(digimon["stage"])

        if digimon["type1"] == "Data":
            data_type += 1
            data_dict += [
                {key_list: value_list for key_list, value_list in digimon.items()}
            ]
            if digimon["type1"] not in digimon_types:
                digimon_types.append(digimon["type1"])

        elif digimon["type1"] == "Vaccine":
            vaccine_type += 1
            vaccine_dict += [
                {key_list: value_list for key_list, value_list in digimon.items()}
            ]
            if digimon["type1"] not in digimon_types:
                digimon_types.append(digimon["type1"])

        elif digimon["type1"] == "Virus":
            virus_type += 1
            virus_dict += [
                {key_list: value_list for key_list, value_list in digimon.items()}
            ]
            if digimon["type1"] not in digimon_types:
                digimon_types.append(digimon["type1"])

        elif digimon["type1"] == "Free":
            free_type += 1
            free_dict += [
                {key_list: value_list for key_list, value_list in digimon.items()}
            ]
            if digimon["type1"] not in digimon_types:
                digimon_types.append(digimon["type1"])

    if baby_dict:
        baby_sorted = sorted(
            baby_dict, key=lambda strongest: strongest["attack"], reverse=True
        )
        baby_strongest = baby_sorted[0]
    if rookie_dict:
        rookie_sorted = sorted(
            rookie_dict, key=lambda strongest: strongest["attack"], reverse=True
        )
        rookie_strongest = rookie_sorted[0]
    if champion_dict:
        champion_sorted = sorted(
            champion_dict, key=lambda strongest: strongest["attack"], reverse=True
        )
        champion_strongest = champion_sorted[0]
    if ultimate_dict:
        ultimate_sorted = sorted(
            ultimate_dict, key=lambda strongest: strongest["attack"], reverse=True
        )
        ultimate_strongest = ultimate_sorted[0]
    if mega_dict:
        mega_sorted = sorted(
            mega_dict, key=lambda strongest: strongest["attack"], reverse=True
        )
        mega_strongest = mega_sorted[0]
    if ultra_dict:
        ultra_sorted = sorted(
            ultra_dict, key=lambda strongest: strongest["attack"], reverse=True
        )
        ultra_strongest = ultra_sorted[0]

    if data_dict:
        data_sorted = sorted(
            data_dict, key=lambda strongest: strongest["attack"], reverse=True
        )
        data_strongest = data_sorted[0]
    if vaccine_dict:
        vaccine_sorted = sorted(
            vaccine_dict, key=lambda strongest: strongest["attack"], reverse=True
        )
        vaccine_strongest = vaccine_sorted[0]
    if virus_dict:
        virus_sorted = sorted(
            virus_dict, key=lambda strongest: strongest["attack"], reverse=True
        )
        virus_strongest = virus_sorted[0]
    if free_dict:
        free_sorted = sorted(
            free_dict, key=lambda strongest: strongest["attack"], reverse=True
        )
        free_strongest = free_sorted[0]

    return core.AnswersDigimonTrivia(
        total_trivia= str(len(digimon_data)),
        highest_atk_name= highest_attack_trivia["name"],
        highest_atk_stage= highest_attack_trivia["stage"],
        highest_atk_type= highest_attack_trivia["type1"],
        lowest_atk_name= lowest_attack_trivia["name"],
        lowest_atk_stage= lowest_attack_trivia["stage"],
        lowest_atk_type= lowest_attack_trivia["type1"],
        total_baby= str(baby_digimon),
        total_rookie= str(rookie_digimon),
        total_champion= str(champion_digimon),
        total_ultimate= str(ultimate_digimon),
        total_mega= str(mega_digimon),
        total_ultra= str(ultra_digimon),
        total_data= str(data_type),
        total_vaccine= str(vaccine_type),
        total_virus= str(virus_type),
        total_free= str(free_type),
        baby_strongest= baby_strongest["name"],
        baby_attack= str(baby_strongest["attack"]),
        rookie_strongest= rookie_strongest["name"],
        rookie_attack= str(rookie_strongest["attack"]),
        champion_strongest= champion_strongest["name"],
        champion_attack= str(champion_strongest["attack"]),
        ultimate_strongest= ultimate_strongest["name"],
        ultimate_attack= str(ultimate_strongest["attack"]),
        mega_strongest= mega_strongest["name"],
        mega_attack= str(mega_strongest["attack"]),
        ultra_strongest= ultra_strongest["name"],
        ultra_attack= str(ultra_strongest["attack"]),
        data_strongest= data_strongest["name"],
        data_attack= str(data_strongest["attack"]),
        vaccine_strongest= vaccine_strongest["name"],
        vaccine_attack= str(vaccine_strongest["attack"]),
        virus_strongest= virus_strongest["name"],
        virus_attack= str(virus_strongest["attack"]),
        free_strongest= free_strongest["name"],
        free_attack= str(free_strongest["attack"]),
        digimon_types= sorted(digimon_types),
        types_sum= str(len(digimon_types)),
        digimon_stages= sorted(digimon_stages),
        stages_sum= str(len(digimon_stages)),
    )
