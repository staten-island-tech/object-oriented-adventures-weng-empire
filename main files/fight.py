import sys, random, time, os
from enemy import Goblin, Knight, Slime, Zombie

def enemypick(player):
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
    fight(player) 

pattack = random.randint(1,3)
eattack = random.randint(1,2)
fighting = "Y"


def hit(player):
    if pattack != 1:
        enemy.health -= player.attack
        if enemy.health <= 0:
            fighting != "Y"
            win(player)
        else: 
            print(f"You hit the {enemy} dealing {player.attack} damage!")
    if eattack != 1:
        print(f"The {enemy} hit you dealing {enemy.attack} damage!")

def dodge():
    if pattack == 1:
        print("You missed!")
    if eattack == 1:
        print(f"The {enemy} missed!")
    else:
        hit()

def run():
    runchance = random.randint(1, 2)
    if runchance == 1:
        fighting != "Y"
        print("You successfully ran away")
        return
    else:
        print("You failed to get away!")

def potion(player):
    if player.potions == 0:
        print("You don't have any potions")
    else:
        player.health += 50
        if player.health > player.maxhealth:
            player.health = player.maxhealth
        print("You drank a potion!")

def defend(player):
    if eattack == 1:
        print(f"The {enemy} missed!")
    else: 
        player.health -= enemy.attack/5
        print(f"The {enemy} dealt {enemy.attack} damage!")
        print(f"{player.health}/{player.maxhealth}HP")
        if player.health <= 0:
            fighting != "Y"
            dead()

def fight(player):
    print(f"You come across a {enemy}!")
    while fighting == "Y":
        print(f"Enemy: {enemy.health}/{enemy.maxhealth} | {player}: {player.health}/{player.maxhealth}")
        print("1.) Attack")
        print("2.) Defend")
        print("3.) Potion")
        print("4.) Run")
        option = input("--> ")
        if option == "1":
            if pattack == 1:
                print("You missed!")
            if eattack == 1:
                print(f"The {enemy} missed!")
            else:
                if pattack != 1:
                    enemy.health -= player.attack
                    if enemy.health <= 0:
                        fighting != "Y"
                        win(player)
                    else: 
                        print(f"You hit the {enemy} dealing {player.attack} damage!")
                if eattack != 1:
                    print(f"The {enemy} hit you dealing {enemy.attack} damage!")
        elif option == "2":
            if eattack == 1:
                print(f"The {enemy} missed!")
            else: 
                player.health -= enemy.attack/5
                print(f"The {enemy} dealt {enemy.attack} damage!")
                print(f"{player.health}/{player.maxhealth}HP")
                if player.health <= 0:
                    fighting != "Y"
                    dead()
        elif option == "3":       
            if player.potions == 0:
                print("You don't have any potions")
            else:
                player.health += 50
                if player.health > player.maxhealth:
                    player.health = player.maxhealth
                print("You drank a potion!")
        elif option == "4":
            runchance = random.randint(1, 2)
            if runchance == '1':
                fighting != "Y"
                print("You successfully ran away")
                return
            else:
                print("You failed to get away!")
def win(player):
    player.gold += enemy.goldgain
    print(f"You have defeated the {enemy.name}") 
    print(f"You found {enemy.goldgain} gold!") 
    return

def dead():
    print("You have died")
    print("1.) Return")
    print("2.) Exit")
    option = input("--> ")
    if option == '1':
        return
    elif option == '2':
        sys.exit
