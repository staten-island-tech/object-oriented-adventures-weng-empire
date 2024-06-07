import random


def heal(player):
    healchance = random.randint(1,10)
    if healchance in [1,2,3,4]:
        player.health += 10
        if player.health >= player.maxhealth:
            player.health = player.maxhealth
        print("You get 100 on your test, regenerate 10 health")
        return input(" ")
    elif healchance in [5,6,7]:
        player.health += 25
        if player.health >= player.maxhealth:
            player.health = player.maxhealth
        print("You hang out with your crush, regenerate 25 health")
        return input(" ")
    elif healchance in [8,9]:
        player.health += 50
        if player.health >= player.maxhealth:
            player.health = player.maxhealth
        print("You get a day off, regenerate 50 health")
        return input(" ")
    else:
        player.maxhealth += 25
        player.health = player.maxhealth
        print("Mr. Whalen increases your HOS to 100, granting you 25 extra health and fully regenerating your health")
        return input(" ")