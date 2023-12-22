import core
import json
import csv
import xmltodict
import yaml
from typing import Dict, Union, List, Any


def read_file(filepath: str) -> List[Dict[str, Union[str, int]]]:
    """
    This function receaves a file from main an based on the format
    it will fit in one of the conditionals.

    If its a .json it uses load.
    If its a .csv it uses DictReader.
    If its a .xml it uses xmltodict.
    If its a .yaml it uses safe load.

    Parameters
    ----------
    filepath:
        The file path, it can be the full path or relative path.

    Returns
    -------
    data:
        The file received will be returned in python data types.
    """
    with open((filepath), "r") as source_pokedex:
        if ".json" in filepath:
            return json.load(source_pokedex)
        elif ".csv" in filepath:
            file: Dict[str, Any] = csv.DictReader(source_pokedex, delimiter=",")
            pokemons: List[str] = [row for row in file]
            return pokemons
        elif ".xml" in filepath:
            file: Dict[str, Any] = source_pokedex.read()
            pokemonsxml: Dict[str, Any] = xmltodict.parse(file)
            pokemonsid: Dict[Any] = {key: value for key, value in pokemonsxml['root'].items()}
            pokemons: List[str] = []
            for key, value in pokemonsid.items():
                pokemons += [{a: i for a, i in value.items()}]
            return pokemons
        elif ".yaml" in filepath:
            file = source_pokedex.read()
            pokemons = yaml.safe_load(file)
            return pokemons
        else:
            print(f"Error: File format not supported!\n{core.client_usage()}")
            quit()
