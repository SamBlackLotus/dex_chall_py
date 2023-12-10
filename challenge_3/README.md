# Third challenge: Read any file format and CRUD on a file

The info and the battle logic should remain the same.

## Read any file format

Since now you know how to handle CSV and JSON files, now you need to add support to 2 more file formats: XML and YAML.

Your cli needs to read properly the input file based on the format.
For example the CLI can be called in the following ways:

```sh
python pokedex.py --player1 pokemons_1.csv --player2 pokemons_2.json --info
```

```sh
python pokedex.py --player1 pokemons_1.yaml --player2 pokemons_2.csv --info
```

```sh
python pokedex.py --player1 pokemons_1.xml --player2 pokemons_2.xml --info
```

### XML

To work with xml files you will need to install the library [xmltodict](https://pypi.org/project/xmltodict/), use pip to do that:

```sh
pip install xmltodict
```

To use:
```
import xmltodict
```

### YAML

To work with yaml files you will need to install the library [pyyaml](https://pypi.org/project/PyYAML/), use pip to do that:

```sh
pip install pyyaml
```

To use:
```
import pyyaml
```

## CRUD on a file

CRUD means: Create, Read, Update and Delete, so far you have been exercising only the R of this acronym, but let's start exercising the other letters.
All the --info and --battle results should be written into a file called, [ID]_info.txt and [ID]_battle.txt respectively. 

The ID will be informed in the CLI as following:

```sh
python pokedex.py --player1 pokemons_1.csv --player2 pokemons_2.json --id 1 --info
```

If no ID is provided, the default ID will be 0.

If those files already exists, communicate with the user with the following message:

```
Files 5_info.txt and 5_battle.txt already exists, what do you prefer to do? [append|OVERWRITE] : 
```

You should collect one letter or a word as input: a, append, o, overwrite.
If the user just hits enter, the default answer should be "overwrite".
If the answer is o or overwrite, remove the files and generate the new report.

### Append to a file

If the answer is a or append, you need to append the results in the same file, for example: 

```
reported generated on: 2023-12-10T15:21:32.319039
                   | PLAYER 1            | PLAYER 2            |
------------------ | -------------------- -------------------- |
Pokémons           |300                  |300                  |
Strongest Pokémon  |GroudonPrimal Groudon|DeoxysAttack Forme   |
Legendaries        |26                   |26                   |
Repeated Pokemons  |112                                        | 
Different Pokemons |188                                        |
------------------ | ----------------------------------------- |

reported generated on: 2023-12-10T15:21:50.755554
                   | PLAYER 1            | PLAYER 2            |
------------------ | -------------------- -------------------- |
Pokémons           |300                  |300                  |
Strongest Pokémon  |GroudonPrimal Groudon|DeoxysAttack Forme   |
Legendaries        |26                   |26                   |
Repeated Pokemons  |112                                        | 
Different Pokemons |188                                        |
------------------ | ----------------------------------------- |
```

The datetime should be generated in the ISO format.

Appeding a file is similar to the read operation, but you use "a" instead of "r".

```python
with open("5_info.txt", "a") as target:
    target.write(value)
```

### Verify if a file exists and remove a file

To verify is a file exists and/or remove a file you can use the built-in python library called "os", e.g.:

- File exists
```py
import os
os.path.exists("5_info.txt")
```

- Remove
```py
import os
os.remove("5_info.txt")
```

### Create a file

Creating a file is similar to the read operation, but you use "w" instead of "r".

```py
with open("5_info.txt", "w") as target:
    target.write(value)
```

## Good practices

From now on let's exercise good coding practices, such as:
- More functions with more granular logic.
- Comments in more complex logic, such as the battle one.
- Data structures that represents only the input and the output data, being less generic.

## References to study
- read xml: https://github.com/martinblech/xmltodict
- read yaml: https://pyyaml.org/wiki/PyYAMLDocumentation
- file operations:
    - https://docs.python.org/3/library/functions.html#open
    - https://docs.python.org/3/tutorial/inputoutput.html#tut-files
- datetime library: https://docs.python.org/3/library/datetime.html
- ISO format: https://www.iso.org/iso-8601-date-and-time-format.html

## Skills

Skills to unlock:
- Read 2 more file formats: xml, yaml.
- Learn how to remove, write and edit a file.
- Collect user input.
- Use datetime library.
- ISO format.
- Install your first external library using pip.

## Retrospective

TODO
