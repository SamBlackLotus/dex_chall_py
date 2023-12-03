# Second challenge: More complex cli

This second challenge will challenge you in 3 news topics, the ability to read multiple files, you are going to read from csv instead of json, and you need to use **set** to do the logic (it's not optional).

Your podekex CLI will change a bit, it will receive 2 files containing pokedexes from 2 players, and you will offer the possibility to show their pokemon overall info or battle.

The new CLI interface needs to be the following:
```sh
python pokedex.py --player1 pokemons.csv --player2 pokemons.csv --info
python pokedex.py --player1 pokemons.csv --player2 pokemons.csv --battle
```
## Info 

For the info submenu it's expect to show the following information:
```sh
                   | Player 1            | Player 2            |
------------------ | -------------------- -------------------- |
pokemons           | 50                  | 2                   |
strongest pokemon  | charmander          | snorlax             |
legendaries        | 2                   | 0                   |
repeated pokemons  | 5                                         |
different pokemons | 50                                        |
------------------ | ----------------------------------------- |
```

Hint: You will use set data type to calculated the amount of repeated pokemons and the amount of different pokemons.

## Battle

To do the battle between the 2 players, the CLI will get the top 3 strongest pokemons based on the attribute "Attack". The battle will be performed among these 6 pokemons (3 from player 1 and 3 from player 2) until the first pokemon dies, each round one of the top pokemons will cause each other damage, the damage calculation is the following: 

```python
damage = (0.5 * (pokemon 1 attack/pokemon 2 defense) + 1
```

When the first pokemon dies the battle will be considered over and you will show the winner among the battle information: 

Expected output:
```python
----- Battle -----
Player 1 pokemons: TornadusTherian, Archeops, HoopaHoopa
Player 2 pokemons: Vulpix, Crobat, Pidgeot

----- Result -----
Winner: Player 1
Rounds: 50
Pokemon that died: Archeops
```

## References to study
- sets: https://realpython.com/python-sets/
- read csv: https://docs.python.org/3/library/csv.html

## Skills

Skills to unlock:
- Read multiple files
- Read csv files
- Working with the following data structures: set
