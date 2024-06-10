import random

class Quest():
    def quest(player):
        questchance = random.randint(1,3)
        print("1.) Accept Quest")
        print("2.) Finish Quest")
        print("3.) Abandon Quest")
        print("4.) Back ")
        option = input(" ")
        if option == "1":
            if questchance == 1:
                quest1 = True
                print("Defeat 10 mobs")
                option = input(" ")
            elif questchance == 2:
                quest2 = True 
                print("Purchase an item from the shop")
                option = input(" ")
            elif questchance == 3:
                quest3 = True
                print("Donate 50 gold")
        elif option == "2":
            if quest1 == True:
                if player.mobkills == 10:
                    player.questcompletes += 1 
                    print("Quest 1 completed ")
                    return input(" ")
                else:
                    print("You are not done with your quest yet")
                    return input(" ")
            elif quest2 == True: 
                if player.storepurchase == True: 
                    player.questcompletes += 1 
                    print("Quest 2 completed ")
                    return input(" ")
                else:
                    print("You are not done with your quest yet")
                    return input(" ")
            elif quest3 == True:
                if player.gold >= 50:
                    player.gold -= 50
                    player.questcompletes += 1 
                    print("Quest 3 completed ")
                    return input(" ")
                else:
                    print("You are not done with your quest yet")
                    return input(" ")
        elif option == "3":
            quest1 = False
            quest2 = False
            quest3 = False
        elif option == "4":
            return