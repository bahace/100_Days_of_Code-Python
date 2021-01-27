# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
int_age = int(age)
total_days = 365 * 90
total_weeks = 52 * 90
total_months = 12 * 90
remaining_days = total_days - int_age * 365
remaining_weeks = total_weeks - int_age * 52
remaining_months = total_months - int_age * 12


message = f"You have {remaining_days} days, {remaining_weeks} weeks, and {remaining_months} months left."
print(message)
