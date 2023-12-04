import os
import sys
import csv

   
def read_file_1(filepath):
    with open((filepath), newline='') as data:

        reader = csv.DictReader(data, delimiter=',')

        for row in reader:

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
        > python3 new_chall.py --filename pokemons_1.csv 
        > python3 new_chall.py --help
        
    """
    return client_usage_msg 

def main():
    if len(sys.argv) == 1:
        client_usage()
        quit()
        
    elif len(sys.argv) > 3:
       print(f"WARNING! Incorrect amount of arguments.\n{client_usage()}")
       quit()

    command = sys.argv[1]

    if command == "--help":
        client_helper()
        quit()

    elif command == "--filename":
        if len(sys.argv) == 2:
            print(f"WARNING! Incorrect amount of arguments.\n{client_usage()}")
            quit()
    
        filepath = sys.argv[2]
        if not os.path.exists(filepath):
                print(f"WARNING: File {filepath} does not exist.")
                quit()        

        data = read_file_1(filepath)
        #info = process_pokemons(data)
        #show_info(info)
    else:
        print(f"WARNING: This command does not exist.\n{client_usage()}")

        
if __name__ == "__main__":
    main()      
                