import core
import menu
import sys
from typing import List, Dict, Any, Set


# TODO: remove the parameters description since there
# are no args in the function, and also the returns
# TODO: don't use Any
def main() -> None:
    """
    This function receive arguments from CLI and process it to calls
    all the system functions.

    Parameters
    ----------
    user_input:
        The command given by the user in the CLI interface, it will
        come as a list.

    arguments:
        This variable will receive the list provided in user_input
        and slice it into positional arguments, where each one calls
        a different action.

    Returns
    -------
    The function return will be a call for another function based on
    the command given by the user and processed by this function.

    """
    user_input: List[str] = sys.argv
    arguments: List[str] = core.file_validator(user_input)

    if arguments[0] == "--help":
        core.client_helper()
        quit()

    elif arguments[0] == "--trivia":
        id_number: str = arguments[2]
        data_1: List[Dict[str, int]] = core.read_file(arguments[1])
        info: Any = menu.pokemon_trivia(data_1)
        menu.show_trivia(info, id_number)
        quit()

    elif arguments[0] == "--player1":

        id_number: str = arguments[2]
        data_1: List[Dict[str, int]] = core.read_file(arguments[1])
        dataset_1: Set[str] = core.cast_to_set(data_1)
        data_2: List[Dict[str, int]] = core.read_file(arguments[4])
        dataset_2: Set[str] = core.cast_to_set(data_2)

        if arguments[5] == "--info" or arguments[6] == "--info":
            info: Any = menu.process_info(data_1, data_2, dataset_1, dataset_2)
            menu.show_info(info, id_number)
            quit()
        elif arguments[5] == "--battle" or arguments[6] == "--battle":
            battle: Any = menu.select_pokemons_for_battle(data_1, data_2)
            result: Any = menu.pokemon_battle(battle)
            menu.show_battle_winner(battle, result, id_number)
            quit()


if __name__ == "__main__":
    main()
