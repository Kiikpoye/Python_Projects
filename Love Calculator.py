print("Love Calculator\n")

name1 = input("What is your name? \n")
name2 = input("\nWhat is their name? \n")

name01 = name1.lower()
name02 = name2.lower()

T = name01.count("t")
R = name01.count("r")
U = name01.count("u")
E = name01.count("e")

L = name01.count("l")
O = name01.count("o")
V = name01.count("v")
E = name01.count("e")

name001 = str(T + R + U + E + L + O + V + E)

T = name02.count("t")
R = name02.count("r")
U = name02.count("u")
E = name02.count("e")

L = name02.count("l")
O = name02.count("o")
V = name02.count("v")
E = name02.count("e")


name002 = str(T + R + U + E + L + O + V + E)

love_score = int(name001 + name002)

if (love_score < 10) or (love_score) > 90:
    print(f"\nYour score is {love_score}, you go together like coke and mentos")
elif (love_score >= 40) and (love_score) <= 50:
    print(f"\nYour score is {love_score}, you are alright together.")
else:
    print(f"\nYour score is {love_score}.")

input()