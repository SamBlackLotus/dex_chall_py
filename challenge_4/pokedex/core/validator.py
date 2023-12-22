import core
import os

def file_validator(user_input):
    if len(user_input) == 1:
        print(core.client_usage())
        quit()
        
    command_1 = user_input[1]
   
    if command_1 == "--help":
        if len(user_input) == 2:
            return[command_1]
        else:
            print(f"WARNING! Incorrect amount of arguments.\n{core.client_usage()}")
            quit()
    
    elif command_1 == "--trivia":
        if len(user_input) == 3:
            filepath_1 = user_input[2]
            if not os.path.exists(filepath_1):
                print(f"WARNING: File {filepath_1} does not exist.")
                quit()
            
            id_number = 0
        elif len(user_input) == 5:
            command_2 = user_input[3]
            if command_2 == '--id':
                id_number = user_input[4]
            else:
                print(f"WARNING: This command does not exist.\n{core.client_usage()}")
                quit()
            
            filepath_1 = user_input[2]
            if not os.path.exists(filepath_1):
                print(f"WARNING: File {filepath_1} does not exist.")
                quit()
        else:
            print(f"WARNING! Incorrect amount of arguments.\n{core.client_usage()}")
            quit()
            
        return[command_1,filepath_1,id_number]
     
    elif command_1 == "--player1":
        if len(user_input) <= 5:
            print(f"WARNING! Incorrect amount of arguments.\n{core.client_usage()}")
            quit()
             
        filepath_1 = user_input[2]
        if not os.path.exists(filepath_1):
            print(f"WARNING: File {filepath_1} does not exist.")
            quit()
        
        command_2 = user_input[3]
            
        if command_2 == "--player2":
            if len(user_input) >= 6:
                filepath_2 = user_input[4]
                if not os.path.exists(filepath_2):
                    print(f"WARNING: File {filepath_2} does not exist.")
                    quit()
                    
        else:
            print(f"WARNING: This command does not exist.\n{core.client_usage()}")
            quit()
        
        command_3 = user_input[5]
        command_4 = 0
            
        if command_3 == "--id":
                if len(user_input) == 8: 
                    id_number = user_input[6]
                    command_4 = user_input[7]     

                else:
                    print(f"WARNING! Incorrect amount of arguments.\n{core.client_usage()}")
                    quit()
                        
        elif command_3 == "--info" or command_3 == '--battle':        
            id_number = 0
                    
        else:
            print(f"WARNING: This command does not exist.\n{core.client_usage()}")
            quit()
        
        return[command_1, filepath_1, id_number, command_2, filepath_2, command_3, command_4]
    
    else:
        print(f"WARNING: This command does not exist.\n{core.client_usage()}")
        quit() 