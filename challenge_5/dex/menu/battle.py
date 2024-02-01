import core
from typing import Dict


def select_battle_team(
    player_1_battle: Dict[str, int], player_2_battle: Dict[str, int]
) -> core.AnswersBattle:
    """
        This function defines the player teams.

    Parameters
    ----------
    player_1_battle:
        The player 1 dict of monsters.
    player_2_battle:
        the player 2 dict of monsters.

    Returns
    -------
    AnswerBattle:
        team_player1 = The three strongest monsters from player_1_battle.
        team_player2 = The three strongest monsters from player_2_battle.

    """

    team_player1 = []
    team_player2 = []

    attack_sorted_p1 = sorted(
        player_1_battle, key=lambda strongest_mon: strongest_mon["attack"], reverse=True
    )
    attack_sorted_p2 = sorted(
        player_2_battle, key=lambda strongest_mon: strongest_mon["attack"], reverse=True
    )
    
    for idx in range(3):
        team_player1.append(attack_sorted_p1[idx])
        team_player2.append(attack_sorted_p2[idx])

    return core.AnswersBattle(p1_player=team_player1, p2_player=team_player2)


def start_battle(team_player1, team_player2: core.AnswersBattle) -> core.AnswersResult:
    # TODO: start_battle seems like an action, it could be a name  for a function
    # the args should describe the players characteristics, such as monsters or
    # pokemon or digimon or player, etc.

    # TODO: this function is hard to extend because imagine that now we want
    # to have a battle with 5 monsters instead of 3, you would need to
    # hardcode more 2 lines of each logic/comparison, it would be better
    # to receive this information as an argument and loop throughout each
    # player's team.

    """
        This function receives the list of the three
        strongest monsters of player 1 and 2, and
        simulate a battle between them to find the
        strongest team.

    Parameters
    ----------
    start_battle:
        Brings the two trios of monsters of each player.

    Returns
    -------
    AnswerTrivia:
        Return a set of data about the two trios of
        monsters, and information about the result
        of the battle.

    """

    while_counter = 0

    p1_mon_1_hp = start_battle["p1_player"][0]["hp"]
    p1_mon_2_hp = start_battle["p1_player"][1]["hp"]
    p1_mon_3_hp = start_battle["p1_player"][2]["hp"]
    p2_mon_1_hp = start_battle["p2_player"][0]["hp"]
    p2_mon_2_hp = start_battle["p2_player"][1]["hp"]
    p2_mon_3_hp = start_battle["p2_player"][2]["hp"]

    damage_p1_mon1 = (
        0.5
        * (start_battle["p1_player"][0]["attack"])
        / (start_battle["p2_player"][0]["defense"])
        + 1
    )
    damage_p1_mon2 = (
        0.5
        * (start_battle["p1_player"][1]["attack"])
        / (start_battle["p2_player"][1]["defense"])
        + 1
    )
    damage_p1_mon3 = (
        0.5
        * (start_battle["p1_player"][2]["attack"])
        / (start_battle["p2_player"][2]["defense"])
        + 1
    )
    damage_p2_mon1 = (
        0.5
        * (start_battle["p2_player"][0]["attack"])
        / (start_battle["p1_player"][0]["defense"])
        + 1
    )
    damage_p2_mon2 = (
        0.5
        * (start_battle["p2_player"][1]["attack"])
        / (start_battle["p1_player"][1]["defense"])
        + 1
    )
    damage_p2_mon3 = (
        0.5
        * (start_battle["p2_player"][2]["attack"])
        / (start_battle["p1_player"][2]["defense"])
        + 1
    )

    while True:
        while_counter += 1

        p1_mon_1_hp -= damage_p1_mon1
        p1_mon_2_hp -= damage_p1_mon2
        p1_mon_3_hp -= damage_p1_mon3
        p2_mon_1_hp -= damage_p2_mon1
        p2_mon_2_hp -= damage_p2_mon2
        p2_mon_3_hp -= damage_p2_mon3

        if p1_mon_1_hp <= 0:
            first_mon_dead = start_battle["p1_player"][0]["name"]
            victorious_player = "2"
            break
        elif p1_mon_2_hp <= 0:
            first_mon_dead = start_battle["p1_player"][1]["name"]
            victorious_player = "2"
            break
        elif p1_mon_3_hp <= 0:
            first_mon_dead = start_battle["p1_player"][2]["name"]
            victorious_player = "2"
            break
        elif p2_mon_1_hp <= 0:
            first_mon_dead = start_battle["p2_player"][0]["name"]
            victorious_player = "1"
            break
        elif p2_mon_2_hp <= 0:
            first_mon_dead = start_battle["p2_player"][1]["name"]
            victorious_player = "1"
            break
        elif p2_mon_3_hp <= 0:
            first_mon_dead = start_battle["p2_player"][2]["name"]
            victorious_player = "1"
            break

    return core.AnswersResult(
        p1_mon_1_name=start_battle["p1_player"][0]["name"],
        p1_mon_2_name=start_battle["p1_player"][1]["name"],
        p1_mon_3_name=start_battle["p1_player"][2]["name"],
        p2_mon_1_name=start_battle["p2_player"][0]["name"],
        p2_mon_2_name=start_battle["p2_player"][1]["name"],
        p2_mon_3_name=start_battle["p2_player"][2]["name"],
        p1_mon_1_hp=start_battle["p1_player"][0]["hp"],
        p1_mon_2_hp=start_battle["p1_player"][1]["hp"],
        p1_mon_3_hp=start_battle["p1_player"][2]["hp"],
        p2_mon_1_hp=start_battle["p2_player"][0]["hp"],
        p2_mon_2_hp=start_battle["p2_player"][1]["hp"],
        p2_mon_3_hp=start_battle["p2_player"][2]["hp"],
        p1_mon_1_atk=start_battle["p1_player"][0]["attack"],
        p1_mon_2_atk=start_battle["p1_player"][1]["attack"],
        p1_mon_3_atk=start_battle["p1_player"][2]["attack"],
        p2_mon_1_atk=start_battle["p2_player"][0]["attack"],
        p2_mon_2_atk=start_battle["p2_player"][1]["attack"],
        p2_mon_3_atk=start_battle["p2_player"][2]["attack"],
        p1_mon_1_dfs=start_battle["p1_player"][0]["defense"],
        p1_mon_2_dfs=start_battle["p1_player"][1]["defense"],
        p1_mon_3_dfs=start_battle["p1_player"][2]["defense"],
        p2_mon_1_dfs=start_battle["p2_player"][0]["defense"],
        p2_mon_2_dfs=start_battle["p2_player"][1]["defense"],
        p2_mon_3_dfs=start_battle["p2_player"][2]["defense"],
        winner=victorious_player,
        rounds=while_counter,
        loser_monster=first_mon_dead
    )
