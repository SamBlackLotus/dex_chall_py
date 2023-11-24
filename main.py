import sys
import json
import math



arguments = sys.argv[1]

with open((arguments), "r") as source_pokedex:
    data = json.load(source_pokedex)

for pokemon in enumerate(data):

    id_list = [pokemon["id"] for pokemon in data]    
    name_list = [pokemon["name"] for pokemon in data]
    base_experience_list = [pokemon["base_experience"] for pokemon in data if pokemon["base_experience"] is not None]    
    height_list = [pokemon["height"] for pokemon in data]
    weight_list = [pokemon["weight"] for pokemon in data]
    alola_list = [pokemon["name"] for pokemon in data if "-alola" in pokemon["name"]]

highest_pokemon = max(height_list)
heaviest_pokemon = max(weight_list)
most_worthy = max(base_experience_list)
alola_list = len(alola_list)


print('There are',len(data),'pokemon in the list.')  
print(f'The highest pokemon is',data[1206]["name"])
print(f'The heaviest pokemon is ',data[1211]["name"])
print(f'The most worthy pokemon to defeat is',data[241]["name"])
print('There are',alola_list,'alola pokemon')



charizard = data[5]["height"]
snorlax = data[142]["height"]

if snorlax > charizard:
    answer = "Yes"
else:
    answer = "No"    

print('Is snorlax bigger than charizard?', answer)
 
#for pokemon in data:
    #print('\n id:',pokemon["id"],'\n name:',pokemon["name"],'\n base experience:'
          #,pokemon["base_experience"],'\n height:',pokemon["height"],'\n weight:'
          #,pokemon["weight"],'\n')