import core
import menu
import os
import sys
from datetime import datetime
from enum import Enum
from typing import Dict, Union, List, TypedDict, Optional

# TODO: separate this functon into smaller ones, e.g. parse diff formats, helpers, etc

def main():
    if len(sys.argv) == 1:
        print(core.client_usage())
        quit()
        
    command_1 = sys.argv[1]

    if command_1 == "--player1":
        if len(sys.argv) <= 5:
            print(f"WARNING! Incorrect amount of arguments.\n{core.client_usage()}")
            quit()    
    
    elif command_1 == "--help":
        if len(sys.argv) == 2:
            core.client_helper()
            quit()
        else:
            print(f"WARNING! Incorrect amount of arguments.\n{core.client_usage()}")
            quit()
    
    elif command_1 == "--trivia":
        if len(sys.argv) == 3:
            filepath_1 = sys.argv[2]
            if not os.path.exists(filepath_1):
                print(f"WARNING: File {filepath_1} does not exist.")
                quit()
            
            id_number = 0
        elif len(sys.argv) == 5:
            command_2 = sys.argv[3]
            if command_2 == '--id':
                id_number = sys.argv[4]
            else:
                print(f"WARNING: This command does not exist.\n{core.client_usage()}")
                quit()
        else:
            print(f"WARNING! Incorrect amount of arguments.\n{core.client_usage()}")
            quit()
            
        data_1 = core.read_file(filepath_1)
        info = menu.process_trivia(data_1)
        menu.show_trivia(info,id_number)
        quit()
    else:
        print(f"WARNING: This command does not exist.\n{core.client_usage()}")
        quit()      
    
    filepath_1 = sys.argv[2]
    if not os.path.exists(filepath_1):
        print(f"WARNING: File {filepath_1} does not exist.")
        quit()
    
    command_2 = sys.argv[3]
        
    if command_2 == "--player2":
        if len(sys.argv) >= 6:
            filepath_2 = sys.argv[4]
            if not os.path.exists(filepath_2):
                print(f"WARNING: File {filepath_2} does not exist.")
                quit()
                
    else:
        print(f"WARNING: This command does not exist.\n{core.client_usage()}")
        quit()
    
    command_3 = sys.argv[5]
        
    if command_3 == "--id":
            if len(sys.argv) == 8: 
                id_number = sys.argv[6]
                command_4 = sys.argv[7]     

            else:
                print(f"WARNING! Incorrect amount of arguments.\n{core.client_usage()}")
                quit()
                    
    elif command_3 == "--info" or command_3 == '--battle':        
        id_number = 0
                  
    else:
        print(f"WARNING: This command does not exist.\n{core.client_usage()}")
        quit()
        
    data_1 = core.read_file(filepath_1)
    dataset_1 = core.cast_to_set(data_1)
    data_2= core.read_file(filepath_2)
    dataset_2 = core.cast_to_set(data_2)
    
    if command_3 == "--info" or command_4 == "--info":                       
        info = menu.process_info(data_1,data_2,dataset_1,dataset_2)
        menu.show_info(info,id_number)                
    elif command_3 == "--battle" or command_4 == "--info":
        battle = menu.select_pokemons_for_battle(data_1,data_2)              
        result = menu.pokemon_battle(battle)
        menu.show_battle_winner(battle,result,id_number)

if   __name__ == "__main__":
    main() 