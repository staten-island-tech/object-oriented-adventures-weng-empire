""" from imports import player, menu
import random


def heal():
    healchance = random.randint(1,10)
    if healchance == 1 or 2 or 3 or 4:
        player.health += 10
        if player.health >= player.maxhealth:
            player.health = player.maxhealth
        print("You sit by a campfire and regenerate 10 health")
        option = input("-->")
        menu()
    elif healchance == 5 or 6 or 7:
        player.health += 25
        if player.health >= player.maxhealth:
            player.health = player.maxhealth
        print("You sit by a roaring campfire and regenerate 25 health")
        option = input("-->")
        menu()
    elif healchance == 8 or 9:
        player.health += 50
        if player.health >= player.maxhealth:
            player.health = player.maxhealth
        print("You sit by a magical campfire and regenerate 50 health")
        option = input("-->")
        menu()
    else:
        player.maxhealth += 25
        player.health = player.maxhealth
        print("The gods bless you and grant you 25 extra health, fully rejuvenating you")
        option = input("-->")
        menu() """