import core
import menu
import sys
import os
from typing import List, Dict, Any, Set


def main() -> None:
    """
    This function receive sys.argv from CLI and process it to calls
    all the system functions.

    Parameters
    ----------
    sys.argv:
        The command given by the user in the CLI interface, it will
        come as a list.

    sys.argv:
        This variable will receive the list provided in sys.argv
        and slice it into positional sys.argv, where each one calls
        a different action.

    Returns
    -------
    The function return will be a call for another function based on
    the command given by the user and processed by this function.

    """

    if len(sys.argv) == 1:
        print(core.client_usage())
        quit()

    command_1: str = sys.argv[1]

    if command_1 == "--help":
        if len(sys.argv) == 2:
            print(core.client_helper())
            quit()

        else:
            print(f"WARNING! Incorrect amount of arguments.\n{core.client_usage()}")
            quit()

    elif command_1 == "--trivia":
        if len(sys.argv) == 3:
            filepath_1: str = sys.argv[2]
            if not os.path.exists(filepath_1):
                print(f"WARNING: File {filepath_1} does not exist.")
                quit()

            id_number: int = 0

        elif len(sys.argv) == 5:
            command_2: str = sys.argv[3]
            if command_2 == "--id":
                id_number = sys.argv[4]

            else:
                print(f"WARNING: This command does not exist.\n{core.client_usage()}")
                quit()

            filepath_1 = sys.argv[2]
            if not os.path.exists(filepath_1):
                print(f"WARNING: File {filepath_1} does not exist.")
                quit()

        else:
            print(f"WARNING! Incorrect amount of arguments.\n{core.client_usage()}")
            quit()

        data_1: List[Dict[str, int]] = core.read_file(sys.argv[2])
        info = menu.pokemon_trivia(data_1)
        core.show_pokemon_trivia(info, id_number)
        quit()

    elif command_1 == "--player1":
        if len(sys.argv) <= 5:
            print(f"WARNING! Incorrect amount of arguments.\n{core.client_usage()}")
            quit()

        filepath_1 = sys.argv[2]
        if not os.path.exists(filepath_1):
            print(f"WARNING: File {filepath_1} does not exist.")
            quit()

        command_2 = sys.argv[3]

        if command_2 == "--player2":
            if len(sys.argv) >= 6:
                filepath_2: str = sys.argv[4]
                if not os.path.exists(filepath_2):
                    print(f"WARNING: File {filepath_2} does not exist.")
                    quit()

        else:
            print(f"WARNING: This command does not exist.\n{core.client_usage()}")
            quit()

        command_3: str = sys.argv[5]
        command_4: int = 0

        if command_3 == "--id":
            if len(sys.argv) == 8:
                id_number = sys.argv[6]
                command_4 = sys.argv[7]

            else:
                print(f"WARNING! Incorrect amount of arguments.\n{core.client_usage()}")
                quit()

        elif command_3 == "--info" or command_3 == "--battle":
            id_number = 0

        else:
            print(f"WARNING: This command does not exist.\n{core.client_usage()}")
            quit()

        data_1 = core.read_file(filepath_1)
        dataset_1: Set[str] = core.cast_to_set(data_1)
        data_2: List[Dict[str, int]] = core.read_file(filepath_2)
        dataset_2: Set[str] = core.cast_to_set(data_2)

        if command_3 == "--info" or command_4 == "--info":
            info = menu.process_info(data_1, data_2, dataset_1, dataset_2)
            core.show_info(info, id_number)
            quit()
        elif command_3 == "--battle" or command_4 == "--battle":
            battle = menu.select_pokemons_for_battle(data_1, data_2)
            result = menu.pokemon_battle(battle)
            core.show_battle_winner(result, id_number)
            quit()

    else:
        print(f"WARNING: This command does not exist.\n{core.client_usage()}")
        quit()


if __name__ == "__main__":
    main()
