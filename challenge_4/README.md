# 4th challenge: Let's organize the logic and the code

The trivia, info and the battle logic should remain the same.

## Docstring

There are 2 famous types of docstring, google and numpy. Choose one and document your code.
Example using numpy docstring:

```python
def read_yaml_file(filepath: str) -> List[Dict[str, str]]:
    """This function reads a YAML file.
    It uses the safe load to load the yaml.

    Parameters
    ----------
    filepath:
        The file path, it can be the full path or relative path.
    
    Returns
    -------
    data:
        The yaml data in python data types. 
    """

    with open(filepath, "r") as source:
        data = yaml.safe_load(source.read())
        return data
```

## Typing

Add typing to all your functions. To verify whether your code is using typing correctly we will verify it using mypy.
To use mypy you need to install it first:

```sh
> pip install mypy
```

To run mypy with you code:

```sh
> mypy pokedex
```

Fix all issues until a green message appears, example:

```
> Success: no issues found in X source files
```

You already have been using the `typing` library, now you will need to extend to other types, example:

```python
from typing import List, Dict, Set

def process_info(
    pokemon_set_1: Set[str],
    pokemon_set_2: Set[str]
):
    intersec_pokemon: Set[str] = (pokemon_set_1.intersection(pokemon_set_2))
    diff_pokemon: Set[str] = (pokemon_set_1.difference(pokemon_set_2)) 

```

## Custom module

The file `pokedex_crud.py` that you produced in the last challenge became big and complex, let's focus on breaking down into different files.
This code is doing 3 core logic, trivia, info and battle, how about you create a file for each one of those.
Also, try to separate your parser into a new file too.

Ideally you would have the following module structure:

```
├── pokedex
│   ├── __init__.py
│   ├── main.py
│   ├── menu
│   │   ├── __init__.py
│   │   ├── trivia.py
│   │   ├── info.py
│   │   └── battle.py
│   └── core
│       ├── __init__.py
│       ├── parser.py
│       └── io.py
└── data
    ├── csv
    │   ├── pokemons_1.csv
    │   └── pokemons_2.csv
    ├── json
    │   ├── pokemons_1.json
    │   └── pokemons_2.json
    ├── xml
    │   ├── pokemons_1.xml
    │   └── pokemons_2.xml
    └── yaml
        ├── pokemons_1.yaml
        └── pokemons_2.yaml
```

In your main.py you would import the new module like this:

```python
from pokedex.menu.trivia import process_trivia
from pokedex.core.io import read_file_yaml
```

To create a module you need to create a folder and add a `__init__.py` in it.
Explanation about it: https://docs.python.org/3/tutorial/modules.html#packages.

## Good coding practices

From now on let's exercise good coding practices, such as:

- More functions with more granular logic, e.g. the `main` function is too big.
- Improve variable names with more meaning, for example `process_poke1` is not a good name because it does not help to identify what is in this variable.
- Add docstring to all functions.
- Data structures that represents only the input and the output data, being less generic, e.g. `Answers` is too generic.
- Don't use more than 120 columns.
- Don't mix multiple languages, if we are using english, use only this one across all the codebase.
- Review your english grammar and vocabulary in the comments to avoid typos, as a suggestion add an english spell check addon on vscode (Code Spell Checker).

There is also another library that can help you identify style problems, let's use `flake8`:

```sh
> pip install flake8
```

How to use it:

```sh
flake8 pokedex
```

Try to fix all the issues reported.

## References to study
- docstrings: https://peps.python.org/pep-0257/
- numpy docstring: https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard
- google docstring: https://google.github.io/styleguide/pyguide.html
- typing: https://docs.python.org/3/library/typing.html
- mypy: https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
- modules: https://docs.python.org/3/tutorial/modules.html
- variable names: https://www.w3docs.com/learn-python/variable-names.html
- flake8: https://flake8.pycqa.org/en/latest/

## Skills

Skills to unlock:
- Create your our module and import it.
- Docstrings.
- Typing.
- Good coding practices.
- Use static python analyzer tools.

## Retrospective

The good:
- Flake8 is helpful to guide to write a clean code.
- Have a separate file to add types.

The bad:
- Mypy is not intuitive for beginners.
