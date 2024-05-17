from imports import Menu, player


class Inventory():
    def inventory():
        print("What do you want to do?")
        print("1.) Equip Weapon")
        print("2.) Go back")
        option = input("--> ")
        if option == "1":
            Equip.equip()
        elif option == "2":
            Menu.menu()
        else:
            print("Please pick a valid option")
            Inventory.inventory

class Equip():
    def equip():
        print(f"{player.weapon}")
        print("What do you want to equip? (Write out full name of item)")
        option = input("--> ").title()
        if option == "Katana":
            player.currentweapon = ["Katana"]
            print(f"{option} Equipped")
            option = input(' ')
            Menu.menu()
        elif option == "Dragon Slayer":
            player.currentweapon = ["Dragon Slayer"]
            print(f"{option} Equipped")
            option = input(' ')
            Menu.menu()
        elif option == "AK-47":
            player.currentweapon = ["AK-47"]
            print(f"{option} Equipped")
            option = input(' ')
            Menu.menu()
        elif option == "Basic Sword":
            player.currentweapon = ["Basic Sword"]
            print(f"{option} Equipped")
            option = input(' ')
            Menu.menu()
