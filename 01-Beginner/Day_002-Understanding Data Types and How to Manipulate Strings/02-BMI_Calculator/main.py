# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
fl_height = float(height)
fl_weight = float(weight)

bmi = int(fl_weight / fl_height ** 2)
print(bmi)
