import core
from typing import Dict, Union, List


def select_battle_team(
    player_1_battle: Dict[str, Union[str, int]], player_2_battle: Dict[str, int], team_size: int
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

    attack_sorted_p1: List[str] = sorted(
        player_1_battle, key=lambda strongest_mon: strongest_mon["attack"], reverse=True
    )
    attack_sorted_p2: List[str] = sorted(
        player_2_battle, key=lambda strongest_mon: strongest_mon["attack"], reverse=True
    )
    for idx in range(team_size):
        team_player1.append(attack_sorted_p1[idx])
        team_player2.append(attack_sorted_p2[idx])

    return core.AnswersBattle(p1_player=team_player1, p2_player=team_player2)


def start_battle(monster_team: core.AnswersBattle, team_size) -> core.AnswersResult:
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
    team_player1 = monster_team["p1_player"]
    team_player2 = monster_team["p2_player"]
    lowest_round = 9999

    for position in range(team_size):
        round_counter = 0
        p1_monster_hp = team_player1[position]["hp"]
        p2_monster_hp = team_player2[position]["hp"]
        damage_player1_monster = (
            0.5
            * (team_player1[position]["attack"])
            / (team_player2[position]["defense"])
            + 1
        )
        damage_player2_monster = (
            0.5
            * (team_player2[position]["attack"])
            / (team_player2[position]["defense"])
            + 1
        )

        while True:
            round_counter += 1

            p1_monster_hp -= damage_player1_monster
            p2_monster_hp -= damage_player2_monster

            if p1_monster_hp <= 0:
                if round_counter < lowest_round:
                    first_mon_dead = team_player1[position]["name"]
                    victorious_player = "2"
                    lowest_round = round_counter
                break
            elif p2_monster_hp <= 0:
                if round_counter < lowest_round:
                    first_mon_dead = team_player2[position]["name"]
                    victorious_player = "1"
                    lowest_round = round_counter
                break

    return core.AnswersResult(
        winner=victorious_player, rounds=lowest_round, loser_monster=first_mon_dead
    )
