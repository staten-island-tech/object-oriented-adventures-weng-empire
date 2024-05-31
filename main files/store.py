import os 
from menu import menu

def store(player):
    print("Welcome to the Store!\n")
    print("What would you like to purchase?\n")
    print("1.) Katana (50 Gold)")
    print("2.) Dragon Slayer (200 Gold)")
    print("3.) Odachi (500 Gold)")
    print("4.) Potion (10 Gold)")
    print("5.) Back")
    option = input(' ')
    if option == "1":
        weapon = "Katana"
        if player.gold >= 50:
            player.gold -= 50
            player.weapon.append(weapon)
            print("You have bought a Katana")
            option = input(' ')
            menu()
        else:
            print("You don't have enough gold")
            option = input(' ')
            store()
    elif option == "2":
        weapon = "Dragon Slayer"
        if player.gold >= 200:
            player.gold -= 200
            player.weapon.append(weapon)
            print("You have bought the Dragon Slayer")
            option = input(' ')
            menu()
        else:
            print("You don't have enough gold")
            option = input(' ')
            store()
    elif option == "3":
        weapon = "Odachi"
        if player.gold >= 500:
            player.gold -= 500
            player.weapon.append(weapon)
            print("You have bought an Odachi")
            option = input(' ')
            menu()
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
