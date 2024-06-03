import os, sys
from store import store
from inventory import inventory
from fight import enemypick
from main import heal

def menu(player):
    os.system('cls')
    print(f"Name: {player.name}")  
    print(f"Attack: {player.attack}")
    print(f"Health: {player.health}/{player.maxhealth}")
    print(f"Gold: {player.gold}") 
    print(f"Potions: {player.potions}") 
    print(f"Weapons: {player.weapon}")  
    print(f"Equipped Weapon: {player.currentweapon}")
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