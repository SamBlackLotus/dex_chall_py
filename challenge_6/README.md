# 6th challenge: Classes and objects

## Abstracting the main entities with classes

Let's try to abstract some concepts using object oriented programming.
Your CLI interacts with 3 main entities, monsters, teams and players.

When you read the pokemon.json/digimon.json file you are collecting each monster's attributes, and building a team that
belongs to a player.

- The monster contains some relevant data attributes, such as, monster category (pokemon/digimon), name, battle attributes and kind category (stages/types), etc.
- The team contains the reference of all the monsters that belongs to it, and you can also include the team name for example.
- The player contains the reference of it's team and the player identity (1/2/or can you even add a name to id).

Following the guidance above try to create the following classes:

```
class Monster:
    ...
```

```
class Team:
    ...
```

```
class Player:
    ...
```

## Abstracting info and battle with classes

To show the team information you will create an info method inside the team class, e.g.:

```
class Team:
    def info(self):
        print(...)

team_1 = Team()
team_1.info()
```

To execute the battle you will create a class called battle with the following interfaces:

```
class Battle:
    def __init__(self, player_1, player_2):
        ...

    def start(self):
        ....

    def show_result(self):
        ....

battle = Battle(p1, p2)
battle.start()
battle.show_result()
```

The battle information should be controlled inside of the battle instance, such as the players, total and current round and the winner.
To access the player's monsters you will need to access player_x.team.monsters (this will be a list of Monster).
You should add an attribute inside Monster's class to control the current hp that the monster has, so that you can check during the battle, e.g.:

```
monster = player_x.team.monsters[idx]
monster.current_hp -= N
```

ps. be careful with class variables and instance variables.

## References to study

- Python classes [THIS IS A MUST]: https://docs.python.org/3.9/tutorial/classes.html
- Simple tutorial: https://www.youtube.com/watch?v=wfcWRAxRVBA

## Skills

Skills to unlock:
- Understand the concept of classes and objects.
- Transform some data structure and functions to classes/instances.

## Retrospective

TODO:
- 

The good:
- 

The bad:
- 
