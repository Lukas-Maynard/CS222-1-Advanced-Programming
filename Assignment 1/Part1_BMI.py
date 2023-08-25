# BMI = (weight * 703) / (height)2

height = input("Enter your height:")
weight = input("Enter your weight:")

bmi = (weight * 703) / (height) * 2

if bmi < 18.5:
    print("You are considerd underweight.")
elif bmi >= 18.5 and bmi <= 25:
    print("You are considered to be an optimal weight.")
else:
    print("You are considered overweight.")