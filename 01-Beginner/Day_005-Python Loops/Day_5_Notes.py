# 5.48 Using the for loop with Python Lists
fruits = ["Apple", "Peach", "Pear"]
for item in fruits:
    print(item)
    print(item + " Pie")
    # inside vs outside for loop
    # inside
    print(fruits)
# outside
print(fruits)
# inside for loops, its proper form to name it the singular form of the list. fruit for list of fruits.

# 5.51 for loops and the range() function
# for number in range(1, 11, 3):
# print(number)
for number in range(1, 10):
    print(number)
# ranges dont include last number, but do include the first number
# we can also change the "step" size by adding a 3rd number in the range function. the 3rd number is the step.:
for number in range(1, 10, 3):
    print(number)

total = 0
for number in range(1, 101):
    total += number
print(total)