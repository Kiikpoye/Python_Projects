print("Welcome to the rollercoaster!\n")
height = int(input("What is your height in cm?\n"))

if height >= 120:
    print("You can ride the rollercoaster!\n")
    age = int(input("What is your age?\n"))
    if age < 12:
        print("\nPlease pay $5")
    elif age <= 18:
        print("\nPlease pay $7")
    elif age >= 40 and age <= 55:
        print("\nDon't worry, everything will be alright. Please pay $0")
    else:
        print("\nPlease pay $12")
else:
    print("\nYou cannot ride the rollercoaster")
input()
