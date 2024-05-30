import json, sys, random
from heal import heal
from store import store
from inventory import inventory
from fight import enemypick
from enemy import Player

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
            enemypick()
        elif option == "2":
            store()
        elif option == "3":
            inventory()
        elif option == "4":
            heal()
        elif option == "5":
            sys.exit()
        else:
            print("Please pick a valid option")
            menu()

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




main()

