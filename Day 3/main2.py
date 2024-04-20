height = float(input("Enter your height in m : "))
weight = float(input("Enter your weight in kg : "))

bmi = float(weight / (height * height))

if bmi < 18.5:
    print(f"your BMI is {bmi} and you are underweight")
elif bmi < 25:
    print(f"your BMI is {bmi} and you are normal")
elif bmi < 30:
    print(f"your BMi is {bmi} and you are overweight")
elif bmi < 35:
    print(f"your BMI is {bmi} and you are obese")
else:
    print(f"your BMi is {bmi} and you are really fat")
