import json, sys, random

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

class Goblin():
    def __init__(self):
        self.name = ["Goblin"]
        self.maxhealth = 80
        self.health = self.maxhealth
        self.attack = 7
        self.goldgain = random.randint(5,15)

class Slime():
    def __init__(self):
        self.name = ["Slime"]
        self.maxhealth = 50
        self.health = self.maxhealth
        self.attack = 5
        self.goldgain = random.randint(1,10)

class Knight():
    def __init__(self):
        self.name = ["Knight"]
        self.maxhealth = 140
        self.health = self.maxhealth
        self.attack = 15
        self.goldgain = random.randint(25,50)
        self.weapon = ["Sword"]

class Zombie():
    def __init__(self, name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.attack = 12
        self.goldgain = random.randint(10,25)

class Mark():
    def __init__(self, name):
        self.name = name
        self.maxhealth = 200000
        self.health = self.maxhealth
        self.attack = 0.05
        self.goldgain = 0.000000000000001


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


def enemypick():
    global enemy
    enemynum = random.randint(1, 4)
    if enemynum == 1:
        enemy = Goblin
    elif enemynum == 2:
        enemy = Knight
    elif enemynum == 3:
        enemy = Slime
    else:
        enemy = Zombie
    fight() 
 

def fight():
    fighting = "Y"
    while fighting == "Y":
        print(f"You come across a {enemy}!")
        print("1.) Attack")
        print("2.) Defend")
        print("3.) Potion")
        print("4.) Run")
        option = input("--> ")
        if option == "1":
            pattack = random.randint(1,3)
            eattack = random.randint(1,2)
            if pattack == 1: 
                print("You missed!")
            else: 
                enemy.health -= player.attack
                print(f"You dealt {player.attack} damage!")
                print(f"{enemy} {enemy.health}/{enemy.maxhealth}HP")
                if enemy.health <= 0:
                    fighting != "Y"
                    win
            if eattack == 1:
                print(f"The {enemy} missed!")
            else: 
                player.health -= enemy.attack
                print(f"The {enemy} dealt {enemy.attack} damage!")
                print(f"{player.health}/{player.maxhealth}HP")
                if player.health <= 0:
                    fighting != "Y"
                    dead
        elif option == "2":
            eattack = random.randint(1,2)
            if eattack == 1:
                print(f"The {enemy} missed!")
            else: 
                player.health -= enemy.attack/5
                print(f"The {enemy} dealt {enemy.attack} damage!")
                print(f"{player.health}/{player.maxhealth}HP")
                if player.health <= 0:
                    fighting != "Y"
                    dead
        elif option == "3":       
            def potion():
                if player.potions == 0:
                    print("You don't have any potions")
                else:
                    player.health += 50
                    if player.health > player.maxhealth:
                        player.health = player.maxhealth
                    print("You drank a potion!")
                potion()
            eattack = random.randint(1,2)
            if eattack == 1:
                print(f"The {enemy} missed!")
            else: 
                player.health -= enemy.attack
                print(f"The {enemy} dealt {enemy.attack} damage!")
                print(f"{player.health}/{player.maxhealth}HP")
                if player.health <= 0:
                    fighting != "Y"
                    dead
        elif option == "4":
            def run():
                runchance = random.randint(1, 2)
                if runchance == '1':
                    fighting != "Y"
                    print("You successfully ran away")
                    menu()
                else:
                    print("You failed to get away!")
            run()
                

def win():
    player.gold += enemy.goldgain
    print(f"You have defeated the {enemy.name}") 
    print(f"You found {enemy.goldgain} gold!") 
    menu()

def dead():
    print("You have died")
    print("1.) Return")
    print("2.) Exit")
    option = input("--> ")
    if option == '1':
        menu()
    elif option == '2':
        sys.exit


def inventory():
    print("What do you want to do?")
    print("1.) Equip Weapon")
    print("2.) Go back")
    option = input("--> ")
    if option == "1":
        equip()
    elif option == "2":
        menu()
    else:
        print("Please pick a valid option")
        inventory()


def equip():
    print(f"{player.weapons}")
    print("What do you want to equip? (Write out full name of item)")
    option = input("--> ").title()
    if option == "Katana":
        player.currentweapon = ["Katana"]
        print(f"{option} Equipped")
        option = input(' ')
        menu()
    elif option == "Dragon Slayer":
        player.currentweapon = ["Dragon Slayer"]
        print(f"{option} Equipped")
        option = input(' ')
        menu()
    elif option == "AK-47":
        player.currentweapon = ["AK-47"]
        print(f"{option} Equipped")
        option = input(' ')
        menu()
    elif option == "Basic Sword":
        player.currentweapon = ["Basic Sword"]
        print(f"{option} Equipped")
        option = input(' ')
        menu()

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
            player.weapons.append(weapon)
            print(f"You have bought a Katana")
            option = input(' ')
            store()
        else:
            print("You don't have enough gold")
            option = input(' ')
            store()
    elif option == "2":
        weapon = "Dragon Slayer"
        if player.gold >= 200:
            player.gold -= 200
            player.weapons.append(weapon)
            print(f"You have bought the Dragon Slayer")
            option = input(' ')
            store()
        else:
            print("You don't have enough gold")
            option = input(' ')
            store()
    elif option == "3":
        weapon = "AK-47"
        if player.gold >= 500:
            player.gold -= 500
            player.weapons.append(weapon)
            print(f"You have bought an AK-47")
            option = input(' ')
            store()
        else:
            print("You don't have enough gold")
            option = input(' ')
            store()
    elif option == "4":
        if player.gold >= 10:
            player.gold -= 10
            player.potions += 1
            print(f"You have bought a potion")
            option = input(' ')
            store()
        else:
            print("You don't have enough gold")
            option = input(' ')
            store()
    elif option == "5":
        menu()
    else:
        print("Please pick a valid option")
        store()




def menu():
    print(f"Name: {player.name}")  
    print(f"Attack: {player.attack}") 
    print(f"Gold: {player.gold}") 
    print(f"Current Weapons: {player.weapons}")  
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
            option = input("--> ")
            global player
            player = Player(option)
            menu()
        start()
    elif option == "2":
        sys.exit()
    else:
        print('Please pick a valid option')
        main()

""" class Heal():
     def heal():
        option = input("-->")
        menu() """



main()