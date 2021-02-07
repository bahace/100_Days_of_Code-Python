# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# in this challenge, can not use the following functions:
# len()
# sum()

# challenge:
# Want to write this in for Loops: for item in list, do something.

# Write your code below this row 👇
# set both sides of fraction to 0
total_height = 0
number_height = 0
# for each item in list of student heights
for height in student_heights:
    # total height sum'd together
    total_height += height
    # number of heights increases by 1 for each item
    number_height += 1


# print statements to ensure math is working properly
print(f" All heights added up are {total_height} cm")
print(f" The total number of heights that you entered are {number_height}")
# calculations, can probably have done it in a single line
avg_height = total_height / number_height
avg_height = int(round(avg_height))
# print final outcome.
print(f" The average height of the ones entered is {avg_height}")
