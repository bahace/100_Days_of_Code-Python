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
 _________|___________| ;`-.o`"=._; ." ` '`."|` . "-._ /_______________|_______
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

decision_1 = input("Do you want to go left or right? \n").lower()
if decision_1 == "left":
    print("you are stupid, never go left")
    exit(-1)
else:
    print("good call, right is the way. \n")

decision_2 = input("You see an island in the distance. Do you swim or wait for the ferry? \n").lower()
if decision_2 == "swim":
    print("you are eaten by a magikarp, game over")
    exit(-2)
else:
    print("Yoda likes your patience, he summons a ferry from the deep. \n\nYou made it to the island. In the house,"
          "you see three doors.")

decision_3 = input("What door do you open? \nRed, Green, Blue?\n").lower()
if decision_3 == "red":
    print("You win!")
    exit(1)
else:
    print("Wrong, game over")
    exit(-3)
