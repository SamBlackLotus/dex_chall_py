#Process the information read in the files and generate the info table 
def process_info(process_poke1,process_poke2,pokemon_set_1,pokemon_set_2):
    
    strongest_p1 = {"index": 0, "value": 0}
    strongest_p2 = {"index": 0, "value": 0}
    legendary_1 = 0
    legendary_2 = 0
    tot_leg_1 = 0
    tot_leg_2 = 0
    intersec_pokemon = (pokemon_set_1.intersection(pokemon_set_2))
    diff_pokemon = (pokemon_set_1.difference(pokemon_set_2)) 
    
    
    
    for index, pokemon in enumerate(process_poke1):
        p1_total = len(process_poke1)
        
        attack = cast_to_int(pokemon["Attack"])
        if attack > strongest_p1["value"]:
            strongest_p1["index"] = index
            strongest_p1["value"] = attack
        
        legendary_1 = cast_to_bool(pokemon["Legendary"])     
        if legendary_1 == True:
            tot_leg_1 +=1  
        
             
    for index, pokemon in enumerate(process_poke2):
        p2_total = len(process_poke2) 
        
        attack = cast_to_int(pokemon["Attack"])
        if attack > strongest_p2["value"]:
            strongest_p2["index"] = index
            strongest_p2["value"] = attack

        legendary_2 = cast_to_bool(pokemon["Legendary"])
        if legendary_2 == True:
            tot_leg_2 +=1   
            
         
                     
  
    return Answers(
        
        p1_tot_info = p1_total,
        p2_tot_info = p2_total,
        strgst_p1_info = process_poke1[strongest_p1["index"]]["Name"],
        strgst_p2_info = process_poke2[strongest_p2["index"]]["Name"],
        leg_1_info = tot_leg_1,
        leg_2_info = tot_leg_2,
        rep_pok_info = len(intersec_pokemon),
        diff_pok_info = len(diff_pokemon)
         
         
)
    
#Show the information gathered in the info process function
def show_info(process_pokemons, idnumber):
    
    datenow =  datetime.now()
    msg =  "                                                                 \n"
    msg += "reported generated on:   " + datenow.isoformat() + "                                                  \n"
    msg += "========================= POKEMON INFO ==========================\n"
    msg += "|                   | PLAYER 1            | PLAYER 2            |\n"
    msg += "|------------------ | -------------------- -------------------- |\n"
    msg += "|Pokémons           |" + str(process_pokemons["p1_tot_info"]) + "                  |" + str(process_pokemons["p2_tot_info"]) + "                  |\n"
    msg += "|Strongest Pokémon  |" + process_pokemons["strgst_p1_info"] + "|" + process_pokemons["strgst_p2_info"] + "   |\n"
    msg += "|Legendaries        |" + str(process_pokemons["leg_1_info"]) + "                   |" + str(process_pokemons["leg_2_info"]) + "                   |\n"
    msg += "|Repeated Pokemons  |" + str(process_pokemons["rep_pok_info"]) + "                                        |\n"
    msg += "|Different Pokemons |" + str(process_pokemons["diff_pok_info"]) + "                                        |\n"
    msg += "|------------------ | ----------------------------------------- |\n"
    msg += "=================================================================\n"
    msg += "                                                                 \n"
    
    if os.path.exists(f"{idnumber}_info.txt"):
        
        choice = input(f"Files {idnumber}_info.txt already exists, what do you prefer to do? [append|OVERWRITE] : ")
        
        if choice == 'o' or choice == 'O' or choice == 'Overwrite' or choice == 'overwrite' or choice == 'OVERWRITE' or choice == '':
           
            os.remove(f"{idnumber}_info.txt")
            
            with open(f"{idnumber}_info.txt", "w") as target:
                target.write(msg)
        elif choice == 'a' or choice == 'A' or choice == 'Append' or choice == 'append' or choice == 'APPEND':
           
            with open(f"{idnumber}_info.txt", "a") as target:
                target.write(msg)  
        else:
            print(f"WARNING: Invalid Input.\n{client_usage()}")
            quit()
              
    else:
        
        with open(f"{idnumber}_info.txt", "w") as target:
            target.write(msg)
    
    print(msg.format(**process_pokemons))
    


info = process_info(data_1,data_2,dataset_1,dataset_2)
                    show_info(info,idnumber)    