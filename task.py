print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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
choice_1 = input('You\'re at a cross road, where do what to go? Type "Left" or "Right" ').lower()

if choice_1 == "left":
    choice_2 = input('You\'ve come to a lake. There is an island in middle of lake. Type "Wait or "Swim"').lower()
    if choice_2 == "wait":
        choice_3 = input("You arrive at the island unharmed.There house with three doors. One red, one yellow and one blue.Which colour do choose?").lower()
        if  choice_3 == "red":
            print("It's room of full of fire. Game Over")
        elif choice_3 == "yellow":
            print("You found the treasure. You Win")
        elif choice_3 == "blue":
            print("You enter the room of beasts. Game Over")
        else:
            print("You chose a door that doesn't exist. Game Over ")
    else:
        print("You got attacked by an angry trout. Game over")
else:
    print("You Fall into a Hole. Game Over")