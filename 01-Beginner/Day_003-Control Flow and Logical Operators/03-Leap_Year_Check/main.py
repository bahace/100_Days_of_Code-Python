# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
check1 = year % 4
check2 = year % 100
check3 = year % 400
if check1 == 0:
    # print("cleanly divisible by 4, running 2nd check")
    if check2 == 0:
        # print("Passed 2nd check, running 3rd check")
        if check3 == 0:
            # print(f"The year {year} passed all check, this is a Leap Year")
            print("leap year")
        else:
            # print(f"The Year {year} failed the final check, it is not a Leap Year")
            print("Not leap year")
    else:
        # print(f"Failed 2nd check, Year {year} is not a leap year.")
        print("Not leap year")
else:
    # print (f"The Year {year} is not cleanly divisible by 4, this is not a leap year")
    print("Not leap year")
