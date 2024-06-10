import os

class Inventory():
    def inventory(player):
        print("What do you want to do?")
        print("1.) Equip Weapon")
        print("2.) Go back")
        option = input("--> ")
        if option == "1":
            os.system('cls')
            def equip(player):
                print(f"{player.weapons}\n")
                print("What do you want to equip? (Write out full name of item) (Type back to return)\n")
                option_2 = input("--> ").title()
                if option_2 in player.weapons:
                    player.currentweapon = player.weapons[player.weapons.index(option_2)]
                    if player.currentweapon == "Basic Sword":
                        player.attack = 10
                    elif player.currentweapon == "Katana":
                        player.attack = 30
                    elif player.currentweapon == "Dragon Slayer":
                        player.attack = 60
                    elif player.currentweapon == "Odachi":
                        player.attack = 120
                    else:
                        player.currentweapon == "Antithesis"
                        player.attack = 500
                    print(f"You have equipped {player.currentweapon}")
                    option = input(' ')
                elif option_2 == "Back":
                    return
                else: 
                    equip(player)
            equip(player)
        elif option == "2":
            return
        else:
            print("Please pick a valid option")
            Inventory.inventory(player)