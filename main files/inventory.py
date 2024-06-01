

def inventory(player):
    print("What do you want to do?")
    print("1.) Equip Weapon")
    print("2.) Go back")
    option = input("--> ")
    if option == "1":
        def equip():
            print(f"{player.weapon}\n")
            print("What do you want to equip? (Write out full name of item)\n")
            option_2 = input("--> ").title()
            if option_2 in player.weapon:
                player.currentweapon = player.weapon[player.weapon.index(option_2)]
                print(f"You have equipped {player.currentweapon}")
                option = input(' ')
            else: 
                print("That is not a valid option")
                equip()
        equip()
    elif option == "2":
        return input(" ")
    else:
        print("Please pick a valid option")
        inventory()