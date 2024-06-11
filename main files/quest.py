import random, os

class Quest():

    def quest(player):
        global quest1, quest2, quest3, quest4
        questchance = random.randint(1,4)
        os.system('cls')
        print("What would you like to do?\n")
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
                option = input(" ") 
            elif questchance == 4: 
                quest4 = True
                print("Defeat 20 mobs")
                option = input(" ")
        elif option == "2":
            if quest1 is True:
                if player.mobkills >= 10:
                    player.questcompletes += 1 
                    print("Quest 1 completed ")
                    return input(" ")
                else:
                    print("You are not done with your quest yet")
                    return input(" ")
            elif quest2 is True: 
                if player.storepurchase == True: 
                    player.questcompletes += 1 
                    print("Quest 2 completed ")
                    return input(" ")
                else:
                    print("You are not done with your quest yet")
                    return input(" ")
            elif quest3 is True:
                if player.gold >= 50:
                    player.gold -= 50
                    player.questcompletes += 1 
                    print("Quest 3 completed ")
                    return input(" ")
                else:
                    print("You are not done with your quest yet")
                    return input(" ")
            elif quest4 is True:
                if player.mobkills >= 20:
                    player.questcompletes += 2 
                    print("Quest 4 completed ")
                    return input(" ")
                else:
                    print("You are not done with your quest yet")
                    return input(" ")
            else:
                print("You are not done with your quest yet")
                return input(" ")
        elif option == "3":
            quest1 = False
            quest2 = False
            quest3 = False
            quest4 = False 
        elif option == "4":
            return
        else:
            Quest.quest(player)