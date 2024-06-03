import random


def heal(player):
    healchance = random.randint(1,10)
    if healchance in [1,2,3,4]:
        player.health += 10
        if player.health >= player.maxhealth:
            player.health = player.maxhealth
        print("Mr. Whalen increases your HOS to 75; You regenerate 10 health")
        return input(" ")
    elif healchance in [5,6,7]:
        player.health += 25
        if player.health >= player.maxhealth:
            player.health = player.maxhealth
        print("Mr. Whalen increases your HOS to 85; You regenerate 25 health")
        return input(" ")
    elif healchance in [8,9]:
        player.health += 50
        if player.health >= player.maxhealth:
            player.health = player.maxhealth
        print("Mr. Whalen increases your HOS to 95; You regenerate 50 health")
        return input(" ")
    else:
        player.maxhealth += 25
        player.health = player.maxhealth
        print("Mr. Whalen increases your HOS to 100, granting you 25 extra health, fully rejuvenating you")
        return input(" ")