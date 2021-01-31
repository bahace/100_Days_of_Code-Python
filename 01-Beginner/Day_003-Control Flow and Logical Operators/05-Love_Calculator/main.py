# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
name1 = name1.lower()
name2 = name2.lower()

# coudlve also combined names and then checked just one name
# combined_name = name1 + name2

countT = name1.count("t") + name2.count("t")
countR = name1.count("r") + name2.count("r")
countU = name1.count("u") + name2.count("u")
countE = name1.count("e") + name2.count("e")

countL = name1.count("l") + name2.count("l")
countO = name1.count("o") + name2.count("o")
countV = name1.count("v") + name2.count("v")

tens_digit = countT + countR + countU + countE
singles_digit = countL + countO + countV + countE

# Have to turn numbers into strings to combine (concatenate) them.
# Turn back into int to run logical operators against them
score = int(str(tens_digit) + str(singles_digit))

if score < 10 or score > 90:
    message = f"Your score is {score}, you go together like coke and mentos"
elif score > 40 and score < 50:
    message = f"Your score is {score}, you are alright together"
else:
    message = f"Your score is {score}"

print(message)
