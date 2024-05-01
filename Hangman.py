import random
import os

print('''
 _
| |  
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_  \

| | | | ( | | | | | ( | | | | | | | ( | | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |
                   |___/    ''')

    
stages = ['''
  +---+
  |   |
  0   |
 /|\  |
 / \  |
      |
=========
''','''
  +---+
  |   |
  0   |
 /|\  |
 /    |
      |
=========
''','''
  +---+
  |   |
  0   |
 /|\  |
      |
      |
=========
''','''
  +---+
  |   |
  0   |
 /|   |
      |
      |
=========
''','''
  +---+
  |   |
  0   |
  |   |
      |
      |
=========
''','''
  +---+
  |   |
  0   |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6
display = []
for _ in range(word_length):
    display += "_"

while end_of_game == False:
    guess = input("Guess a letter: ").lower()
    
    os.system("cls")
    
    if guess in display:
        print(f"You've already guessed {guess}")
    
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter     
    print(display)

    if guess not in chosen_word:
        print(f"You guessed {guess} that's not in the word. You lose a life.")
        lives -= 1
        if lives == 5:
            print(stages[5])
        elif lives == 4:
            print(stages[4])
        elif lives == 3:
            print(stages[3])
        elif lives == 2:
            print(stages[2])
        elif lives == 1:
            print(stages[1])
        else:
            end_of_game = True
            print("You loose")
            print(stages[0])
            
            
    if "_" not in display:
        end_of_game = True
        print("\nYou win.")

input()
