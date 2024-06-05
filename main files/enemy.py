import random

""" class Enemy():
    def __init__(self):
        self.maxhealth = 100
        self.health = self.maxhealth
        self.attack = 7
        self.goldgain = random.randint(5,50)

class Goblin(Enemy):
    pass

class Slime(Enemy):
    pass

class Knight(Enemy):
    pass

class Zombie(Enemy):
    pass

class Mark(Enemy):
    pass """


class Goblin():
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
        self.goldgain = 0.000000000000001
