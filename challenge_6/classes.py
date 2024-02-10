class Monster:
    def __init__(self, category, id, name, stage, type, generation, legendary, hp, attack, defense, speed):
        self.category = category
        self.id = id
        self.name = name
        self.stage = stage
        self.type = type
        self.generation = generation
        self.legendary = legendary
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed

    def info_self(self):
        print("INFO CARD", "\n"
              "Id:" + self.id, "\n"
              "Name:" + self.name, "\n"
              "Stage:" + self.stage, "\n"
              "Type:" + self.type, "\n"
              "Generation:" + self.generation, "\n"
              "Legendary:" + self.legendary, "\n"
              "HP:" + self.hp, "\n"
              "Attack:" + self.attack, "\n"
              "Defense:" + self.defense, "\n"
              "Speed:" + self.speed, "\n")


digimon = Monster("Digimon", "5", "Poyomon", "Baby", "Free", "null", "null", "540", "54", "59", "86")

pokemon = Monster("Pokemon", "255", "Torchic", "null", "null", "3", "No", "45", "60", "40", "45")

digimon.info_self()
pokemon.info_self()

# class Team:
#     def

# class Player:
#     def

# class Battle:

# player_1 = Player()
# player_1.strongest_monster = {"index": 0, "value": 0}
# player_1.total_ult_or_legend = {"index": 0, "value": 0}
# player_1.monster_dict = {"index": 0, "value": 0}

# player_2 = Player()
# player_2.strongest_monster = {"index": 0, "value": 0}
# player_2.total_ult_or_legend = {"index": 0, "value": 0}
# player_2.monster_dict = {"index": 0, "value": 0}
