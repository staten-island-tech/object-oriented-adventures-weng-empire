import json
import random 
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

class Player():
    def __init__(self, name):
        self.name = name 
        self.health = 100
        self.weapon = ["Old Blade"]
        self.baseattack = 5
        self.maxhealth = self.health
        self.gold = 50

    def attack(self):
        attack = self.baseattack
        if self.weapon == "Old Blade":
            attack += 10


        

        


