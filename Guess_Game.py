import random

number = random.randint(1, 100)

print("Welcome to the Number Guesssing Game!")
print("I'm thinking of a number between 1 and 100.")

def level():
    level = input("Choose a difficulty, Type 'easy' or 'hard': ")
    if level == "easy":
        return 10
    else:
        return 5
attempts = level()

game_on = True
while attempts and game_on:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess > number:
        attempts -= 1
        print("Too high.")
        if attempts == 0:
            print("You've run out of guesses, you lose.")
    elif guess < number:
        attempts -= 1
        print("Too low.")
        if attempts == 0:
            print("You've run out of guesses, you lose.")
    else:
        game_on = False
        print(f"You got it, the answer was {number}")

    if guess != number and attempts == 0:
        game_on = False
    elif guess != number:
        print("Guess again.")
input()
