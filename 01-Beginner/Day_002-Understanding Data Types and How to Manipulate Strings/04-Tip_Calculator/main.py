# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
# HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
# HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
tip_percent = float(input("What percentage tip would you like to give? ")) / 100
people = float(input("How many people to split the bill? "))
split_amount = (bill * tip_percent + bill) / people

# round to 2 digits
final_split = round(split_amount, 2)

# format to 2 digits after the decimal
# https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points
final_split = "{:.2f}".format(split_amount)
message = f"Each person should pay ${final_split}"
print(message)
