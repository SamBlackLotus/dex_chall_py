import core
from datetime import datetime


def process_info(process_poke1, process_poke2, pokemon_set_1, pokemon_set_2):
    """
        This function will process some validations using data, to find
        some specific information and answer the given questions.

    Parameters
    ----------
    process_poke1:

    process_poke2:

    pokemon_set_1:

    pokemon_set_2:

    Returns
    -------
    AnswerTrivia:
        Returns the results for the asked validations and puts
        then in variables so it can the called to be presented
        to the user.

    """

    strongest_pokemon_player1 = {"index": 0, "value": 0}
    strongest_pokemon_player2 = {"index": 0, "value": 0}
    legendary_1 = 0
    legendary_2 = 0
    total_legendary_player1 = 0
    total_legendary_player2 = 0
    intersec_pokemon = pokemon_set_1.intersection(pokemon_set_2)
    diff_pokemon = pokemon_set_1.difference(pokemon_set_2)
    print(process_poke1)
    for index, pokemon in enumerate(process_poke1):
        player1_total_pokemons = len(process_poke1)

        attack = core.cast_to_int(pokemon["attack"])
        if attack > strongest_pokemon_player1["value"]:
            strongest_pokemon_player1["index"] = index
            strongest_pokemon_player1["value"] = attack

        legendary_1 = core.cast_to_bool(pokemon["legendary"])
        # TODO: there is no need to check for True
        if legendary_1 is True:
            total_legendary_player1 += 1

    for index, pokemon in enumerate(process_poke2):
        player2_total_pokemons = len(process_poke2)

        attack = core.cast_to_int(pokemon["attack"])
        if attack > strongest_pokemon_player2["value"]:
            strongest_pokemon_player2["index"] = index
            strongest_pokemon_player2["value"] = attack

        legendary_2 = core.cast_to_bool(pokemon["legendary"])
        if legendary_2 is True:
            total_legendary_player2 += 1

    return core.AnswersInfo(
        player1_total_pokemons_info=str(player1_total_pokemons),
        player2_total_pokemons_info=str(player2_total_pokemons),
        strongest_pokemon_player1_info=process_poke1[
            strongest_pokemon_player1["index"]
        ]["name"],
        strongest_pokemon_player2_info=process_poke2[
            strongest_pokemon_player2["index"]
        ]["name"],
        legendary_player1_info=str(total_legendary_player1),
        legendary_player2_info=str(total_legendary_player2),
        repeated_pokemon_info=str(len(intersec_pokemon)),
        different_pokemon_info=str(len(diff_pokemon)),
    )
