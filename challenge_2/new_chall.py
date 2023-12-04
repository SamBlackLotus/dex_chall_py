import os
import sys
import csv

   
def read_file_1(filepath_1):
    with open((filepath_1), newline='') as data_1:

        reader_1 = csv.DictReader(data_1)

        for row in reader_1:

            print(row)
            
def read_file_2(filepath_2):
    with open((filepath_2), newline='') as data_2:

        reader_2 = csv.DictReader(data_2)

        for row in reader_2:
            
            print(row)            
 
 
                  
def client_helper():
    helper_msg = """
    Hello! Welcome to the Pokedex.
    We will inform some statistic about your pokemon list.
    """
    return print(helper_msg)

def client_usage():
    client_usage_msg = """
    CLI usage:
        > python3 new_chall.py --player1 pokemons_1.csv 
        > python3 new_chall.py --help
        
    """
    return client_usage_msg 

def main():
    if len(sys.argv) == 1:
        client_usage()
        quit()
        
    elif len(sys.argv) > 5:
       print(f"WARNING! Incorrect amount of arguments.\n{client_usage()}")
       quit()

    command = sys.argv[1]

    if command == "--help":
        client_helper()
        quit()

    elif command == "--player1":
        if len(sys.argv) == 2:
            print(f"WARNING! Incorrect amount of arguments.\n{client_usage()}")
            quit()
    
        filepath_1 = sys.argv[2]
        if not os.path.exists(filepath_1):
                print(f"WARNING: File {filepath_1} does not exist.")
                quit()  
                
        filepath_2 = sys.argv[4]
        if not os.path.exists(filepath_2):
                print(f"WARNING: File {filepath_2} does not exist.")
                quit()           
                
                     

        data_1 = read_file_1(filepath_1)
        data_2 = read_file_2(filepath_2)
        #info = process_pokemons(data)
        #show_info(info)
    else:
        print(f"WARNING: This command does not exist.\n{client_usage()}")

        
if __name__ == "__main__":
    main()      
                