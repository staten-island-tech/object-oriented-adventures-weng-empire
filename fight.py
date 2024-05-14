import sys, random, time 
from main import Goblin, Knight, Slime, Zombie, player, Menu, Start



class Enemypick():
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
        Fight.fight() 
 
fighting = "Y"
class Fight():
    while fighting == "Y":
        def fight():
            print(f"You come across a {enemy}!")
            print("1.) Attack")
            print("2.) Defend")
            print("3.) Potion")
            print("4.) Run")
            pattack = random.randint(1,3)
            eattack = random.randint(1,2)
            if pattack == 1: 
                print("You missed!")
                time.sleep(1)
            else: 
                enemy.health -= player.attack
                print(f"You dealt {player.attack} damage!")
                print(f"{enemy} {enemy.health}/{enemy.maxhealth}HP")
                if enemy.health <= 0:
                    fighting != "Y"
                    Win.win
                    break
            if eattack == 1:
                print(f"The {enemy} missed!")
            else: 
                player.health -= enemy.attack
                print(f"The {enemy} dealt {enemy.attack} damage!")
                print(f"{player.health}/{player.maxhealth}HP")
                if player.health <= 0:
                    fighting != "Y"
                    Dead.dead
                    break



class Run():
    def run():
        runchance = random.randint(1, 2)
        if runchance == '1':
            fighting != "Y"
            print("You successfully ran away")
            Menu.menu()
        else:
            print("You failed to get away!")

class Win():
    def win():
        player.gold += enemy.goldgain
        print(f"You have defeated the {enemy.name}") 
        print(f"You found {enemy.goldgain} gold!") 
        Menu.menu()

class Dead():
    def dead():
        print("You have died")
        print("1.) Restart")
        print("2.) Exit")
        option = input("--> ")
        if option == '1':
            Start.start()
        elif option == '2':
            sys.exit