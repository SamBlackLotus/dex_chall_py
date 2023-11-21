import sys
import json

arguments = sys.argv[1]

with open((arguments), "r") as source_pokedex:
    data = json.load(source_pokedex)

#for pokemon in data:    
print('There are',len(data),'pokemon in the list.')    
    
#for pokemon in data:
    #print('\n id:',pokemon["id"],'\n name:',pokemon["name"],'\n base experience:'
          #,pokemon["base_experience"],'\n height:',pokemon["height"],'\n weight:'
          #,pokemon["weight"],'\n')
  
    
#1292 itens
#cada linha contém um pokemon com 5 infos [0-4]


### Information I want to see in the terminal:
#- How many pokemons there is?
    # Count how many lines of data the json will produce

#- Which one is the highest?
    # the highest what? base xp?
    
#- Which one is the heaviest?

#- Which one is more worthy of defeating based on the experience gained from defeating them?
    # the highest base xp
    
#- How many alola pokemons there is?


#- Is snorlax bigger than charizard?