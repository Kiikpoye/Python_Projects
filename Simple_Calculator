def myfunction():
    import os
    Calculator = True
    while Calculator:
        os.system("clear")
        x = int(input("Enter a number: "))
        select = input("""
Select an operator: ^ × ÷ + - \n
    """)
        y = int(input("\nEnter a number: "))
    
        exponent = x**y
        multiply = x*y
        divide = x/y
        add = x+y
        subtract = x-y
    
        if select == "^":
            print(f"\nAnswer = {exponent}")
        elif select == "×":
            print(f"\nAnswer = {multiply}")
        elif select == "÷":
            print(f"\nAnswer = {divide}")
        elif select == "+":
            print(f"\nAnswer = {add}")
        elif select == "-":
            print(f"\nAnswer = {subtract}")
        else:
            print("\nInvalid operator")
        prompt = input("\nAre you done with the calculator?\nType 'yes' or 'no': ").lower()
        if prompt == "no":
            Calculator
        elif prompt == "yes":
            Calculator = False
        else:
            error_prompt = input("Please, input 'yes' or 'no'\n").lower()
            if error_prompt == "yes":
                Calculator = False
            elif error_prompt == "no":
                Calculator
            else:
                Calculator = False
                print("Invalid input, run the code again")
myfunction()

