from typing import Dict, Union, List, TypedDict, Optional

# TODO: break more this data struture
class Answers(TypedDict):
    p1_tot_info: int  
    p2_tot_info: int
    strgst_p1_info: str
    strgst_p2_info: str
    leg_1_info: int
    leg_2_info: int
    intersec_pokemon: int
    diff_pokemon: int
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
    winner: int
    rounds: int
    loser_pokemon: str

#Cast the dict data received into a set
def cast_to_set(file_set_1):
    pokemon_set = set()
    for pokemon in file_set_1:
        pokemon_set.add(pokemon["Name"])
    return pokemon_set    

#Cast the needed values into integers
def cast_to_int(value):
    return int(value) if value is not None else 0
    
#Cast the needed values into boolean
def cast_to_bool(value):
    return True if value == "True" else False 

def client_helper():
    # TODO: typo: between
    # TODO: -- info and -- battle have space in between
    helper_msg = """
    Hello! Welcome to the Pokedex.
    
    Here you can choose betweem the following options, that are:
    
    --trivia
    
    If you choose trivia we'll show you some interesting  information
    about the pokemon list you provided, notice that this option only
    works with one file at time, so inform just one list for each time 
    you use this option.
    
    For the next two options notice that we'll need two players, 
    and each player will need to provide a list, since the
    functions work with comparisons:
    
    --info
    
    We'll show you some comparative information about the two players
    pokemon lists.
    
    --battle
    
    The two players will challenge each other, using their three strongest
    pokemon, where the first pokemon to fall decides the winner, and we'll
    show you the battle information.
    
    Warning: If you have any doubt about how to use the function read the ATENTION
    flag at the client usage.
   
    """
    return print(helper_msg)

def client_usage():
    # TODO: typo: that both lists
    # TODO: add explanation about what is an id
    client_usage_msg = """
    CLI usage:
    
        > python3 pokedex_crud.py --help
        > python3 pokedex_crud.py --player1 pokemons_1.json --trivia  --id 1
        > python3 pokedex_crud.py --player1 pokemons_1.json --player2 pokemons_2.json --id 1 --info
        > python3 pokedex_crud.py --player1 pokemons_1.json --player2 pokemons_2.json --id 1 --battle
        
        ATENTION:
        
        Where you read <pokemons_1.json> or <pokemons_2.json> 
        Notice that the both list don't need to be in the same format, here you can use more than one file
        format at the same time, like a json and a csv list at the same time, it will work as well.
        You can use the formats that best suits your needs:
        Example --> pokemons_1.json  pokemons_2.json 
                    pokemons_1.csv   pokemons_2.csv
                    pokemons_1.xml   pokemons_2.xml
                    pokemons_1.yaml  pokemons_2.yaml
                    
        For all options you'll need to inform an id, so the function can
        save the log in a text file, if you don't inform any id number it will be 
        automatically set as 0.
    
        Before using the function you can choose what will be done with the information
        generated, answering the question that will be displayed: what do you prefer to do? 
        
        [append|OVERWRITE]
        
        append -> This function will increment the file, keeping the information that already
        exists on the file and simply add the new one, to choose this type any of this:
        'a','A','Append','append','APPEND'  
        
        OVERWRITE -> This option will delete the existing file and create a new one with the
        generated information, to choose this type any of this: 
        'o','O','Overwrite','overwrite','OVERWRITE'. 
        
        WARNING: If you don't choose an option, and just hit enter it will automatically use 
        OVERWRITE option. 
        
        
    """
    return client_usage_msg