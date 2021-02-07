# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
# # Joey Solve
# column = int(position[0]) - 1
# row = int(position[1])
#
# if row == 1:
#     row1[column] = "X"
#
# if row == 2:
#     row2[column] = "X"
#
# if row == 3:
#     row3[column] = "X"

# Teacher solve
column = int(position[0])
row = int(position[1])

selected_row = map[row - 1]
selected_row[column - 1] = "X"

# Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")