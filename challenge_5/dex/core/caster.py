from typing import List, Set, SupportsIndex, Dict


def cast_to_set(file_set_1: Dict) -> Set:
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


def cast_to_int(value: SupportsIndex) -> int:
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


def cast_to_bool(value: List[str]) -> bool:
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
