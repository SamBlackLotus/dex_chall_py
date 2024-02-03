import core
import menu
import sys
import os


def main() -> None:

    if len(sys.argv) == 1:
        print(core.client_usage())
        quit()

    command_1 = sys.argv[1]
    if command_1 == "--help":
        if len(sys.argv) == 2:
            print(core.client_helper())
            quit()

        else:
            print(f"WARNING! Incorrect amount of arguments.\n{core.client_usage()}")
            quit()

    elif command_1 == "--trivia":
        if len(sys.argv) == 3:
            filepath_1 = sys.argv[2]
            if not os.path.exists(filepath_1):
                print(f"WARNING: File {filepath_1} does not exist.")
                quit()

        elif len(sys.argv) == 5:
            command_3 = sys.argv[3]
            if command_3 == "--id":
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

        data_arq1 = core.read_file(filepath_1)
        if "pokemon" in filepath_1:
            data_1 = core.cast_to_lower(data_arq1, "pokemon")
            info = menu.pokemon_trivia(data_1)
            core.show_pokemon_trivia(info, id_number)
            quit()

        elif "digimon" in filepath_1:
            data_1 = core.cast_to_lower(data_arq1, "digimon")
            info = menu.digimon_trivia(data_1)
            core.show_digimon_trivia(info, id_number)
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
                filepath_2 = sys.argv[4]
                if not os.path.exists(filepath_2):
                    print(f"WARNING: File {filepath_2} does not exist.")
                    quit()

        else:
            print(f"WARNING: This command does not exist.\n{core.client_usage()}")
            quit()

        command_3 = sys.argv[5]
        command_4 = "0"

        if command_3 == "--id":
            if len(sys.argv) == 8:
                id_number = sys.argv[6]
                command_4 = sys.argv[7]

            else:
                print(f"WARNING! Incorrect amount of arguments.\n{core.client_usage()}")
                quit()

        elif command_3 != "--info" or command_3 != "--battle":
            print(f"WARNING: This command does not exist.\n{core.client_usage()}")
            quit()

        if "pokemon" in filepath_1:
            monster_type1 = "pokemon"
            if "pokemon" in filepath_2:
                monster_type2 = "pokemon"
            elif "digimon" in filepath_2:
                print(f"WARNING: Different type of monsters.\n{core.client_usage()}")
                quit()
        elif "digimon" in filepath_1:
            monster_type1 = "digimon"
            if "pokemon" in filepath_2:
                print(f"WARNING: Different type of monsters.\n{core.client_usage()}")
                quit()
            elif "digimon" in filepath_2:
                monster_type2 = "digimon"

        data_arq1 = core.read_file(filepath_1)
        data_arq2 = core.read_file(filepath_2)
        data_1 = core.cast_to_lower(data_arq1, monster_type1)
        data_2 = core.cast_to_lower(data_arq2, monster_type2)

        if command_3 == "--info" or command_4 == "--info":
            dataset_1 = core.cast_to_set(data_1)
            dataset_2 = core.cast_to_set(data_2)
            info = menu.process_info(data_1, data_2, dataset_1, dataset_2, monster_type1, monster_type2)
            core.show_info(info, id_number, monster_type1)
            quit()
        elif command_3 == "--battle" or command_4 == "--battle":
            team_size: int = int(input("How many monsters will participate the battle? "))
            battle = menu.select_battle_team(data_1, data_2, team_size)
            result = menu.start_battle(battle, team_size)
            core.show_battle_winner(result, id_number)
            quit()

    else:
        print(f"WARNING: This command does not exist.\n{core.client_usage()}")
        quit()


if __name__ == "__main__":
    main()
