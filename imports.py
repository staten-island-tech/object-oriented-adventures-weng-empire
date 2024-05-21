""" import sys, random

class Player():
    def __init__(self, name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.attack = 10
        self.gold = 1000
        self.potions = 2
        self.weapon = ["Basic Sword"]
        self.currentweapon = ["Basic Sword"]

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


class Potion():
    def potion():
        if player.potions == 0:
            print("You don't have any potions")
        else:
            player.health += 50
            if player.health > player.maxhealth:
                player.health = player.maxhealth
            print("You drank a potion!")
        Fight.fight()

class Heal():
    def heal():
        option = input("-->")
        Menu.menu

def attackdamage(self):
    attack = self.attack
    if self.weapon == ["Basic Sword"]:
        attack += 5
    elif self.weapon == "Katana":
        attack += 25
    elif self.weapon == ["Dragon Slayer"]:
        attack += 50
    elif attack.weapon == "AK-47":
        attack += 100


class Store():
    def store():
        print("Welcome to the Store!")
        print("\nWhat would you like to purchase? (Enter full name of item)\n")
        print("1.) Katana (50 Gold)")
        print("2.) Dragon Slayer (200 Gold)")
        print("3.) AK-47 (500 Gold)")
        print("4.) Potion (10 Gold)")
        print("5.) Back")
        option = input(' ')
        if option == "1":
            weapon = "Katana"
            if player.gold >= 50:
                player.gold -= 50
                player.weapon.append(weapon)
                print(f"You have bought a Katana")
                option = input(' ')
                Store.store()
            else:
                print("You don't have enough gold")
                option = input(' ')
                Store.store()
        elif option == "2":
            weapon = "Dragon Slayer"
            if player.gold >= 200:
                player.gold -= 200
                player.weapon.append(weapon)
                print(f"You have bought the Dragon Slayer")
                option = input(' ')
                Store.store()
            else:
                print("You don't have enough gold")
                option = input(' ')
                Store.store()
        elif option == "3":
            weapon = "AK-47"
            if player.gold >= 500:
                player.gold -= 500
                player.weapon.append(weapon)
                print(f"You have bought an AK-47")
                option = input(' ')
                Store.store()
            else:
                print("You don't have enough gold")
                option = input(' ')
                Store.store()
        elif option == "4":
            if player.gold >= 10:
                player.gold -= 10
                player.potions += 1
                print(f"You have bought a potion")
                option = input(' ')
                Store.store()
            else:
                print("You don't have enough gold")
                option = input(' ')
                Store.store()
        elif option == "5":
            Menu.menu()
        else:
            print("Please pick a valid option")
            Store.store() """