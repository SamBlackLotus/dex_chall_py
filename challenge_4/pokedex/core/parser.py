import core
import json
import csv
import xmltodict
import yaml

#Receive and read json files 
def read_file(filepath): 
    with open((filepath), "r") as source_pokedex:
        if ".json" in filepath:
            return json.load(source_pokedex)
        elif ".csv" in filepath:
            file = csv.DictReader(source_pokedex, delimiter = ",")
            pokemons = [row for row in file]
            return pokemons
        elif ".xml" in filepath:
            file = source_pokedex.read()
            pokemonsxml = xmltodict.parse(file)
            pokemonsid = {key: value for key, value in pokemonsxml['root'].items()}
            pokemons= []
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