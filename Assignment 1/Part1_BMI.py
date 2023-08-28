"""
BMI 
Lukas Maynard
CS222-1
Assignment 1 Part 1
"""

height = int(input("Enter your height in inches:"))
weight = int(input("Enter your weight in pounds:"))

bmi = (weight * 703) / (height)**2
print("Your body mass index:", bmi)

if bmi < 18.5:
    print("You are considerd underweight.")
elif bmi >= 18.5 and bmi <= 25:
    print("You are considered to be an optimal weight.")
else:
    print("You are considered overweight.")