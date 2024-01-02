import core
from datetime import datetime


def select_pokemons_for_battle(player_1_battle, player_2_battle):
    p1_pokemon = []
    p2_pokemon = []

    attack_sorted_p1 = sorted(
        player_1_battle, key=lambda strongest_mon: strongest_mon["Attack"], reverse=True
    )
    attack_sorted_p2 = sorted(
        player_2_battle, key=lambda strongest_mon: strongest_mon["Attack"], reverse=True
    )
    counter = 0

    while counter <= 2:
        p1_pokemon.append(attack_sorted_p1[counter])
        p2_pokemon.append(attack_sorted_p2[counter])
        counter += 1

    return core.AnswersBattle(p1_player=p1_pokemon, p2_player=p2_pokemon)


def pokemon_battle(start_battle):
    print(start_battle)
    while_counter = 0

    p1_mon_1_hp = start_battle["p1_player"][0]["HP"]
    p1_mon_2_hp = start_battle["p1_player"][1]["HP"]
    p1_mon_3_hp = start_battle["p1_player"][2]["HP"]
    p2_mon_1_hp = start_battle["p2_player"][0]["HP"]
    p2_mon_2_hp = start_battle["p2_player"][1]["HP"]
    p2_mon_3_hp = start_battle["p2_player"][2]["HP"]

    damage_p1_mon1 = (
        0.5
        * (start_battle["p1_player"][0]["Attack"])
        / (start_battle["p2_player"][0]["Defense"])
        + 1
    )
    damage_p1_mon2 = (
        0.5
        * (start_battle["p1_player"][1]["Attack"])
        / (start_battle["p2_player"][1]["Defense"])
        + 1
    )
    damage_p1_mon3 = (
        0.5
        * (start_battle["p1_player"][2]["Attack"])
        / (start_battle["p2_player"][2]["Defense"])
        + 1
    )
    damage_p2_mon1 = (
        0.5
        * (start_battle["p2_player"][0]["Attack"])
        / (start_battle["p1_player"][0]["Defense"])
        + 1
    )
    damage_p2_mon2 = (
        0.5
        * (start_battle["p2_player"][1]["Attack"])
        / (start_battle["p1_player"][1]["Defense"])
        + 1
    )
    damage_p2_mon3 = (
        0.5
        * (start_battle["p2_player"][2]["Attack"])
        / (start_battle["p1_player"][2]["Defense"])
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
            first_pokemon_dead = start_battle["p1_player"][0]["Name"]
            victorious_player = "2"
            break
        elif p1_mon_2_hp <= 0:
            first_pokemon_dead = start_battle["p1_player"][1]["Name"]
            victorious_player = "2"
            break
        elif p1_mon_3_hp <= 0:
            first_pokemon_dead = start_battle["p1_player"][2]["Name"]
            victorious_player = "2"
            break
        elif p2_mon_1_hp <= 0:
            first_pokemon_dead = start_battle["p2_player"][0]["Name"]
            victorious_player = "1"
            break
        elif p2_mon_2_hp <= 0:
            first_pokemon_dead = start_battle["p2_player"][1]["Name"]
            victorious_player = "1"
            break
        elif p2_mon_3_hp <= 0:
            first_pokemon_dead = start_battle["p2_player"][2]["Name"]
            victorious_player = "1"
            break

    return core.AnswersResult(
        p1_pkm_1_name=start_battle["p1_player"][0]["Name"],
        p1_pkm_2_name=start_battle["p1_player"][1]["Name"],
        p1_pkm_3_name=start_battle["p1_player"][2]["Name"],
        p2_pkm_1_name=start_battle["p2_player"][0]["Name"],
        p2_pkm_2_name=start_battle["p2_player"][1]["Name"],
        p2_pkm_3_name=start_battle["p2_player"][2]["Name"],
        p1_pkm_1_hp=start_battle["p1_player"][0]["HP"],
        p1_pkm_2_hp=start_battle["p1_player"][1]["HP"],
        p1_pkm_3_hp=start_battle["p1_player"][2]["HP"],
        p2_pkm_1_hp=start_battle["p2_player"][0]["HP"],
        p2_pkm_2_hp=start_battle["p2_player"][1]["HP"],
        p2_pkm_3_hp=start_battle["p2_player"][2]["HP"],
        p1_pkm_1_atk=start_battle["p1_player"][0]["Attack"],
        p1_pkm_2_atk=start_battle["p1_player"][1]["Attack"],
        p1_pkm_3_atk=start_battle["p1_player"][2]["Attack"],
        p2_pkm_1_atk=start_battle["p2_player"][0]["Attack"],
        p2_pkm_2_atk=start_battle["p2_player"][1]["Attack"],
        p2_pkm_3_atk=start_battle["p2_player"][2]["Attack"],
        p1_pkm_1_dfs=start_battle["p1_player"][0]["Attack"],
        p1_pkm_2_dfs=start_battle["p1_player"][1]["Attack"],
        p1_pkm_3_dfs=start_battle["p1_player"][2]["Attack"],
        p2_pkm_1_dfs=start_battle["p2_player"][0]["Attack"],
        p2_pkm_2_dfs=start_battle["p2_player"][1]["Attack"],
        p2_pkm_3_dfs=start_battle["p2_player"][2]["Attack"],
        winner=victorious_player,
        rounds=while_counter,
        loser_pokemon=first_pokemon_dead,
    )
