import random

class Enemy():
    def __init__(self, name, maxhealth, health, attack, goldgain):
        self.name = name
        self.maxhealth = maxhealth
        self.health = self.maxhealth
        self.attack = attack
        self.goldgain = goldgain

class Goblin(Enemy):
    def __init__(self, name, maxhealth, health, attack, goldgain):
        super().__init__(name, maxhealth, health, attack, goldgain)

class Slime(Enemy):
    def __init__(self, name, maxhealth, health, attack, goldgain):
        super().__init__(name, maxhealth, health, attack, goldgain)

class Knight(Enemy):
    def __init__(self, name, maxhealth, health, attack, goldgain):
        super().__init__(name, maxhealth, health, attack, goldgain)

class Zombie(Enemy):
    def __init__(self, name, maxhealth, health, attack, goldgain):
        super().__init__(name, maxhealth, health, attack, goldgain)

class Mark(Enemy):
    def __init__(self, name, maxhealth, health, attack, goldgain):
        super().__init__(name, maxhealth, health, attack, goldgain)

class True_Mark(Enemy):
    def __init__(self, name, maxhealth, health, attack, goldgain):
        super().__init__(name, maxhealth, health, attack, goldgain)



""" class Goblin():
    def __init__(self):
        self.name = ["Goblin"]
        self.maxhealth = 80
        self.health = self.maxhealth
        self.attack = 7
        self.goldgain = random.randint(5,15)

class Slime():
    def __init__(self):
        self.name = ["Slime"]
        self.maxhealth = 50
        self.health = self.maxhealth
        self.attack = 5
        self.goldgain = random.randint(1,10)

class Knight():
    def __init__(self):
        self.name = ["Knight"]
        self.maxhealth = 140
        self.health = self.maxhealth
        self.attack = 15
        self.goldgain = random.randint(25,50)
        self.weapon = ["Sword"]

class Zombie():
    def __init__(self, name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.attack = 12
        self.goldgain = random.randint(10,25)

class Mark():
    def __init__(self, name):
        self.name = name
        self.maxhealth = 200000
        self.health = self.maxhealth
        self.attack = 0.05
        self.goldgain = 0.000000000000001 """
