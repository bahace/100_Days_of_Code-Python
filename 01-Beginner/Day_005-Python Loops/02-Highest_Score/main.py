# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

# in this challenge, can not use the following functions:
# max()
# min()

# Write your code below this row 👇
# set high score variable
high_score = 0
# for loop to check students score vs current high score variable
for score in student_scores:
    if high_score < score:
        high_score = score
# print high score
print(high_score)
