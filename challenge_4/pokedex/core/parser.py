import json
import csv
import xmltodict
import yaml

#Receive and read json files 
def read_file_json(filepath): 
    with open((filepath), "r") as source_pokedex:
        return json.load(source_pokedex)
    
#Receive and read csv files       
def read_file_csv(filepath):
    with open(filepath, "r") as data:
        file = csv.DictReader(data, delimiter = ",")
        pokemons = [row for row in file]
        return pokemons

#Receive and read xml files
# TODO: don't mix portuguese with english
def read_file_xml(filepath): 
    with open(filepath, "r") as data:
        file = data.read()
        pokemonsxml = xmltodict.parse(file)
        pokemonsid = {chave: valor for chave, valor in pokemonsxml['root'].items()}
        pokemons= []
        for chave, valor in pokemonsid.items():
            pokemons += [{a: i for a, i in valor.items()}]
    return pokemons

#Receive and read yaml files 
def read_file_yaml(filepath):
    with open(filepath, "r") as data:
        file = data.read()
        pokemons = yaml.safe_load(file)
        return pokemons