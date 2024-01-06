import core
from datetime import datetime


def select_pokemons_for_battle(player_1_battle, player_2_battle):
    p1_pokemon = []
    p2_pokemon = []

    attack_sorted_p1 = sorted(
        player_1_battle, key=lambda strongest_mon: strongest_mon["attack"], reverse=True
    )
    attack_sorted_p2 = sorted(
        player_2_battle, key=lambda strongest_mon: strongest_mon["attack"], reverse=True
    )
    counter = 0

    while counter <= 2:
        p1_pokemon.append(attack_sorted_p1[counter])
        p2_pokemon.append(attack_sorted_p2[counter])
        counter += 1

    return core.AnswersBattle(p1_player=p1_pokemon, p2_player=p2_pokemon)


def pokemon_battle(start_battle):
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
            first_pokemon_dead = start_battle["p1_player"][0]["name"]
            victorious_player = "2"
            break
        elif p1_mon_2_hp <= 0:
            first_pokemon_dead = start_battle["p1_player"][1]["name"]
            victorious_player = "2"
            break
        elif p1_mon_3_hp <= 0:
            first_pokemon_dead = start_battle["p1_player"][2]["name"]
            victorious_player = "2"
            break
        elif p2_mon_1_hp <= 0:
            first_pokemon_dead = start_battle["p2_player"][0]["name"]
            victorious_player = "1"
            break
        elif p2_mon_2_hp <= 0:
            first_pokemon_dead = start_battle["p2_player"][1]["name"]
            victorious_player = "1"
            break
        elif p2_mon_3_hp <= 0:
            first_pokemon_dead = start_battle["p2_player"][2]["name"]
            victorious_player = "1"
            break

    return core.AnswersResult(
        p1_pkm_1_name=start_battle["p1_player"][0]["name"],
        p1_pkm_2_name=start_battle["p1_player"][1]["name"],
        p1_pkm_3_name=start_battle["p1_player"][2]["name"],
        p2_pkm_1_name=start_battle["p2_player"][0]["name"],
        p2_pkm_2_name=start_battle["p2_player"][1]["name"],
        p2_pkm_3_name=start_battle["p2_player"][2]["name"],
        p1_pkm_1_hp=start_battle["p1_player"][0]["hp"],
        p1_pkm_2_hp=start_battle["p1_player"][1]["hp"],
        p1_pkm_3_hp=start_battle["p1_player"][2]["hp"],
        p2_pkm_1_hp=start_battle["p2_player"][0]["hp"],
        p2_pkm_2_hp=start_battle["p2_player"][1]["hp"],
        p2_pkm_3_hp=start_battle["p2_player"][2]["hp"],
        p1_pkm_1_atk=start_battle["p1_player"][0]["attack"],
        p1_pkm_2_atk=start_battle["p1_player"][1]["attack"],
        p1_pkm_3_atk=start_battle["p1_player"][2]["attack"],
        p2_pkm_1_atk=start_battle["p2_player"][0]["attack"],
        p2_pkm_2_atk=start_battle["p2_player"][1]["attack"],
        p2_pkm_3_atk=start_battle["p2_player"][2]["attack"],
        p1_pkm_1_dfs=start_battle["p1_player"][0]["attack"],
        p1_pkm_2_dfs=start_battle["p1_player"][1]["attack"],
        p1_pkm_3_dfs=start_battle["p1_player"][2]["attack"],
        p2_pkm_1_dfs=start_battle["p2_player"][0]["attack"],
        p2_pkm_2_dfs=start_battle["p2_player"][1]["attack"],
        p2_pkm_3_dfs=start_battle["p2_player"][2]["attack"],
        winner=victorious_player,
        rounds=while_counter,
        loser_pokemon=first_pokemon_dead,
    )
