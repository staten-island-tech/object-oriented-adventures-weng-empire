import json, sys, random, os
from store import store
from inventory import inventory
from fight import enemypick
from heal import heal

class Player():
    def __init__(self, name):
        self.name = name
        self.maxhealth = 1000
        self.health = 1
        self.attack = 10
        self.gold = 1000
        self.potions = 2
        self.weapon = ["Basic Sword"]
        self.currentweapon = ["Basic Sword"]

""" def heal():
    healchance = random.randint(1,10)
    if healchance == 1 or 2 or 3 or 4:
        player.health += 10
        if player.health >= player.maxhealth:
            player.health = player.maxhealth
        print("You sit by a campfire and regenerate 10 health")
        option = input("-->")
        menu()
    elif healchance == 5 or 6 or 7:
        player.health += 25
        if player.health >= player.maxhealth:
            player.health = player.maxhealth
        print("You sit by a roaring campfire and regenerate 25 health")
        option = input("-->")
        menu()
    elif healchance == 8 or 9:
        player.health += 50
        if player.health >= player.maxhealth:
            player.health = player.maxhealth
        print("You sit by a magical campfire and regenerate 50 health")
        option = input("-->")
        menu()
    else:
        player.maxhealth += 25
        player.health = player.maxhealth
        print("The gods bless you and grant you 25 extra health, fully rejuvenating you")
        option = input("-->")
        menu() """


def menu():
    os.system('cls')
    print(f"Name: {player.name}")  
    print(f"Attack: {player.attack}") 
    print(f"Gold: {player.gold}") 
    print(f"Current Weapons: {player.weapon}")  
    print(f"Potions: {player.potions}") 
    print(f"Health: {player.health}/{player.maxhealth}")
    print("1.) Fight")
    print("2.) Store")
    print("3.) Inventory")
    print("4.) Heal")
    print("5.) Exit")
    gameloop = "Y"
    while gameloop == "Y":
        option = input("--> ")
        if option == "1":
            enemypick()
        elif option == "2":
            store(player)
        elif option == "3":
            inventory(player)
        elif option == "4":
            heal(player)
        elif option == "5":
            sys.exit()
        else:
            print("Please pick a valid option")
            option = input(' ')
    
def main(): 
    print("Welcome!\n")
    print("1.) Start")
    print("2.) Exit")
    option = input("--> ")
    if option == "1":
        print("Hello, what is your name?")
        name2 = input("--> ")
        global player
        player = Player(name2)
        menu()
    elif option == "2":
        sys.exit()
    else:
        print('Please pick a valid option')
        main()


main()
