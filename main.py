import sys
import json
import math



arguments = sys.argv[1]

with open((arguments), "r") as source_pokedex:
    data = json.load(source_pokedex)


#for pokemon in enumerate(data):
    #print(pokemon)


for pokemon in data:

    id_list = [pokemon["id"] for pokemon in data]    
    name_list = [pokemon["name"] for pokemon in data]
    base_experience_list = [pokemon["base_experience"] for pokemon in data]    
    height_list = [pokemon["height"] for pokemon in data]
    weight_list = [pokemon["weight"] for pokemon in data]


highest_pokemon = max(height_list)
heaviest_pokemon = max(weight_list)
#most_worthy = max(base_experience_list)
    
     

print('There are',len(data),'pokemon in the list.')  
print(f'The highest pokemon is ',{highest_pokemon})
print(f'The heaviest pokemon is ',{heaviest_pokemon})
#print(f'The most worthy pokemon to defeat is ',{most_worthy})
#print('There are',(),'alola pokemon')
#Is snorlax bigger than charizard?
    
#for pokemon in data:
    #print('\n id:',pokemon["id"],'\n name:',pokemon["name"],'\n base experience:'
          #,pokemon["base_experience"],'\n height:',pokemon["height"],'\n weight:'
          #,pokemon["weight"],'\n')