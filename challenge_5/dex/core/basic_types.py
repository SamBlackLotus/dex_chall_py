from typing import TypedDict, List, Dict


class AnswersPokemonTrivia(TypedDict):
    total_trivia: int
    hp_trivia_name: str
    hp_trivia_points: int
    atk_trivia_name: str
    atk_trivia_points: int
    def_trivia_name: str
    def_trivia_points: int
    spd_trivia_name: str
    spd_trivia_points: int


class AnswersDigimonTrivia(TypedDict):
    total_trivia: int
    highest_atk_name: int
    highest_atk_stage: str
    highest_atk_type: str
    lowest_atk_name: str
    lowest_atk_stage: str
    lowest_atk_type: str
    total_baby: int
    total_rookie: int
    total_champion: int
    total_ultimate: int
    total_mega: int
    total_ultra: int
    total_data: int
    total_vaccine: int
    total_virus: int
    total_free: int
    baby_strongest: str
    baby_attack: int
    rookie_strongest: str
    rookie_attack: int
    champion_strongest: str
    champion_attack: int
    ultimate_strongest: str
    ultimate_attack: int
    mega_strongest: str
    mega_attack: int
    ultra_strongest: str
    ultra_attack: int
    data_strongest: str
    data_attack: int
    vaccine_strongest: str
    vaccine_attack: int
    virus_strongest: str
    virus_attack: int
    free_strongest: str
    free_attack: int
    digimon_types: List[str]
    types_sum: int
    digimon_stages: List[str]
    stages_sum: int


class AnswersInfo(TypedDict):
    player1_total_monster_info: int
    player2_total_monster_info: int
    strongest_monster_player1_info: str
    strongest_monster_player2_info: str
    stg_or_legend_player1_info: str
    stg_or_legend_player2_info: str
    repeated_monster_info: int
    different_monster_info: int


class AnswersBattle(TypedDict):
    p1_player: List[Dict[str, int]]
    p2_player: List[Dict[str, int]]


class AnswersResult(TypedDict):
    p1_mon_1_name: str
    p1_mon_2_name: str
    p1_mon_3_name: str
    p2_mon_1_name: str
    p2_mon_2_name: str
    p2_mon_3_name: str
    p1_mon_1_hp: str
    p1_mon_2_hp: str
    p1_mon_3_hp: str
    p2_mon_1_hp: str
    p2_mon_2_hp: str
    p2_mon_3_hp: str
    p1_mon_1_atk: str
    p1_mon_2_atk: str
    p1_mon_3_atk: str
    p2_mon_1_atk: str
    p2_mon_2_atk: str
    p2_mon_3_atk: str
    p1_mon_1_dfs: str
    p1_mon_2_dfs: str
    p1_mon_3_dfs: str
    p2_mon_1_dfs: str
    p2_mon_2_dfs: str
    p2_mon_3_dfs: str
    winner: str
    rounds: str
    loser_monster: str
