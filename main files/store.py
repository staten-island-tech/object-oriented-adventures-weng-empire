import os 

def store(player):
    os.system('cls')
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
            return input(" ")
        else:
            print("You don't have enough gold")
            option = input(' ')
            store(player)
    elif option == "2":
        weapon = "Dragon Slayer"
        if player.gold >= 200:
            player.gold -= 200
            player.weapon.append(weapon)
            print("You have bought the Dragon Slayer")
            return input(" ")
        else:
            print("You don't have enough gold")
            option = input(' ')
            store(player)
    elif option == "3":
        weapon = "Odachi"
        if player.gold >= 500:
            player.gold -= 500
            player.weapon.append(weapon)
            print("You have bought an Odachi") 
            return input(" ")  
        else:
            print("You don't have enough gold")
            option = input(' ')
            store(player)
    elif option == "4":
        if player.gold >= 10:
            player.gold -= 10
            player.potions += 1
            print(f"You have bought a potion")
            print(f"You have {player.potions} potions")
            option = input(' ')
            store(player)
        else:
            print("You don't have enough gold")
            option = input(' ')
            store(player)
    elif option == "5":
        return
    else:
        print("Please pick a valid option")
        option = input(" ")
        store(player)
