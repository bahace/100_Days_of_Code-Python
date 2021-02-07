import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# get what the human will throw, convert to int
human_throw = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
if human_throw >= 3 or human_throw < 0:
    print("Invalid Number, you lose")
    exit()

# make a list of the options and print the ascii for the human throw
rps = [rock, paper, scissors]
print("You chose")
print(rps[human_throw])

# formatting print
print("Computer chose")

# get the cpu throw via random and print the ascii for it
cpu_throw = random.randint(0, 2)
print(rps[cpu_throw])

# determine and print who wins if human chooses 0/rock
if human_throw == 0:
    if cpu_throw == 0:
        print("Draw")
    elif cpu_throw == 1:
        print("You lose")
    elif cpu_throw == 2:
        print("You win")

# determine and print who wins if human chooses 1/paper
if human_throw == 1:
    if cpu_throw == 0:
        print("You win")
    elif cpu_throw == 1:
        print("Draw")
    elif cpu_throw == 2:
        print("You lose")

# determine and print who wins if human chooses 2/scissors
if human_throw == 2:
    if cpu_throw == 0:
        print("You lose")
    elif cpu_throw == 1:
        print("You win")
    elif cpu_throw == 2:
        print("Draw")
