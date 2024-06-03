def inventory(player):
    print("What do you want to do?")
    print("1.) Equip Weapon")
    print("2.) Go back")
    option = input("--> ")
    if option == "1":
        def equip(player):
            print(f"{player.weapon}\n")
            print("What do you want to equip? (Write out full name of item) (Type back to return)\n")
            option_2 = input("--> ").title()
            if option_2 in player.weapon:
                player.currentweapon = player.weapon[player.weapon.index(option_2)]
                if player.currentweapon == "Basic Sword":
                    player.attack = 15
                elif player.currentweapon == "Katana":
                    player.attack = 35
                elif player.currentweapon == "Dragon Slayer":
                    player.attack = 75
                elif player.currentweapon == "Odachi":
                    player.attack = 150
                print(f"You have equipped {player.currentweapon}")
                option = input(' ')
            elif option_2 == "Back":
                return
            else: 
                print("That is not a valid option")
                equip(player)
        equip(player)
    elif option == "2":
        return
    else:
        print("Please pick a valid option")
        inventory(player)