import core
from typing import Dict


# TODO: try to not cross 120 col width
def process_info(
    process_monster1: Dict[str, int],
    process_monster2: Dict[str, int],
    monster_set_1: Dict[str, int],
    monster_set_2: Dict[str, int],
    archive_type: str,
) -> core.AnswersInfo:
    # TODO: create a function for each question
    """
        This function will process some validations using data, to find
        some specific information and answer the given questions.

    Parameters
    ----------
    process_monster1:
        The player 1 list of monsters
    process_monster2:
        the player 2 list of monsters
    monster_set_1:
        The player 1 list converted in a set
    monster_set_2:
        The player 2 list converted in a set
    Returns
    -------
    AnswerTrivia:
        Returns the results for the asked validations and puts
        then in variables so it can be called and presented
        to the user.

    """

    strongest_monster_player1 = {"index": 0, "value": 0}
    strongest_monster_player2 = {"index": 0, "value": 0}
    total_stg_or_legend_player1 = 0
    total_stg_or_legend_player2 = 0
    intersec_monster = monster_set_1.intersection(monster_set_2)
    diff_monster = monster_set_1.difference(monster_set_2)
    monster_dict = []
    monster_dict2 = []

    for index, monster in enumerate(process_monster1):
        player1_total_monster = len(process_monster1)
        monster_dict += [
            {key_list: value_list for key_list, value_list in monster.items()}
        ]

        if monster_dict:
            monster_attack = sorted(
                monster_dict, key=lambda highest: highest["attack"], reverse=True
            )
            strongest_monster_player1 = monster_attack[0]

        if archive_type == "--pokemon":
            if core.cast_to_bool(monster["legendary"]):
                total_stg_or_legend_player1 += 1

        elif archive_type == "--digimon":
            if monster["stage"] == "Ultra":
                total_stg_or_legend_player1 += 1

    for index, monster in enumerate(process_monster2):
        player2_total_monster = len(process_monster2)
        monster_dict2 += [
            {key_list: value_list for key_list, value_list in monster.items()}
        ]

        if monster_dict2:
            monster_attack2 = sorted(
                monster_dict2, key=lambda highest: highest["attack"], reverse=True
            )
            strongest_monster_player2 = monster_attack2[0]

        if archive_type == "--pokemon":
            if core.cast_to_bool(monster["legendary"]):
                total_stg_or_legend_player2 += 1

        elif archive_type == "--digimon":
            if monster["stage"] == "Ultra":
                total_stg_or_legend_player2 += 1
    print(strongest_monster_player2)
    print(strongest_monster_player1)
    return core.AnswersInfo(
        player1_total_monster_info=str(player1_total_monster),
        player2_total_monster_info=str(player2_total_monster),
        strongest_monster_player1_info=strongest_monster_player1["name"],
        strongest_monster_player2_info=strongest_monster_player2["name"],
        stg_or_legend_player1_info=str(total_stg_or_legend_player1),
        stg_or_legend_player2_info=str(total_stg_or_legend_player2),
        repeated_monster_info=str(len(intersec_monster)),
        different_monster_info=str(len(diff_monster))
    )
