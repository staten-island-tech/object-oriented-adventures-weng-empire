import json, random, os, sys

class Player():
    def __init__(self, name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.attack = 10
        self.gold = 100
        self.potions = 2
        self.weapon = ["Basic Sword"]

class Enemy():
    def __init__(self, name):
        self.name = name
        self.maxhealth = 80
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
        option = input("--> ")
        if option == "1":
            Start.start()
        elif option == "2":
            sys.exit()
        else:
            print('Please pick a valid option')
            Main.main()

class Start():
    def start():
        print("Hello, what is your name?")
        option = input("--> ")
        global player 
        player = Player(option)
        Menu.menu()

class Menu():
    def menu():
        print(f"Name: {player.name}")  
        print(f"Attack: {player.attack}") 
        print(f"Gold: {player.gold}") 
        print(f"Current Weapons: {player.weapon}")  
        print(f"Potions: {player.potions}") 
        print(f"Health: {player.health}/{player.maxhealth}")
        print("1.) Fight")
        print("2.) Store")
        print("3.) Inventory")
        print("4.) Exit")
        option = input("--> ")
        if option == "1":
            Enemypick.enemypick()
        elif option == "2":
            Store.store()
        elif option == "3":
            Inventory.inventory()
        elif option == "4":
            sys.exit()
        else:
            print("Please pick a valid option")
            Menu.menu()

def attack(self):
    attack = self.attack
    if self.weapon == ["Basic Sword"]:
        attack += 5
    elif self.weapon == ["Great Sword"]:
        attack += 25
    elif self.weapon == ["Dragon Slayer"]:
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
        elif enemynum == 3 :
            enemy = Slime
        else:
            enemy = Zombie
        Fight.fight()

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
        Fight.fight()

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
        Menu.menu()

class Run():
    def run():
        runchance = random.randint(1, 2)
        if runchance == '1':
            print("You successfully ran away!")
            option = input(' ')
            Menu.menu()
        else:
            print("You failed to get away!")
           

class Win():
    def win():
        player.gold += enemy.goldgain
        print(f"You have defeated the {enemy.name}")
        print(f"You found {enemy.goldgain} gold!")
        option = input(' ')
        Menu.menu()

class Dead():
    def dead():
        print("You have died")
        print("1.) Restart")
        print("2.) Exit")
        option = input("--> ")
        if option == '1':
            Start.start()
        elif option == '2':
            sys.exit

weapons = ["Katana", "Dragon Slayer", "AK-47"]
class Store():
    def store():
        print("Welcome to the shop!")
        print("\nWhat would you like to buy?\n")
        print("1.) Katana (50 Gold)")
        print("2.) Dragon Slayer (200 Gold)")
        print("3.) AK-47 (500 Gold)")
        print("4.) Potion (10 Gold)")
        print("5.) Back")
        option = input("--> ")
        for weapon in weapons:
            if option in weapons:
                option = weapon 
                if player.gold >= 50:
                    player.gold -= 50
                    player.weapon.append(option)
                    print(f"You have purchased {option}")
                    Store.store

Main.main()

class Abilities():
    def __init__(self, name, effects):
        self.name = name
        self.attack = []
        self.effects = effects
        def castabilities():
            print(self.effects)
            print(self.attack)

class Boss():
    def __init__(self, name, weapon, abilities):
        self.name = name
        self.maxhealth = []
        self.health = self.maxhealth
        self.attack = []
        self.weapon = weapon
        self.abilities = abilities
        self.goldgain = []
