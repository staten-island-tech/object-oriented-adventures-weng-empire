import os, sys
""" from store import store
from inventory import inventory
from fight import enemypick """

def menu(user):
    os.system('cls')
    print(f"Name: {user.name}")  
    print(f"Attack: {user.attack}")
    print(f"Health: {user.health}/{user.maxhealth}")
    print(f"Gold: {user.gold}") 
    print(f"Potions: {user.potions}") 
    print(f"Weapons: {user.weapon}")  
    print(f"Equipped Weapon: {user.currentweapon}")
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