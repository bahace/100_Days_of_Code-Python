## Notes for 3.27
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

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


## Notes for 3.29
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
# if height > 120:
#     print("you can ride!")
#     age = int(input("What is your age?"))
#     if age < 12:
#         print("that will be $5")
#     elif age <= 18:
#         print("Please pay $7")
#     else:
#         print("THat will be $12")
# else:
#     print("you need to grow a little more")
#

## Notes for 3.32 - multiple IF statements.
# if height > 120:
#     print("you can ride!")
#     age = int(input("What is your age?"))
#     if age < 12:
#         print("Child tickets are $5")
#         bill = 5
#     elif age <= 18:
#         print("Youth tickets are $7")
#         bill = 7
#     else:
#         print("Adult tickets are $12")
#         bill = 12
#     wants_photo = input("Do you want a photo taken? Y or N. ")
#     if wants_photo == "Y":
#         # Add $3 to bill
#         # bill = bill + 3
#         bill += 3 # same as above, but shorter
#
#     print(f"Your final bill is ${bill}")
#
# else:
#     print("you need to grow a little more")

## Notes for 3.34 Logical Operators
# and - both must be true
# or - one option must be true
# not - the opposite
if height > 120:
    print("you can ride!")
    age = int(input("What is your age?"))
    if age < 12:
        print("Child tickets are $5")
        bill = 5
    elif age <= 18:
        print("Youth tickets are $7")
        bill = 7
    elif age >= 45 and age <= 55:
        print("you are in midlife crisis, have free ticket!")
        bill == 0
    else:
        print("Adult tickets are $12")
        bill = 12
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        # Add $3 to bill
        # bill = bill + 3
        bill += 3 # same as above, but shorter

    print(f"Your final bill is ${bill}")

else:
    print("you need to grow a little more")
