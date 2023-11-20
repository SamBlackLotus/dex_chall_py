import sys
import json

arguments = sys.argv

with open("pokemons.json", "r") as source_pokedex:
    data = json.load(source_pokedex)
    
for pokemon in data:
    print(pokemon)
    
#1292 itens
#cada linha contém um pokemon com 5 infos [0-4]
