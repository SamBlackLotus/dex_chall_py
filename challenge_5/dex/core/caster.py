from typing import List, Set, SupportsIndex, Dict


def cast_to_set(file_set_1: Dict) -> Set:
    """
    This function converts a list to a set.

    Parameters
    ----------
    file_set_1:
        The data to be converted in set.

    Returns
    -------
    pokemon_set:
        The data in a set type.
    """
    monster_set: set = set()
    for monster in file_set_1:
        monster_set.add(monster["name"])
    return monster_set


def cast_to_int(value: SupportsIndex) -> int:
    """
    This function converts a list to integers.

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
    This function converts a list to bool.

    Parameters
    ----------
    Value:
        The list of strings to be converted.

    Returns
    -------
        The data as bool type.
    """
    return True if value == "True" else False


def cast_to_lower(value: List[str], monster_type: str) -> List[str]:
    """
    This function converts the list of variables
    to lower case and put them in a patterned keynames.

    Parameters
    ----------
    Value:
        The list to be converted.

    Returns
    -------
        The data in a lower case on a new dict.
    """
    change_dict = value
    new_dict = []

    if monster_type == "--pokemon":
        for key in change_dict:
            new_dict += [
                dict(
                    id=key["Id"],
                    name=key["Name"],
                    type1=key["Type 1"],
                    type2=key["Type 2"],
                    total=key["Total"],
                    hp=key["HP"],
                    attack=key["Attack"],
                    defense=key["Defense"],
                    spatk=key["Sp. Atk"],
                    spdef=key["Sp. Def"],
                    speed=key["Speed"],
                    generation=key["Generation"],
                    legendary=key["Legendary"],
                )
            ]
    elif monster_type == "--digimon":
        for key in change_dict:
            new_dict += [
                dict(
                    id=key["Id"],
                    name=key["Name"],
                    stage=key["Stage"],
                    type1=key["Type"],
                    attribute=key["Attribute"],
                    memory=key["Memory"],
                    equip=key["Equip Slots"],
                    hp=key["HP"],
                    sp=key["SP"],
                    attack=key["Atk"],
                    defense=key["Def"],
                    intelligence=key["Int"],
                    speed=key["Spd"],
                    image=key["Image link"],
                )
            ]

    return new_dict
