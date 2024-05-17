import json, sys
from fight import Enemypick
from enemy import Player
from store import Store
from inventory import Inventory

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
            Menu.menu()

class Heal():
    def heal():
        option = input("-->")
        Menu.menu




