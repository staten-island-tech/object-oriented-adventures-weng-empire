import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

class Character():
    def __init__(self, name):
        self.name = name
        self.maxhealth = 100
        self.attack = 10
        self.gold = 0
        self.weapon = ["Basic Sword"]

class Goblin():
    def __init__(self, name):
        self.name = name
        self.maxhealth = 80
        self.attack = 7
        self.goldgain = 20

class Slime():
    def __init__(self, name):
        self.name = name
        self.maxhealth = 50
        self.attack = 5
        self.goldgain = 10

def main():
    print("Welcome to the game")
    print("1.) Start")
    print("2.) Load")
    print("3.) Exit")
    if 

class Knight():
    def __init__(self, name):
        self.name = name
        self.maxhealth = 140
        self.attack = 15
        self.goldgain = 40
        self.weapon = ["Sword"]

class Zombie():
    def __init__(self, name):
        self.name = name
        self.maxhealth = 120
        self.attack = 18
        self.goldgain = 35


