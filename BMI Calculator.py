print("BMI Calculator\n")

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))

BMI = weight / height**2
Answer = round(BMI, 2)

if Answer < 18.5:
    print(f"""\nYour BMI is {Answer}kg/m.square
You are underweight""")
elif Answer >= 18.5 and Answer < 25:
    print(f"""\nYour BMI is {Answer}kg/m.square
You are normal""")
elif Answer >= 25 and Answer < 30:
    print(f"""\nYour BMI is {Answer}kg/m.square
You are overweight""")
elif Answer >= 30 and Answer < 35:
    print(f"""\nYour BMI is {Answer}kg/m.square
You are obese""")
else:
    print(f"""\nYour BMI is {Answer}kg/m.square
You are clinically obese""")
input()

