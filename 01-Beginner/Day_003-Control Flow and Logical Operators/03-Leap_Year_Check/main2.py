# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if year % 4 == 0:
    message = "Leap year"
    if year % 100 == 0:
        message = 'Not Leap year'
        if year % 400 == 0:
            message = 'Leap year'
else:
    message = 'Not Leap year'

print(message)
