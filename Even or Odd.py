import os

process = True
while process:
    os.system("cls")
    print("Even or Odd\n")

    num = int(input("Enter any number: "))

    if num % 2 == 0:
        print(f"\n{num} is an even number.")
    else:
        print(f"\n{num} is an odd number.")

    input()
