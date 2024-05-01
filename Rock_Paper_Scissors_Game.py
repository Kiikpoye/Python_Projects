import random

rock = '''
    _______
---'   ____)
       (____)
       (____)
      (____)
---'__(___)
'''

paper = '''
    _______
---'   ____)____
       	  ______)
          _______)
         _______)
---'__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---'__(___)
'''

mylist = [rock, paper, scissors]

game_on = True
while game_on:
    player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    print(mylist[player_choice])

    computer_choice = random.randint(0, 2)
    print("Computer choose: ")
    print(mylist[computer_choice]) 


    if player_choice >= 3 or player_choice < 0:
        print("You typed an invalid number, you lose!")
    elif player_choice == 0 and computer_choice == 2:
        print("You Win!")
    elif computer_choice == 0 and player_choice == 2:
        print("You Lose")
    elif computer_choice > player_choice:
        print("You Lose")
    elif player_choice > computer_choice:
        print("You Win!")
    elif computer_choice == player_choice:
        print("It's a draw")

    should_continue = input("Type 'y' to continue or 'n' to exit: ")
    if should_continue == "n":
        game_on = False
    else:
        game_on
input()