from time import sleep
import random

#Vars
game = ("[{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}]")
Ground = "-"
Plr = "i"
#Start Game
print(game.format(Plr,Ground,Ground,Ground,Ground,Ground,Ground,Ground,Ground,Ground,Ground,Ground,Ground,Ground,Ground))
# Slots

Slot1 = "i"
Slot2 = "-"
Slot3 = "-"
Slot4 = "-"
Slot5 = "-"
Slot6 = "-"
Slot7 = "-"
Slot8 = "-"
Slot9 = "-"
Slot10 = "-"
Slot11 = "-"
Slot12 = "-"
Slot13 = "-"
Slot14 = "-"
Slot15 = "-"

# Movement

while True:
    MoveTo = input()
    MoveForward = None
    Fight = False

    #Checks if forward or backwards
    
    if MoveTo.lower() == "w":
       MoveForward = True
    elif MoveTo.lower() == "s":
        MoveForward = False
    elif MoveTo.lower() == "f":
        Fight = True



        #Checks Where Plr is and sets new pos

    if MoveForward == True or MoveForward == False or Fight == True:
        if Slot1 == "i":
            if MoveForward == True:
                Slot1 = "-"
                Slot2 = "i"
            elif MoveForward == False:
                Slot1 = "i"
                Slot2 = "-"
        elif Slot2 == "i":
            if MoveForward == True:
                Slot2 = "-"
                Slot3 = "i"
            elif MoveForward == False:
                Slot1 = "i"
                Slot2 = "-"
        elif Slot3 == "i":
            if MoveForward == True:
                Slot3 = "-"
                Slot4 = "i"
            elif MoveForward == False:
                Slot2 = "i"
                Slot3 = "-"
        elif Slot4 == "i":
            if MoveForward == True:
                Slot4 = "-"
                Slot5 = "i"
            elif MoveForward == False:
                Slot3 = "i"
                Slot4 = "-"
        elif Slot5 == "i":
            if MoveForward == True:
                Slot5 = "-"
                Slot6 = "i"
            elif MoveForward == False:
                Slot4 = "i"
                Slot5 = "-"
        elif Slot6 == "i":
            if MoveForward == True:
                Slot6 = "-"
                Slot7 = "i"
            elif MoveForward == False:
                Slot5 = "i"
                Slot6 = "-"
        elif Slot7 == "i":
            if MoveForward == True:
                Slot7 = "-"
                Slot8 = "i"
            elif MoveForward == False:
                Slot6 = "i"
                Slot7 = "-"
        elif Slot8 == "i":
            if MoveForward == True:
                Slot8 = "-"
                Slot9 = "i"
            elif MoveForward == False:
                Slot7 = "i"
                Slot8 = "-"
        elif Slot9 == "i":
            if MoveForward == True:
                Slot9 = "-"
                Slot10 = "i"
            elif MoveForward == False:
                Slot8 = "i"
                Slot9 = "-"
        elif Slot10 == "i":
            if MoveForward == True:
                Slot10 = "-"
                Slot11 = "i"
            elif MoveForward == False:
                Slot9 = "i"
                Slot10 = "-"
        elif Slot11 == "i":
            if MoveForward == True:
                Slot11 = "-"
                Slot12 = "i"
            elif MoveForward == False:
                Slot10 = "i"
                Slot11 = "-"
        elif Slot12 == "i":
            if MoveForward == True:
                Slot12 = "-"
                Slot13 = "i"
            elif MoveForward == False:
                Slot11 = "i"
                Slot12 = "-"
        elif Slot13 == "i":
            if MoveForward == True:
                Slot13 = "-"
                Slot14 = "i"
            elif MoveForward == False:
                Slot12 = "i"
                Slot13 = "-"
        elif Slot15 == "D":
            if MoveForward == True or MoveForward == False:
                print("Game Over!")
                sleep(2)
                quit()
            elif Fight == True:
                Slot15 = "-"
                GameLayout = game.format(Slot1,Slot2,Slot3,Slot4,Slot5,Slot6,Slot7,Slot8,Slot9,Slot10,Slot11,Slot12,Slot13,Slot14,Slot15)
                print(GameLayout)

        elif Slot14 == "i":
            if MoveForward == True:
                Slot14 = "-"
                Slot15 = "i"
            elif MoveForward == False:
                Slot13 = "i"
                Slot14 = "-"
            
        elif Slot15 == "i":
            if MoveForward == False:
                Slot15 = "-"
                Slot14 = "i"
            
            


    RandomNum = random.randint(0,8)
    if RandomNum == 8:
        Slot15 = "D"
    
    #Draws layout
    GameLayout = game.format(Slot1,Slot2,Slot3,Slot4,Slot5,Slot6,Slot7,Slot8,Slot9,Slot10,Slot11,Slot12,Slot13,Slot14,Slot15)
    print(GameLayout)


