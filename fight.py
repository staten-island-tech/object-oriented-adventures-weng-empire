import sys, random, time 
from imports import Menu, player
from enemy import Goblin, Knight, Slime, Zombie

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
            option = input("--> ")
            if option == "1":
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
                if eattack == 1:
                    print(f"The {enemy} missed!")
                else: 
                    player.health -= enemy.attack
                    print(f"The {enemy} dealt {enemy.attack} damage!")
                    print(f"{player.health}/{player.maxhealth}HP")
                    if player.health <= 0:
                        fighting != "Y"
                        Dead.dead
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
                        Dead.dead
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
                        Dead.dead
            elif option == "4":
                def run():
                    runchance = random.randint(1, 2)
                    if runchance == '1':
                        fighting != "Y"
                        print("You successfully ran away")
                        Menu.menu()
                    else:
                        print("You failed to get away!")
                run()
                
class Win():
    def win():
        player.gold += enemy.goldgain
        print(f"You have defeated the {enemy.name}") 
        print(f"You found {enemy.goldgain} gold!") 
        Menu.menu()

class Dead():
    def dead():
        print("You have died")
        print("1.) Return")
        print("2.) Exit")
        option = input("--> ")
        if option == '1':
            Menu.menu()
        elif option == '2':
<<<<<<< HEAD
            sys.exit
=======
            sys.exit
>>>>>>> b5f9957ff2e25586e55d5c5827b8d894a3cfa48c
