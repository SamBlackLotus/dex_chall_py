import os
from typing import List, Set, SupportsIndex, Dict




def client_helper() -> str:
    helper_msg: str = """
    Hello! Welcome to the Pokedex.

    Here you can choose between the following options, that are:

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

    """
    return helper_msg


# TODO: the correct trivia cmd is:
# python3 pokedex/main.py --trivia data/json/pokemons_1.json --id 1
def client_usage() -> str:
    client_usage_msg: str = """
    CLI usage:

    > python3 main.py --help
    > python3 pokedex/main.py --player1 pokemons_1.json --trivia  --id 1
    > python3 pokedex/main.py --player1 pokemons_1.json --player2 pokemons_2.json --id 1 --info
    > python3 pokedex/main.py --player1 pokemons_1.json --player2 pokemons_2.json --id 1 --battle

    ATTENTION:

    Where you read <pokemons_1.json> or <pokemons_2.json>
    Notice that both lists don't need to be in the same format, here you
    can use more than one file format at the same time, like a json and a
    csv list at the same time, it will work as well.
    You can use the formats that best suits your needs:
    Example --> pokemons_1.json  pokemons_2.json
                    pokemons_1.csv   pokemons_2.csv
                    pokemons_1.xml   pokemons_2.xml
                    pokemons_1.yaml  pokemons_2.yaml

    For all options you'll need to inform an id so the function can
    save the log in a text file, if you don't inform any id number it
    will be automatically set as 0. The id is a key name to make the file
    unique, making it possible have multiple files with different data
    across them.

    Before using the function you can choose what will be done with the
    information generated, answering the question that will be displayed:

    What do you prefer to do?

    [append|OVERWRITE]

    append -> This function will increment the file, keeping the
    information that already exists on the file and simply add
    the new one, to choose this type any of this:

    'a','A','Append','append','APPEND'

    OVERWRITE -> This option will delete the existing file and
    create a new one with the generated information, to choose
    this type any of this:

    'o','O','Overwrite','overwrite','OVERWRITE'.

    WARNING: If you don't choose an option, and just hit enter
    it will automatically use OVERWRITE option.
    """
    return client_usage_msg

def save_data(saved_data,archive_type,id_number):
    if os.path.exists(f"{id_number}_{archive_type}.txt"):

        user_choice = input(f"Files {id_number}_{archive_type}.txt already exists, what do you prefer to do? [append|OVERWRITE] : ")

        if user_choice.lower() == 'o' or user_choice.lower() == 'overwrite':

            os.remove(f"{id_number}_{archive_type}.txt")

            with open(f"{id_number}_{archive_type}.txt", "w") as target:
                target.write(saved_data)
        elif user_choice.lower() == 'a' or user_choice.lower() == 'append':

            with open(f"{id_number}_{archive_type}.txt", "a") as target:
                target.write(saved_data)
        else:
            print(f"WARNING: Invalid Input.\n{core.client_usage()}")
            quit()

    else:

        with open(f"{id_number}_{archive_type}.txt", "w") as target:
            target.write(saved_data)

def show_trivia(pokemons_info, id_number):
    """
    This function will print a message in the CLI.

    Parameters
    ----------
    pokemons_info:
        Bring the treated variables which will be used to answer
        the questions

    Returns
    -------
        Create a file with a id value in the name and print the
        same message from the file in the CLI interface.
    """
    datenow = datetime.now()
    msg =  ((" " * 80) + "\n")
    msg += "reported generated on: " + datenow.isoformat() + (" " * 31  ) + "\n"
    msg += ((" " * 80) + "\n")
    msg += (("=" * 29) + " Welcome to the Dex! " + ("=" * 30) + "\n")
    msg += ((" " * 80) + "\n")    
    msg += "Here we have some useful information gathered from the list you provided us:    \n"
    msg += ((" " * 80) + "\n")
    msg += "1. How many pokemons there is in this list:" + (" " * 37) + "\n"
    msg += (" " * 4) + "> " + pokemons_info["total_trivia"] + " pokemons" + \
        (" " * (25 - len(pokemons_info["total_trivia"]))) + "\n"
    msg += ((" " * 80) + "\n")
    msg += "2. The pokemon with the highest HP point is:" + (" " * 36) + "\n"
    msg += (" " * 4) + ">" + pokemons_info["hp_trivia_name"] + " with " + pokemons_info["hp_trivia_points"] + \
        " HP points" + (" " * ((59 - len(pokemons_info["hp_trivia_name"])) - \
        len(pokemons_info["hp_trivia_points"]))) + "\n"
    msg += ((" " * 80) + "\n")
    msg += "3. Which one has the strongest attack:" + (" " * 42) + "\n"
    msg += (" " * 4) + ">" + pokemons_info["atk_trivia_name"] + " with " + \
        pokemons_info["atk_trivia_points"] + " attack points." + \
        (" " * ((54 - len(pokemons_info["atk_trivia_name"])) - \
        len(pokemons_info["atk_trivia_points"]))) + "\n"
    msg += ((" " * 80) + "\n")
    msg += "4. Which one has the strongest defense:" + (" " * 41) + "\n"
    msg += (" " * 4) + ">" + pokemons_info["def_trivia_name"] + " with " + \
        pokemons_info["def_trivia_points"] + " defense points." + \
        (" " * ((53 - len(pokemons_info["def_trivia_name"])) - \
        len(pokemons_info["def_trivia_points"]))) + "\n"
    msg += ((" " * 80) + "\n")
    msg += "5. Which one is the fastest:" + (" " * 52) + "\n"
    msg += (" " * 4) + ">" + pokemons_info["spd_trivia_name"] + " with " + \
        pokemons_info["spd_trivia_points"] + " speed points." + \
        (" " * ((55 - len(pokemons_info["spd_trivia_name"])) - \
        len(pokemons_info["spd_trivia_points"]))) + "\n"
    msg += ((" " * 80) + "\n")
    msg += "Thanks for using this pokedex!" + (" " * 50) + "\n"
    msg += ((" " * 80) + "\n")    
    msg += (("=" * 80) + "\n")
    msg += ((" " * 80) + "\n")
    
    print(msg.format(**pokemons_info))
    
    core.save_data(msg,"trivia",id_number)
        