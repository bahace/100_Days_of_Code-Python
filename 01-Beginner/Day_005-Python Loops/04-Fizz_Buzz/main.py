# Write your code below this row 👇

for number in range(1, 101):

    # divisible by 3 and 5
    if number % 3 == 0 and number % 5 == 0:
        print("Fizz Buzz")

    # divisible by 3 only
    elif number % 3 == 0:
        print("Fizz")

    # divisible by 5 only
    elif number % 5 == 0:
        print("Buzz")

    # print number with no fizz buzz
    else:
        print(number)
