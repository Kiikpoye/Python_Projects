import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
           'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
           'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to my PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

len_letters = range(1, nr_letters + 1)
len_numbers = range(1, nr_symbols + 1)
len_symbols = range(1, nr_numbers + 1)


#easy password
password = ""
for char in len_letters:
    password += random.choice(letters)

for char in len_symbols:
    password += random.choice(symbols)

for char in len_numbers:
    password += random.choice(numbers)

print(f"Your easy password is {password}")


#hard password
password_list = []
for char in len_letters:
    password_list += random.choice(letters)

for char in len_symbols:
    password_list += random.choice(symbols)

for char in len_numbers:
    password_list += random.choice(numbers)

random.shuffle(password_list)
#print(password_list)

password = ""
for char in password_list:
    password += char
print(f"\nYour hard password is {password}")

input()
