from main import player, Menu


class Store():
    def store():
        print("Welcome to the Store!")
        print("\nWhat would you like to purchase? (Enter full name of item)\n")
        print("1.) Katana (50 Gold)")
        print("2.) Dragon Slayer (200 Gold)")
        print("3.) AK-47 (500 Gold)")
        print("4.) Potion (10 Gold)")
        print("5.) Back")
        option = input(' ')
        if option == "1":
            weapon = "Katana"
            if player.gold >= 50:
                player.gold -= 50
                player.weapon.append(weapon)
                print(f"You have bought a Katana")
                option = input(' ')
                Store.store()
            else:
                print("You don't have enough gold")
                option = input(' ')
                Store.store()
        elif option == "2":
            weapon = "Dragon Slayer"
            if player.gold >= 200:
                player.gold -= 200
                player.weapon.append(weapon)
                print(f"You have bought the Dragon Slayer")
                option = input(' ')
                Store.store()
            else:
                print("You don't have enough gold")
                option = input(' ')
                Store.store()
        elif option == "3":
            weapon = "AK-47"
            if player.gold >= 500:
                player.gold -= 500
                player.weapon.append(weapon)
                print(f"You have bought an AK-47")
                option = input(' ')
                Store.store()
            else:
                print("You don't have enough gold")
                option = input(' ')
                Store.store()
        elif option == "4":
            if player.gold >= 10:
                player.gold -= 10
                player.potions += 1
                print(f"You have bought a potion")
                option = input(' ')
                Store.store()
            else:
                print("You don't have enough gold")
                option = input(' ')
                Store.store()
        elif option == "5":
            Menu.menu()
        else:
            print("Please pick a valid option")
            Store.store()