# Notes for 3.27
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

# if we want to include 120, use ">="
# if height > 120:
#   print("Let's Ride!!!!")
# else:
#    print("you need to grow a little more :(")

# comparison operators
# > Greater than
# < Less than
# >= Greater than or equal to
# <= Less than or equal to
# == Equal to
# != Not equal to

# modulo
# print(7 % 2)
# modulo gives you the remainder


# Notes for 3.29
# nested if statements.
# if height > 120:
#     print("you can ride!")
#     age = int(input("What is your age?"))
#     if age <= 18:
#         print("that will be $7")
#     else:
#         print("THat will be $12")
# else:
#     print("you need to grow a little more")
# end of nested if

# elif
# you can add as many elif conditions that you like.
if height > 120:
    print("you can ride!")
    age = int(input("What is your age?"))
    if age < 12:
        print("that will be $5")
    elif age <= 18:
        print("Please pay $7")
    else:
        print("THat will be $12")
else:
    print("you need to grow a little more")