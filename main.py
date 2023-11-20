import sys
import json

arguments = sys.argv

with open("pokemons.json", "r") as source_pokedex:
    data = json.load(source_pokedex)
    #print(len(data))
    
for pokemon in data:
    print(len(pokemon))