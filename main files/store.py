import os 

class Store():
    def store(player):
        os.system('cls')
        print("Welcome to the Store!\n")
        print("What would you like to purchase?\n")
        print(f"You have {player.gold} gold")
        print("1.) Katana (30 Gold)")
        print("2.) Dragon Slayer (100 Gold)")
        print("3.) Odachi (250 Gold)")
        print("4.) Antithesis (1000 Gold) (Requires 25 Mob kills)")
        print("5.) Shodai Kitetsu (2500 Gold) (Requires 50 Quest Completions )")
        print("6.) Potion (5 Gold)")
        print("7.) Back")
        option = input(' ')
        if option == "1":
            weapon = "Katana"
            if weapon in player.weapons:
                print("You already have this weapon")
                option = input(' ')
                Store.store(player)
            elif player.gold >= 30:
                player.gold -= 30
                player.weapons.append(weapon)
                print("You have bought a Katana")
                player.storepurchase = True
                return input(" ")
            else:
                print("You don't have enough gold")
                option = input(' ')
                Store.store(player)
        elif option == "2":
            weapon = "Dragon Slayer"
            if weapon in player.weapons:
                print("You already have this weapon")
                option = input(' ')
                Store.store(player)
            elif player.gold >= 100:
                player.gold -= 100
                player.weapons.append(weapon)
                print("You have bought the Dragon Slayer")
                player.storepurchase = True
                return input(" ")
            else:
                print("You don't have enough gold")
                option = input(' ')
                Store.store(player)
        elif option == "3":
            weapon = "Odachi"
            if weapon in player.weapons:
                print("You already have this weapon")
                option = input(' ')
                Store.store(player)
            elif player.gold >= 250:
                player.gold -= 250
                player.weapons.append(weapon)
                print("You have bought an Odachi") 
                player.storepurchase = True
                return input(" ")  
            else:
                print("You don't have enough gold")
                option = input(' ')
                Store.store(player)
        elif option == "4":
            if player.mobkills >= 25:
                weapon = "Antithesis"
                if weapon in player.weapons:
                    print("You already have this weapon")
                    option = input(' ')
                    Store.store(player)
                elif player.gold >= 1000:
                    player.gold -= 1000
                    player.weapons.append(weapon)
                    print("You have bought the Antithesis") 
                    player.storepurchase = True
                    return input(" ")
                else:
                    print("You don't have enough gold")
                    option = input(' ')
                    Store.store(player)  
            else:
                print("You don't have enough Mob Kills")
                option = input(' ')
                Store.store(player)
        elif option == "5": 
            if player.questcompletes >= 50:
                weapon = "Shodai Kitetsu"
                if weapon in player.weapons:
                    print("You already have this weapon")
                    option = input(' ')
                    Store.store(player)
                elif player.gold >= 2500:
                    player.gold -= 2500
                    player.weapons.append(weapon)
                    print("You have bought the Shodai Kitetsu") 
                    player.storepurchase = True
                    return input(" ")
                else:
                    print("You don't have enough gold")
                    option = input(' ')
                    Store.store(player)  
            else:
                print("You don't have enough Quest Completions")
                option = input(' ')
                Store.store(player)
        elif option == "6":
            if player.gold >= 5:
                player.gold -= 5
                player.potions += 1
                print(f"You have bought a potion")
                player.storepurchase = True
                print(f"You have {player.potions} potions")
                option = input(' ')
                Store.store(player)
            else:
                print("You don't have enough gold")
                option = input(' ')
                Store.store(player)
        elif option == "7":
            return
        else:
            print("Please pick a valid option")
            option = input(" ")
            Store.store(player)
