import random
from time import sleep

game = ["i","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"]
MoveForward = False
MoveBackwards = False
Fight = False

#Prints Starting Game

print("[",end="")
for items in game:
    print(items,end="")
print("]",end="")
print("\n")



while True:
    #Mobs
    Mobs = ["D","B"]
    MobChoice = random.choice(Mobs)
    RandomNum = random.randint(0,5)
    SpawnPoint = random.randint(0,19)
    PlrPos = game.index("i")

    #Gets movement input
    MoveTo = input()

    #Gets Movement keys
    if MoveTo.lower() == "w":
        MoveForward = True
    elif MoveTo.lower() == "s":
        MoveBackwards = True
    elif MoveTo.lower() == "f":
        Fight = True

    
    #Mobs
    if MoveForward or MoveBackwards == True:
        if RandomNum == 4:
            if PlrPos != SpawnPoint:
                game[SpawnPoint] = MobChoice
            else:
                pass

    #Does actions
    if MoveForward == True:
        if PlrPos <= 18:
            if game[PlrPos + 1] == "B" or game[PlrPos + 1] == "D":
                print("Game Over!")
                sleep(2)
                quit()
            else:
                game[PlrPos] = "-"
                PlrPos += 1
                game[PlrPos] = "i"
        else:
            pass
    elif MoveBackwards == True:
        if PlrPos >= 1:
            if game[PlrPos - 1] == "B" or game[PlrPos - 1] == "D":
                print("Game Over!")
                sleep(2)
                quit()
            else:
                game[PlrPos] = "-"
                PlrPos -= 1
                game[PlrPos] = "i"
        else:
            pass

    #Fighting
    if Fight == True:
        if game[PlrPos + 1] == "B" or game[PlrPos + 1] == "D":
            game[PlrPos + 1] = "-"
        elif game[PlrPos - 1] == "B" or game[PlrPos - 1] == "D":
            game[PlrPos - 1] = "-"

    #Invalid Key Error
    elif MoveBackwards == False and MoveForward == False and Fight == False:
        print("Invalid Key",end="\n")
        print("\n")

    
    #Prints GameLayout
    print("[",end="")
    for items in game:
        print(items,end="")
    print("]",end="")

    print("\n")
    MoveForward = False
    MoveBackwards = False
    Fight = False
            
