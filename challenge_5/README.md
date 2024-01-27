# 5th challenge: Dependencies aaaand Digimon!

## New data folder

The files were migrated to the root path, located at `data` to avoid having to duplicate those files on every new challenge.

## Digimon

As you were predicting, we will add support to both pokemons and digimons in your CLI.
For digimon the data will be under data/digimon. The battle logic will remain the same. The trivia will change a bit, now you will answer the following questions when someone choose the digimon option:

```
- How many digimons there is?
- How many different types there is?
- List of the strongest digimon, based on the attack attribute, per type:
    - Virus, Agumon (Blk), 5
    - Data, ...
```

In the digimon info menu, instead of `Legendaries`, you will have `Ultimate`.

Both info and battle menu don't need to inform the monster type in the CLI, you need to infer from filepath or the file structure.

```
python dex/main.py --player1 ../data/pokemon/json/pokemons_1.json --player2 ../data/digimon/json/digimons_2.json --id 1 --info
python dex/main.py --player1 ../data/pokemon/json/pokemons_1.json --player2 ../data/digimon/json/digimons_2.json --id 1 --battle
```

Your CLI will also change, first the name, `pokedex` now will turn into `dex`. Second, a new option will be added, to choose between pokemon or digimon, if no option is passed the default should be pokemon.


```
python dex/main.py --pokemon --trivia ../data/pokemon/json/pokemons_1.json --id 1
python dex/main.py --digimon --trivia ../data/digimon/json/digimon_1.json --id 1
```

If by mistake someone do the following:

```
python dex/main.py --pokemon --trivia ../data/digimon/json/digimon_1.json --id 1
```

Or:

```
python dex/main.py --digimon --trivia ../data/pokemon/json/pokemons_1.json --id 1
```

You will have to warn the user that he/she chose the incorrect option. You need to capture this by checking if the option is "--pokemon", than the file should have the "Legendary" field, and "Stage" field for "--digimon" option.

## Dependencies

Your `dex` is already using some external dependencies, let's organize them in a file called requirements.txt. This is a common practice so that newcomers install all the required libraries that your app uses. It's also used to control the versions of each library.

First create a file called `requirements.txt`, them add the libraries and versions:

```
xmltodict==0.13.0
pyyaml==6.0.1
```

Every new external library you add to your `dex` app you need to append to this file with the respectively version you used at the time you installed it.

Ps. I did not add flake8, mypy and black in the example above, but you should do it.

## Virtual environment

As you already know, python is used in many places in the operating system, so do its dependencies. To avoid having library conflicts it's a good practice to have an isolated environment to install your dependencies per different project. To understand better what is this "python virtual environment", please read the reference links in the bottom of this document.

Let's create one for the `dex`. First, decide which python version you will use in your virtual envionment since you can have one virtual envionment for each python version you use. Let's pretend that you will use Python 3.9.

To start a python virtual environment:

```sh
python3.9 -m venv venv-dex
```

When you run the command above a new folder will appear called `venv-dex`. Now you need to "activate" your virtual environment, in linux you can do this by running the following command:

```sh
source venv-dex/bin/activate
```

Now you are inside your python virtual enviroment. Let's install the dependencies you set in the previous section by running the command:

```
pip install -r requirements.txt
```

To run the dex:

```sh
python dex/main.py --help
```

To exit this virtual environment:

```sh
deactivate
```

## Good coding practices

As I said in the previous challenge, from now on we will verify whether you are following good coding practices, which means that it's REQUIRED to have both mypy and flake8 all green. To help you to fix some annoying issues, you can use the library called "black".

```sh
pip install black
black dex
```

## Configuration file

Let's ignore some of the rules from mypy that are not too relevant right now and setup flake8 properly. Please create a file called setup.cfg and write the following lines:

```cfg
[flake8]
max-line-length = 120
exclude = challenge_1,challenge_2,challenge_3,challenge_4,venv-dex,data

[mypy]
disable_error_code = import-untyped
```

Your directory tree should be looking like this now:

```
├── challenge_1
│   └── ...
├── challenge_2
│   └── ...
├── challenge_3
│   └── ...
├── challenge_4
│   └── ...
├── challenge_5
│   └── README.md
├── data
│   ├── digimon
│   │   └── ...
│   └── pokemon
│   │   └── ...
├── venv-dex
├── setup.cfg
├── overview.md
└── README.md
```

## References to study

- Virtual environments and dependencies: https://docs.python.org/3/tutorial/venv.html
- Configuration file: https://docs.python.org/3.9/distutils/configfile.html
- venv: https://docs.python.org/3/library/venv.html#module-venv
- black: https://black.readthedocs.io/en/stable/
- packages versions syntax: https://pip.pypa.io/en/stable/reference/requirement-specifiers/#examples
- dependencies resolution: https://pip.pypa.io/en/stable/topics/dependency-resolution/#dependency-resolution
- semantic versioning: https://semver.org/

## Skills

Skills to unlock:
- How to organize all your dependencies.
- Python virtual environment with venv.
- Package management with pip.
- Setup your configuration file.
- Generalize functions to be used in multiple scopes.

## Retrospective

TODO:
- Fix pokemon/digimon trivia, running json first and csv as second returns incorrect information, both should be similar.
- OVERWRITE by default is not working.
- Bug: KeyError: 'Type 1', from `python dex/main.py --pokemon --trivia ../data/pokemon/xml/pokemons_1.xml --id 1`.
- Bug: AttributeError: 'list' object has no attribute 'items', from `python dex/main.py --digimon --trivia ../data/digimon/xml/digimons_1.xml --id 1`.
- Fix 7Q on digimon trivia, it looks confusing.
- Bug: When we run --info the player 2 data is coming from the player 1 data.
- Battle is not working: `python dex/main.py --digimon --player1 ../data/pokemon/json/pokemons_1.json --player2 ../data/digimon/json/digimons_2.json --id 1 --battle`.

The good:
- Learn about the python basics for dependencies.
- She discovered by herself about lambda and she found that it's very useful.
- After a long holiday break we are back \o/.

The bad:
- Bugs.

## Dates

- 26/12/2023: Challenge 5th released.
- 13/01/2024: Challenge 5th review.
- Total days: 19.
