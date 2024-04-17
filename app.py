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

class Goblin:
    def __int__(self, name):
        self.name = name
        self.maxhealth = 80
        self.attack = 7
        self.goldgain = 20

class Slime
        
        