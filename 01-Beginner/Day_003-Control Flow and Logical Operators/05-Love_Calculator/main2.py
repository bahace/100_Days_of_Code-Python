# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
name1 = name1.lower()
name2 = name2.lower()
# Couldve combined the names to make it easier. DOH
# combined_name = name1 + name2
t_number = (name1 + name2).count("t")
r_number = (name1 + name2).count("r")
u_number = (name1 + name2).count("u")
e_number = (name1 + name2).count("e")

l_number = (name1 + name2).count("l")
o_number = (name1 + name2).count("o")
v_number = (name1 + name2).count("v")

tens_digit = str(t_number + r_number + u_number + e_number)
singles_digit = str(l_number + o_number + v_number + e_number)
score = str(tens_digit + singles_digit)
score = int(score)

if score < 10 or score > 90:
    message = f"Your score is {score}, you go together like coke and mentos"
elif 40 < score < 50:
        message = f"Your score is {score}, you are alright together"
else:
    message = f"Your score is {score}"

print(score)
print(message)

