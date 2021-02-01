# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
import random

# get the number of people in the list just entered
number_of_people = len(names)
# generate a random number that has the same range as integer amount of people in the list
random_draw = random.randint(0, number_of_people - 1)
# assign bill payer variable from list using random integer
bill_payer = names[random_draw]
# save message
message = f"{bill_payer} is going to buy the meal today!"
print(message)
