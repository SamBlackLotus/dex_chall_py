import core
import menu
import sys

# TODO: separate this functon into smaller ones, e.g. parse diff formats, helpers, etc

def main():
    user_input = sys.argv
    arguments = core.file_validator(user_input)
    
    if arguments[0] == "--help":
        core.client_helper()
        quit()
    
    elif arguments[0] == "--trivia":
        id_number = arguments[2]
        data_1 = core.read_file(arguments[1])
        info = menu.process_trivia(data_1)
        menu.show_trivia(info,id_number)
        quit()
    
    elif arguments[0] == "--player1":
        
        id_number = arguments[2]
        data_1 = core.read_file(arguments[1])
        dataset_1 = core.cast_to_set(data_1)
        data_2= core.read_file(arguments[4])
        dataset_2 = core.cast_to_set(data_2)
        
        if arguments[5] == "--info" or arguments[6] == "--info":                       
            info = menu.process_info(data_1,data_2,dataset_1,dataset_2)
            menu.show_info(info,id_number)
            quit()                
        elif arguments[5] == "--battle" or arguments[6] == "--battle":
            battle = menu.select_pokemons_for_battle(data_1,data_2)              
            result = menu.pokemon_battle(battle)
            menu.show_battle_winner(battle,result,id_number)
            quit()  
        
if   __name__ == "__main__":
    main() 