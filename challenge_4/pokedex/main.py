# TODO: separate this functon into smaller ones, e.g. parse diff formats, helpers, etc
def main():
    if len(sys.argv) == 1:
        client_usage()
        quit()
        
    elif len(sys.argv) == 2:
        command1 = sys.argv[1]
        if command1 == "--help":
            client_helper()
            quit()
        else:
            print(f"WARNING: This command does not exist.\n{client_usage()}")
            quit()
            
    elif len(sys.argv) > 8:
            print(f"WARNING! Incorrect amount of arguments.\n{client_usage()}")
            quit()

    command1 = sys.argv[1]

    if command1 == "--player1":
        if len(sys.argv) == 2:
            print(f"WARNING! Incorrect amount of arguments.\n{client_usage()}")
            quit()
        elif len(sys.argv) == 3:
            print(f"WARNING! Incorrect amount of arguments.\n{client_usage()}")
            quit()    
    
        filepath_1 = sys.argv[2]
        if not os.path.exists(filepath_1):
                print(f"WARNING: File {filepath_1} does not exist.")
                quit()
        
        command2 = sys.argv[3]
        
        # TODO: --trivia shouldn't need the --player1 arg
        if command2 == "--trivia":
            if len(sys.argv) >= 7:
                print(f"WARNING! Incorrect amount of arguments.\n{client_usage()}")
                quit()         
            if '.json' in filepath_1:    
                data_1 = read_file_json(filepath_1)
            elif '.csv' in filepath_1:    
                data_1 = read_file_csv(filepath_1)
            elif '.xml' in filepath_1:    
                data_1 = read_file_xml(filepath_1)
            elif '.yaml' in filepath_1:    
                data_1 = read_file_yaml(filepath_1)
            else:
                print(f"Error: File format not supported!\n{client_usage()}")
                quit()
            
            if len(sys.argv) >= 5:
                
                command3 = sys.argv[4]
                
                if command3 == '--id':
                    
                    if len(sys.argv) == 6: 
                        idnumber = sys.argv[5]
                    else:
                        print(f"WARNING! Incorrect amount of arguments.\n{client_usage()}")
                        quit() 
                        
                else:
                    print(f"WARNING: This command does not exist.\n{client_usage()}")
                    quit()   
            else:
                idnumber = 0
            info = process_trivia(data_1)
            show_trivia(info,idnumber)
            quit()
            
        elif command2 == "--player2":
            if len(sys.argv) == 4:
                print(f"WARNING! Incorrect amount of arguments.\n{client_usage()}")
                quit()
                
            filepath_2 = sys.argv[4]
            if not os.path.exists(filepath_2):
                    print(f"WARNING: File {filepath_2} does not exist.")
                    quit()
        else:
            print(f"WARNING: This command does not exist.\n{client_usage()}")
            quit()
        
        if len(sys.argv) == 5:
            print(f"WARNING! Incorrect amount of arguments.\n{client_usage()}")
            quit()        
         
        if len(sys.argv) >= 6:    
            command3 = sys.argv[5]
        
            if command3 == "--id":
                if len(sys.argv) == 8:
                    if '.json' in filepath_1:
                        data_1 = read_file_json(filepath_1)
                        dataset_1 = cast_to_set(data_1)
                    elif '.csv' in filepath_1:
                        data_1 = read_file_csv(filepath_1)
                        dataset_1 = cast_to_set(data_1)
                    elif '.xml' in filepath_1:
                        data_1 = read_file_xml(filepath_1)
                        dataset_1 = cast_to_set(data_1)
                    elif '.yaml' in filepath_1:
                        data_1 = read_file_yaml(filepath_1)
                        dataset_1 = cast_to_set(data_1)
                    else:
                        print(f"Error: File format not supported!\n{client_usage()}")
                        quit()
                                
                    if '.json' in filepath_2:
                        data_2= read_file_json(filepath_2)
                        dataset_2 = cast_to_set(data_2)
                    elif '.csv' in filepath_2:
                        data_2 = read_file_csv(filepath_2)
                        dataset_2 = cast_to_set(data_2)
                    elif '.xml' in filepath_2:
                        data_2 = read_file_xml(filepath_2)
                        dataset_2 = cast_to_set(data_2)
                    elif '.yaml' in filepath_2:
                        data_2 = read_file_yaml(filepath_2)
                        dataset_2 = cast_to_set(data_2)
                    else:
                        print(f"Error: File format not supported!\n{client_usage()}")
                        quit()
                    
                    idnumber = sys.argv[6]
                    command4 = sys.argv[7]     

                    if command4 == "--info":   
                        info = process_info(data_1,data_2,dataset_1,dataset_2)
                        show_info(info,idnumber)
                        
                    elif command4 == "--battle":
                        battle = select_pokemons_for_battle(data_1,data_2)
                        result = pokemon_battle(battle)
                        show_battle_winner(battle,result,idnumber)
                    else:
                        print(f"WARNING: This command does not exist.\n{client_usage()}")
                        quit()
                        
                else:
                    print(f"WARNING! Incorrect amount of arguments.\n{client_usage()}")
                    quit()
                    
            elif command3 == "--info" or command3 == '--battle':        
                if '.json' in filepath_1:
                    data_1 = read_file_json(filepath_1)
                    dataset_1 = cast_to_set(data_1)
                elif '.csv' in filepath_1:
                    data_1 = read_file_csv(filepath_1)
                    dataset_1 = cast_to_set(data_1)
                elif '.xml' in filepath_1:
                    data_1 = read_file_xml(filepath_1)
                    dataset_1 = cast_to_set(data_1)
                elif '.yaml' in filepath_1:
                    data_1 = read_file_yaml(filepath_1)
                    dataset_1 = cast_to_set(data_1)
                else:
                    print(f"Error: File format not supported!\n{client_usage()}")
                    quit()    
                                
                if '.json' in filepath_2:
                    data_2= read_file_json(filepath_2)
                    dataset_2 = cast_to_set(data_2)
                elif '.csv' in filepath_2:
                    data_2 = read_file_csv(filepath_2)
                    dataset_2 = cast_to_set(data_2)
                elif '.xml' in filepath_2:
                    data_2 = read_file_xml(filepath_2)
                    dataset_2 = cast_to_set(data_2)
                elif '.yaml' in filepath_2:
                    data_2 = read_file_yaml(filepath_2)
                    dataset_2 = cast_to_set(data_2)
                else:
                    print(f"Error: File format not supported!\n{client_usage()}")
                    quit()    
                
                idnumber = 0
            
                if command3 == "--info":   
                    info = process_info(data_1,data_2,dataset_1,dataset_2)
                    show_info(info,idnumber)                
                elif command3 == "--battle":
                    battle = select_pokemons_for_battle(data_1,data_2)
                    result = pokemon_battle(battle)
                    show_battle_winner(battle,result,idnumber)
            else:
                print(f"WARNING: This command does not exist.\n{client_usage()}")
                quit()   
    else:
        print(f"WARNING: This command does not exist.\n{client_usage()}")
        quit()
       
if __name__ == "__main__":
    main() 