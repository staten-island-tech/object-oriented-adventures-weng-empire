import sys, random

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

class Main():
    def main(): 
        print("Welcome!\n")
        print("1.) Start")
        print("2.) Exit")
        option = input("--> ")
        if option == "1":
            def start():
                print("Hello, what is your name?")
                option = input("--> ")
                global player 
                player = Player(option)
                Menu.menu()
            start()
        elif option == "2":
            sys.exit()
        else:
            print('Please pick a valid option')
            Main.main()
Main.main()


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
            Store.store()

class WarriorStore():
    def WarriorStore():
        print("Welcome to the Warrior's Store!")
        print("\nWhat would you like to purchase? (Enter full name of item)\n")
        print("1.) Sword (10 gold) attack = 3")
        print("2.) Katana (50 gold) (attack = 7)")
        print("3.) Emerald Sword (200 gold) (attack = 20)")
        print("4.) Buster Sword (800 gold) (attack =50)")
        print("5.) Leviathan Axe (2000 gold) (attack = 100)")
        print("6.) The Master Sword (5000 gold) (attack = 200)")
        print("7.) Angel Sword (15000 gold) (attack = 500)")
        print("8.) Warrior Potion (20 gold)")
        option = input(' ')
        if option == "1":
            weapon = "Sword"
            if player.gold >= 10:
                player.gold -= 10
                player.weapon.append(weapon)
                print(f"You have bought a Sword")
                option = input(' ')
                Store.store()
            else:
                print("You don't have enough gold")
                option = input(' ')
                Store.store()
        elif option == "2":
            weapon = "Katana"
            if player.gold >= 505:
                player.gold -= 50
                player.weapon.append(weapon)
                print(f"You have bought the Katana")
                option = input(' ')
                Store.store()
            else:
                print("You don't have enough gold")
                option = input(' ')
                Store.store()
        elif option == "3":
            weapon = "Emerald Sword"
            if player.gold >= 200:
                player.gold -= 200
                player.weapon.append(weapon)
                print(f"You have bought the Emerald Sword")
                option = input(' ')
                Store.store()
            else:
                print("You don't have enough gold")
                option = input(' ')
                Store.store()
        elif option == "4":
            weapon = "Buster Sword"
            if player.gold >= 800:
                player.gold -= 800
                player.weapon.append(weapon)
                print(f"You have bought the Buster Sword")
                option = input(' ')
                Store.store()
            else:
                print("You don't have enough gold")
                option = input(' ')
                Store.store()
        elif option == "5":
            weapon = "Leviathan Axe"
            if player.gold >= 2000:
                player.gold -= 2000
                player.weapon.append(weapon)
                print(f"You have bought the Leviathan Axe")
                option = input(' ')
                Store.store()
            else:
                print("You don't have enough gold")
                option = input(' ')
                Store.store()
        elif option == "6":
            weapon = "Master Sword"
            if player.gold >= 5000:
                player.gold -= 5000
                player.weapon.append(weapon)
                print(f"You have bought the Master Sword")
                option = input(' ')
                Store.store()
            else:
                print("You don't have enough gold")
                option = input(' ')
                Store.store()
        elif option == "7":
            weapon = "Angel Sword"
            if player.gold >= 15000:
                player.gold -= 15000
                player.weapon.append(weapon)
                print(f"You have bought the Angel Sword")
                option = input(' ')
                Store.store()
            else:
                print("You don't have enough gold")
                option = input(' ')
                Store.store()
        elif option == "8":
            if player.gold >= 20:
                player.gold -= 20
                player.weapon.append(weapon)
                print(f"You have bought the Warrior Potion")
                option = input(' ')
                Store.store()
            else:
                print("You don't have enough gold")
                option = input(' ')
                Store.store()

class MageStore():
    def MageStore():
        print("Welcome to the Warrior's Store!")
        print("\nWhat would you like to purchase? (Enter full name of item)\n")
        print("1.) Staff (10 gold) attack = 3")
        print("2.) Cursed Staff(50 gold) (attack = 7)")
        print("3.) Emerald Staff (200 gold) (attack = 20)")
        print("4.) Buster Staff (800 gold) (attack =50)")
        print("5.) Leviathan Staff (2000 gold) (attack = 100)")
        print("6.) Majestic Staff (5000 gold) (attack = 200)")
        print("7.) Angel Staff (15000 gold) (attack = 500)")
        print("8.) Mage Potion (20 gold)")
        option = input(' ')
        if option == "1":
            weapon = "Sword"
            if player.gold >= 10:
                player.gold -= 10
                player.weapon.append(weapon)
                print(f"You have bought a Sword")
                option = input(' ')
                Store.store()
            else:
                print("You don't have enough gold")
                option = input(' ')
                Store.store()
        elif option == "2":
            weapon = "Cursed Staff"
            if player.gold >= 505:
                player.gold -= 50
                player.weapon.append(weapon)
                print(f"You have bought the Cursed Staff")
                option = input(' ')
                Store.store()
            else:
                print("You don't have enough gold")
                option = input(' ')
                Store.store()
        elif option == "3":
            weapon = "Emerald Staff"
            if player.gold >= 200:
                player.gold -= 200
                player.weapon.append(weapon)
                print(f"You have bought the Emerald Staff")
                option = input(' ')
                Store.store()
            else:
                print("You don't have enough gold")
                option = input(' ')
                Store.store()
        elif option == "4":
            weapon = "Buster Staff"
            if player.gold >= 800:
                player.gold -= 800
                player.weapon.append(weapon)
                print(f"You have bought the Buster Staff")
                option = input(' ')
                Store.store()
            else:
                print("You don't have enough gold")
                option = input(' ')
                Store.store()
        elif option == "5":
            weapon = "Leviathan Staff"
            if player.gold >= 2000:
                player.gold -= 2000
                player.weapon.append(weapon)
                print(f"You have bought the Leviathan Staff")
                option = input(' ')
                Store.store()
            else:
                print("You don't have enough gold")
                option = input(' ')
                Store.store()
        elif option == "6":
            weapon = "Majestic Staff"
            if player.gold >= 5000:
                player.gold -= 5000
                player.weapon.append(weapon)
                print(f"You have bought the Majestic Staff")
                option = input(' ')
                Store.store()
            else:
                print("You don't have enough gold")
                option = input(' ')
                Store.store()
        elif option == "7":
            weapon = "Angel Staff"
            if player.gold >= 15000:
                player.gold -= 15000
                player.weapon.append(weapon)
                print(f"You have bought the Angel Staff")
                option = input(' ')
                Store.store()
            else:
                print("You don't have enough gold")
                option = input(' ')
                Store.store()
        elif option == "8":
            if player.gold >= 20:
                player.gold -= 20
                player.weapon.append(weapon)
                print(f"You have bought the Mage Potion")
                option = input(' ')
                Store.store()
            else:
                print("You don't have enough gold")
                option = input(' ')
                Store.store()