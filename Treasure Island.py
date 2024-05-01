print("Treasure Island\n")

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n")

decision1 = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'\n").lower()
if decision1 == "left":
    decision2 = input("\nYou come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
    if decision2 == "wait":
        decision3 = input("\nYou arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n").lower()
        if decision3 == "yellow":
            print("\nYou found the Treasure. You Win!")
        else:
            print("\nYou've entered a furnace. Game Over.")
    else:
        print("\nYou can't survive in the lake, it's too cold. Game Over.")
else:
    print("\nYou've entered a restricted zone. Game Over.")
input()