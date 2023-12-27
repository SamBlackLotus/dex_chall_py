from typing import List, Set


def cast_to_set(file_set_1: List[str]) -> Set:
    """
    This function receives data in any python types
    and turns into a set.

    Parameters
    ----------
    file_set_1:
        The data to be converted in set.

    Returns
    -------
    pokemon_set:
        The data in a set type.
    """
    pokemon_set: set = set()
    for pokemon in file_set_1:
        pokemon_set.add(pokemon["Name"])
    return pokemon_set


def cast_to_int(value: List[str]) -> List[int]:
    """
    This function converts a list of strings to
    integers.

    Parameters
    ----------
    Value:
        The list of strings to be converted.

    Returns
    -------
        The data as integer type.
    """
    return int(value) if value is not None else 0


def cast_to_bool(value: List[str]) -> List[bool]:
    """
    This function converts a list of strings
    to bool.

    Parameters
    ----------
    Value:
        The list of strings to be converted.

    Returns
    -------
        The data as bool type.
    """
    return True if value == "True" else False


def client_helper() -> None:

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
    return print(helper_msg)


# TODO: the correct trivia cmd is:
# python3 pokedex/main.py --trivia data/json/pokemons_1.json --id 1
def client_usage() -> None:
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
