import core
import os


# TODO: add returns type
# TODO: add sys.argv here since you dont use it on main
# TODO: avoid redundant logic, if you are checking the
# main commands on main, you should not do it again here
# or vice versa, try to break the logic per each menu, e.g.
# core.trivia()
def file_validator(user_input: str) -> None:
    """
    This function receives the "sys.argv" input, and use it to validate
    and define which path the main function shall run and in cases the input
    has errors the client_usage function is called, with the information on
    how to use the input, which will be printed on the CLI interface alongside
    the type of error that ocurred.

    Parameters
    ----------
    user_input
        The file path, it can be the full path or relative path.

    Returns
    -------
    List of arguments:
        The function will return a list of variables, according to the if path.
    """

    if len(user_input) == 1:
        print(core.client_usage())
        quit()

    command_1: str = user_input[1]

    if command_1 == "--help":
        if len(user_input) == 2:
            return [command_1]
        else:
            print(f"WARNING! Incorrect amount of arguments.\n{core.client_usage()}")
            quit()

    elif command_1 == "--trivia":
        if len(user_input) == 3:
            filepath_1: str = user_input[2]
            if not os.path.exists(filepath_1):
                print(f"WARNING: File {filepath_1} does not exist.")
                quit()

            id_number: int = 0

        elif len(user_input) == 5:
            command_2: str = user_input[3]
            if command_2 == '--id':
                id_number: int = user_input[4]
            else:
                print(f"WARNING: This command does not exist.\n{core.client_usage()}")
                quit()

            filepath_1: str = user_input[2]
            if not os.path.exists(filepath_1):
                print(f"WARNING: File {filepath_1} does not exist.")
                quit()
        else:
            print(f"WARNING! Incorrect amount of arguments.\n{core.client_usage()}")
            quit()

        return [command_1, filepath_1, id_number]

    elif command_1 == "--player1":
        if len(user_input) <= 5:
            print(f"WARNING! Incorrect amount of arguments.\n{core.client_usage()}")
            quit()

        filepath_1: str = user_input[2]
        if not os.path.exists(filepath_1):
            print(f"WARNING: File {filepath_1} does not exist.")
            quit()

        command_2: str = user_input[3]

        if command_2 == "--player2":
            if len(user_input) >= 6:
                filepath_2: str = user_input[4]
                if not os.path.exists(filepath_2):
                    print(f"WARNING: File {filepath_2} does not exist.")
                    quit()

        else:
            print(f"WARNING: This command does not exist.\n{core.client_usage()}")
            quit()

        command_3: str = user_input[5]
        command_4: int = 0

        if command_3 == "--id":
            if len(user_input) == 8:
                id_number: int = user_input[6]
                command_4: int = user_input[7]

            else:
                print(f"WARNING! Incorrect amount of arguments.\n{core.client_usage()}")
                quit()

        elif command_3 == "--info" or command_3 == '--battle':
            id_number: int = 0

        else:
            print(f"WARNING: This command does not exist.\n{core.client_usage()}")
            quit()

        return [command_1, filepath_1, id_number, command_2, filepath_2, command_3, command_4]

    else:
        print(f"WARNING: This command does not exist.\n{core.client_usage()}")
        quit()
