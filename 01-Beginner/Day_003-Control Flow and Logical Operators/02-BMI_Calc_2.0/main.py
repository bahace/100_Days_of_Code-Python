# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = round(weight / height ** 2)

# print (bmi)
#

if bmi < 18.5:
    message = f"your BMI is {bmi}, you are underweight"
elif bmi <= 25:
    message = f"your BMI is {bmi}, you are normal weight"
elif bmi <= 30:
    message = f"your BMI is {bmi}, you are slightly over weight"
elif bmi <= 35:
    message = f"your BMI is {bmi}, you are obese weight"
else:
    message = f"your BMI is {bmi}, you are clinically obese"

print(message)