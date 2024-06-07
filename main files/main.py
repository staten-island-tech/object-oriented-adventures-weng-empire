import json, sys, random, os
from store import store
from inventory import inventory
from fight import enemypick
from heal import heal

class Player():
    def __init__(self, name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.attack = 10
        self.gold = 0
        self.potions = 2
        self.weapons = ["Basic Sword"]
        self.currentweapon = ["Basic Sword"]

class Menu():
    def menu():
        gameloop = "Y"
        while gameloop == "Y":
            os.system('cls')
            print(f"Name: {player.name}")  
            print(f"Attack: {player.attack}") 
            print(f"Gold: {player.gold}") 
            print(f"Weapons: {player.weapons}")
            print(f"Equipped Weapon: {player.currentweapon}")  
            print(f"Potions: {player.potions}") 
            print(f"Health: {player.health}/{player.maxhealth}")
            print("1.) Fight")
            print("2.) Store")
            print("3.) Inventory")
            print("4.) Heal")
            print("5.) Exit")
            option = input("--> ")
            if option == "1":
                enemypick(player)
            elif option == "2":
                store(player)
            elif option == "3":
                inventory(player)
            elif option == "4":
                heal(player)
            elif option == "5":
                sys.exit()
            else:
                print(" ")
        
def main(): 
    print("Welcome!\n")
    print("1.) Start")
    print("2.) Exit")
    option = input("--> ")
    if option == "1":
        os.system('cls')
        print("Hello, what is your name?")
        name2 = input("--> ")
        global player
        player = Player(name2)
        Menu.menu()
    elif option == "2":
        sys.exit()
    else:
        print('Please pick a valid option')
        option = input(" ")
        os.system('cls')
        main()


main()