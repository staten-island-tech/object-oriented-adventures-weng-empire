import json, sys
from fight import Enemypick
from enemy import Player
from store import Store
from inventory import Inventory


def main(): 
    print("Welcome!\n")
    print("1.) Start")
    print("2.) Exit")
    option = input("--> ")
    if option == "1":
        def start():
            print("Hello, what is your name?")
            name = input("--> ")
            global player
            player = Player(name)
            menu()
        start()
    elif option == "2":
        sys.exit()
    else:
        print('Please pick a valid option')
        main()

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
        print("4.) Heal")
        print("5.) Exit")
        option = input("--> ")
        if option == "1":
            Enemypick.enemypick()
        elif option == "2":
            Store.store()
        elif option == "3":
            Inventory.inventory()
        elif option == "4":
            Heal.heal()
        elif option == "5":
            sys.exit()
        else:
            print("Please pick a valid option")
            menu()

class Heal():
     def heal():
         option = input("-->")
         menu




