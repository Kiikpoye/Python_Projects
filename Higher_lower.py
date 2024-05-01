data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social Media Platform',
        'country': 'United States', 
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal', 
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 183,
        'description': 'Musician and actress',
        'country': 'United States', 
    },
    {
        'name': 'Dwayne Johnson',
        'follower_count': 181,
        'description': 'Actor and professional wrestler',
        'country': 'United States', 
    },
    {
        'name': 'Selena Gomez',
        'follower_count': 174,
        'description': 'Musician and actress',
        'country': 'United States', 
    },
    {
        'name': 'Kylie Jenner',
        'follower_count': 172,
        'description': 'Reality TV personality and businesswoman and Self-Made Billionaire',
        'country': 'United States', 
    },
    {
        'name': 'Kim Kardashian',
        'follower_count': 167,
        'description': 'Reality TV personality and businesswoman',
        'country': 'United States', 
    },
    {
        'name': 'Lionel Messi',
        'follower_count': 149,
        'description': 'Footballer',
        'country': 'Argentina', 
    },
    {
        'name': 'Beyonce',
        'follower_count': 145,
        'description': 'Musician',
        'country': 'United States', 
    },
    {
        'name': 'Neymar',
        'follower_count': 138,
        'description': 'Footballer',
        'country': 'Brasil', 
    },
]

import random
import os

# Display art
print("HIGHER LOWER GAME\n")

# Format the account data into printable format.
def format_data(acccount):
    """Takes the account data and returns the printabale format."""
    account_name = acccount["name"]
    account_description = acccount["description"]
    account_country = acccount["country"]
    return f"{account_name}, a {account_description}, from {account_country}."

## Use if statement to check if the user is correct.
def check_guess(guess, follower_count_a, follower_count_b):
    """"Take the user guess and follower counts and returns if they got it right."""
    if follower_count_a > follower_count_b:
        return guess == "a"
    else:
        return guess == "b"

account_b = random.choice(data)

# Score keeping
score = 0

# Make the game repeatable.
game_on = True
while game_on:
    # Generate a random account from game data.
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)            
    
    print(f"Compare A: {format_data(account_a)}")
    print("VS")
    print(f"Against B: {format_data(account_b)}")

    # Ask user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check if user is correct.
    ## Get follower_count of each account. 
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    check_answer = check_guess(guess, a_follower_count, b_follower_count)

    # Clear the screen
    os.system("cls")

    print("HIGHER LOWER\n")

    # Give user feedbcack on their guesses.
    if check_answer:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        game_on = False
        print(f"Sorry, that's wrong. Final score: {score}")

input()
