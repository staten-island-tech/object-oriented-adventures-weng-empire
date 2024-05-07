import json, random, os, sys
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

class Character():
    def __init__(self, name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.attack = 10
        self.gold = 0
        self.potions = 0
        self.weapon = ["Basic Sword"]
class Enemy():
    def __init__(self, name):
        self.name = name
        self.maxhealth = 50
        self.health = self.maxhealth
        self.attack = 5
        self.goldgain = random.randint(5,15)
Goblin = Enemy()
Knight = Enemy()
Slime = Enemy()
Zombie = Enemy()
class Main():
    def main():
        print("Welcome!\n")
        print("1.) Start")
        print("2.) Exit")
        option = input("-> ")
        if option == "1":
            St.start()
        elif option == "2":
            sys.exit()
        else:
            print('Please pick a valid option')
            Ma.main()

class Start():
    def start():
        print("Hello, what is your name?")
        option = input("--> ")
        global player 
        player = Character(option)
        Mn.menu

class Menu():
    def menu():
        print("Name: %s") % player.name
        print("Attack: %i") % player.attack
        print("Gold: %i") % player.gold
        print("Current Weapons: %s") % player.weapon
        print("Potions: %i") % player.potions
        print("Health: %i/%i\n") % (player.health, player.maxhealth)
        print("1.) Fight")
        print("2.) Store")
        print("3.) Inventory")
        print("4.) Exit")
        option = input("--> ")
        if option == "1":
            Ep.enemypick()
        elif option == "2":
            St.store()
        elif option == "3":
            I.inventory()
        elif option == "4":
            sys.exit()
        else:
            print("Please pick a valid option")
            Mn.menu()

def attack(self):
    attack = self.attack
    if self.weapon == "Basic Sword":
        attack += 5
    elif self.weapon == "Great Sword":
        attack += 25
    elif self.weapon == "Dragon Slayer":
        attack += 50
    return attack

class Inventory():
    def inventory():
        print("What do you want to do?")
        print("1.) Equip Weapon")
        print("2.) Go back")

class Equip():
    def equip():
        print("What do you want to equip?")

class Enemypick():
    def enemypick():
        global enemy
        enemynum = random.randint(1, 4)
        if enemynum == 1:
            enemy = Goblin
        elif enemynum == 2:
            enemy = Knight
        elif enemynum == 3:
            enemy = Slime
        else:
            enemy = Zombie
        F.fight()

class Fight():
    def fight():
        print()
    fight()

def attackdamage():
    attackdamage()

class Potionfight():
    def potionfight():
        if player.potions == 0:
            print("You don't have any potions")
        else:
            player.health += 50
            if player.health > player.maxhealth:
                player.health = player.maxhealth
            print("You drank a potion!")
        option = input(' ')
        F.fight()

class Potionmenu():
    def potionmenu():
        if player.potions == 0:
            print("You don't have any potions")
        else:
            player.health += 50
            if player.health > player.maxhealth:
                player.health = player.maxhealth
            print("You drank a potion!")
        option = input(' ')
        Mn.menu()

class Run():
    def run():
        runchance = random.randint(1, 2)
        if runchance == '1':
            print("You successfully ran away!")
            option = input(' ')
            Mn.menu()
        else:
            print("You failed to get away!")
            option = input(' ')

class Win():
    def win():
        player.gold += enemy.goldgain
        print(f"You have defeated {enemy.name}")
        print(f"You found %i gold! {enemy.goldgain}")
        option = input(' ')
        Mn.menu()

class Dead():
    def dead():
        print("You have died")
        print("1.) Restart")
        print("2.) Exit")
        option = input(' ')
        if option == '1':
            St.start()
        elif option == '2':
            sys.exit


weapons = {"Great Sword"}
class Store():
    def store():
        print("Welcome to the shop!")
        print("\nWhat would you like to buy?\n")
        print("1.) Great Sword")
        print("2.) Dragon Slayer")
        print("3.) Back")
        option = input(' ')

Ma = Main()
St = Start()
Mn = Menu()
I = Inventory()
Eq = Equip()
Ep = Enemypick()
F = Fight()
R = Run()
W = Win()
D = Dead()
So = Store()
Main.main()