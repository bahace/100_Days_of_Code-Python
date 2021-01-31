dog = '''
**********************************
              _=,_
           o_/6 /#|
           \__ |##/
            ='|--|
              /   #'-.
              \#|_   _'-. /
               |/ \_( # |" 
              C/ ,--___/
**********************************
'''


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
print("Welcome to Find Cody.")
print("Your mission is to find Cody, he is lost.")
fork_decision = input("You are at a fork in the road, which way do you go? Left or Right? \n")
fork_decision = fork_decision.lower()

if fork_decision == "right":
    print("You've come to a small lake with an island in the center")
    lake_decision = input("Do you swim or wait for the ferry? \n")
    lake_decision = lake_decision.lower()
    if lake_decision == "swim":
        print("Good call, a ferry comes 10min later and takes you the island")
        door_decision = input("You find a house with 3 colored doors inside, Which one do you choose? Red, Yellow, or Blue? \n")
        door_decision = door_decision.lower()
        if door_decision == "red":
            print(dog)
            print("You found Cody! You win!")
        elif door_decision == "yellow":
            print("A witch traps you in a book and takes you the island of Myst, you lost")
        elif door_decision == "blue":
            print("You should never pick blue, you lose")
        else:
            print("input error, Game Over")
    else:
        print("You were attacked by a giant trout, you lose")
else:
    print("You fell into a hole, Game Over")