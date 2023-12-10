# First challenge: Your first CLI

This step consist of building a cli that will read one argument from the terminal, the pokedex filename, read the file from that filename and show some aggregate information in the terminal.

The json file will be provided in the shared drive folder with the name: "pokemons.json".

Information I want to see in the terminal:
- How many pokemons there is?
- Which one is the highest?
- Which one is the heaviest?
- Which one is more worthy of defeating based on the experience gained from defeating them?
- How many alola pokemons there is?
- Is snorlax bigger than charizard?

Skills to unlock:
- How to parse arguments in the terminal
- Reading a file
- Reading a json file
- Working with the following data structures: list, dict
- Data aggregation
- Formatting strings

## Parsing arguments

```python
import sys

arguments = sys.argv
```

## Reading json files

```python
import json

with open(filename, "r") as source:
    data = json.load(source)
```

## Data

Each item in the list have a different pokemon, there are normal pokemons and alolas.

The columns descriptions and data types:
- id: The identifier for this resource. integer
- name: The name for this resource. string
- base_experience: The base experience gained for defeating this Pokémon. integer
- height: The height of this Pokémon in decimetres. integer
- weight: The weight of this Pokémon in hectograms. integer

## Retrospective

The good:
- Execute code from linux terminal.
- Learn about CLI.
- Read json and aggregate data.
- Exercise how to read and understand external code.
- Used fluxograms to understand the problem.

The bad:
- Difficulties on how to aggregate the data, it's not straightforward.
    - Translate the logic into an algorithm and later into python.
- Typing still too complex.
