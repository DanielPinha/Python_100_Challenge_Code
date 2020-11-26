print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice = input("you are at a crossroad. Where do you want to go? type 'left' or 'right'\n")
if choice.lower() == "left":
    choice = input("You found a lake! There is an island in the middle, do you swim or wait for a boat? type 'swim' or "
                   "'wait'\n")
    if choice.lower() == "wait":
        choice = input("You found a house and entered. there are 3 doors, time to make a choice. type 'red', "
                       "'blue' or 'yellow'\n")
        if choice.lower() == 'yellow':
            print("You open the door and.. you find the treasure! YOU WIN (Sad Developer noises)")
        elif choice.lower() == "red":
            print("What is that smell? You are burned by fire. Game Over!")
        elif choice.lower() == "blue":
            print("You sneak your head out of the door and a giant squirrel bits your head! Game Over")
        else:
            print("You tried an unnamed door, but the jock is on you! the time-space collapses and you died. "
                  "Game Over!")
    elif choice.lower() == "swim":
        print("Sardine attack! yeah.. Game Over for you")
    else:
        print("Your choice breaks my game or so you believed. flying monkeys punch you in the gut. Game Over")
elif choice.lower() == "right":
    print("Fell into a hole. This is game over to you!")
else:
    print("The developer saw that coming. He mocks your effort! Game Over")
