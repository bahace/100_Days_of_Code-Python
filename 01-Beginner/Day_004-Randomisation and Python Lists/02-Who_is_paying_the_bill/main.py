# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
import random
print(names)
number_of_people = len(names)
print(number_of_people)
random_draw = random.randint(1, number_of_people)
bill_payer = names[random_draw]
message = f"{bill_payer} is going to buy the meal today!"
print(message)
