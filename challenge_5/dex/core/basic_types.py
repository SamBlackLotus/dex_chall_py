# TODO: create nested data when is repeated to organize better
# some structures, such as "name, points" - dataclass
from typing import TypedDict, List, Dict


class AnswersTrivia(TypedDict):
    highest_hp_trivia: str
    highest_attack_trivia: str
    highest_defense_trivia: str
    highest_speed_trivia: str
    hp_trivia_int: int
    index: int
    attack_trivia_int: int
    defense_trivia_int: int
    speed_trivia_int: int
    total_trivia: int
    hp_trivia_name: str
    hp_trivia_points: int
    atk_trivia_name: str
    atk_trivia_points: int
    def_trivia_name: str
    def_trivia_points: int
    spd_trivia_name: str
    spd_trivia_points: int
    user_choice_trivia: str


class AnswersInfo(TypedDict):
    strongest_pokemon_player1: str
    strongest_pokemon_player2: str
    legendary_1: bool
    legendary_2: bool
    total_legendary_player1: str
    total_legendary_player2: str
    intersec_pokemon: str
    diff_pokemon: str
    attack: int
    index: int
    strongest_pokemon_player1: int
    strongest_pokemon_player2: int
    total_legendary_player1: int
    total_legendary_player1: int
    player1_total_pokemons: int
    player2_total_pokemons: int
    player1_total_pokemons_info: int
    player2_total_pokemons_info: int
    strongest_pokemon_player1_info: int
    strongest_pokemon_player2_info: int
    legendary_player1_info: int
    legendary_player2_info: int
    repeated_pokemon_info: int
    different_pokemon_info: int
    user_choice_info: str


class AnswersBattle(TypedDict):
    p1_pokemon: List[Dict[str, int]]
    p1_pokemon: List[Dict[str, int]]
    
class AnswersResult(TypedDict):
    hp: str
    attack: str
    defense: str
    name: str
    p1_pokemon_1: str
    p1_pokemon_2: str
    p1_pokemon_3: str
    p2_pokemon_1: str
    p2_pokemon_2: str
    p2_pokemon_3: str
    p1_pkm_1_name: str
    p1_pkm_2_name: str
    p1_pkm_3_name: str
    p2_pkm_1_name: str
    p2_pkm_2_name: str
    p2_pkm_3_name: str
    p1_pkm_1_hp: int
    p1_pkm_2_hp: int
    p1_pkm_3_hp: int
    p2_pkm_1_hp: int
    p2_pkm_2_hp: int
    p2_pkm_3_hp: int
    p1_pkm_1_atk: int
    p1_pkm_2_atk: int
    p1_pkm_3_atk: int
    p2_pkm_1_atk: int
    p2_pkm_2_atk: int
    p2_pkm_3_atk: int
    p1_pkm_1_dfs: int
    p1_pkm_2_dfs: int
    p1_pkm_3_dfs: int
    p2_pkm_1_dfs: int
    p2_pkm_2_dfs: int
    p2_pkm_3_dfs: int
    p1_player: str
    p2_player: str
    while_counter: int
    p1_pkm_1_hp: int
    p1_pkm_2_hp: int
    p1_pkm_3_hp: int
    p2_pkm_1_hp: int
    p2_pkm_2_hp: int
    p2_pkm_3_hp: int
    damagep1poke1: int
    damagep1poke2: int
    damagep1poke3: int
    damagep2poke1: int
    damagep2poke2: int
    damagep2poke3: int
    first_pokemon_dead: str
    victorious_player: str
    winner: str
    rounds: int
    loser_pokemon: str
    user_choice_battle: str
