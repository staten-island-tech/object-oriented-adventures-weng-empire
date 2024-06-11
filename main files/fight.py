import sys, random, os
from enemy import Goblin, Knight, Slime, Zombie, Mark, True_Mark



def enemypick(player):
    global enemy, fighting
    fighting = True
    enemynum = random.randint(1, 4)
    if player.mobkills == 100:
        enemy = True_Mark("True Mark", 10000000000000, 10000000000000, 1000, random.randint(100000000,10000000000000000))
    elif enemynum == 1:
        enemy = Knight("Knight", 120, 140, 9, random.randint(25,50))
    elif enemynum == 2:
        enemy = Slime("Slime", 50, 80, 4, random.randint(1,10))
    elif enemynum == 3:
        enemy = Mark("Mark", 1000000000, 1000000000, 0.000000001, random.randint(1,1000000000))
    elif enemynum == 4:
        enemy = Goblin("Goblin", 80, 80, 5, random.randint(5,15))
    else:
        enemy = Zombie("Zombie", 100, 80, 7, random.randint(10,25))
    fight(player)
  
def enemyhit(player):
    eattack = random.randint(1,3)
    if eattack != 1:
        player.health -= enemy.attack
        if player.health <= 0:
            global fighting
            fighting = False
            dead(player)
        else:
            print(f"The {enemy.name} hit you dealing {enemy.attack} damage!")
            option = input(" ")
    else: 
        print(f"The {enemy.name} missed!")
        option = input(" ")

def playerhit(player):
    global fighting
    pattack = random.randint(1,4)
    if pattack != 1:
        enemy.health -= player.attack
        if enemy.health <= 0:
            print("debug1")
            fighting = False
            if enemy == True_Mark:
                print("debug2")
                markwin(player)
            else:
                win(player)
        else: 
            print(f"You hit the {enemy.name} dealing {player.attack} damage!")
            enemyhit(player)
    else:
        print("You missed!")
        enemyhit(player)

def run(player):
    runchance = random.randint(1, 2)
    if runchance == 1:
        global fighting
        fighting = False
        print("You successfully ran away")
        return input(" ")
    else:
        print("You failed to get away!")
        enemyhit(player)

def potion(player):
    if player.potions == 0:
        print("You don't have any potions")
    else:
        player.health += 50
        if player.health > player.maxhealth:
            player.health = player.maxhealth
        print("You drank a potion!")
        option = input(" ")

def fight(player):
    print(f"You come across a {enemy.name}!")
    while fighting:
        os.system('cls')
        print(f"{enemy.name}: {enemy.health}/{enemy.maxhealth} | {player.name}: {player.health}/{player.maxhealth}")
        print("1.) Attack")
        print("2.) Potion")
        print("3.) Run")
        option = input("--> ")
        if option == "1":
            playerhit(player)
        elif option == "2":       
            potion(player)
        elif option == "3":
            run(player)
        else:
            fight(player)


def markwin(player):
    player.gold += enemy.goldgain
    player.mobkills += 1 
    print("You have defeated True Mark!") 
    print("Continue Playing?")
    print("1.) Continue")
    print("2.) Exit")
    option = input(" ")
    if option == "1":
        return
    elif option == "2":
        sys.exit
    else:
        markwin(player)

def win(player):
    player.gold += enemy.goldgain
    print(f"You have defeated the {enemy.name}") 
    print(f"You found {enemy.goldgain} gold!") 
    return input(" ")

def dead(player):
    player.health = player.maxhealth
    print("You have died")
    print("1.) Return")
    print("2.) Exit")
    option = input("--> ")
    if option == '1':
        return
    elif option == '2':
        sys.exit


