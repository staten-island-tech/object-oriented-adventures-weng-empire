import json
import random 
import os 
import pickle 

## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

class Player():
    def __init__(self, name):
        self.name = name
        self.maxhealth = 100
        self.attack = 10
        self.gold = 0
        self.weapon = ["Basic Sword"]

class Goblin():
    def __init__(self):
        self.name = ["Goblin"]
        self.maxhealth = 80
        self.attack = 7
        self.goldgain = random.randint(5,15)

class Slime():
    def __init__(self):
        self.name = ["Slime"]
        self.maxhealth = 50
        self.attack = 5
        self.goldgain = random.randint(1,10)

class Knightmob():
    def __init__(self):
        self.name = ["Knight"]
        self.maxhealth = 140
        self.attack = 15
        self.goldgain = random.randint(25,50)
        self.weapon = ["Sword"]

def main():
    print("Welcome to the game")
    print("1.) Start")
    print("2.) Load")
    print("3.) Exit")
    choice = ("-> ")
    if choice == "1":
        start()


def start():
    os.system('clear')
    print("Welcome traveler, what is your name?: ")
    option = input("--> ")
    global PlayerIG
    PlayerIG = Player(option)
    

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

class Mark():
    def __init__(self, name):
        self.name = name
        self.maxhealth = 200000
        self.attack = 0.1
        self.goldgain = 0.0000000000000000000000000001

print(main)