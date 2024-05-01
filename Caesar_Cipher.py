print("Caesar Cipher\n")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    
    print(f"Here's the {cipher_direction}d result: {end_text}")

start_over = True
while start_over:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 25

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    go_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if go_again == 'no':
        start_over = False
        print("Goodbye")

input()

# def caesar(plain_text, shift_amount, direction):
#     encode = ""
#     decode = ""
#     for char in plain_text:
#         if char in alphabet:
#             position = alphabet.index(char)
#             encrypt = position + shift_amount
#             decrypt = position - shift_amount
#             encode = encode + alphabet[encrypt]
#             decode = decode + alphabet[decrypt]
#         else:
#             encode += char
#             decode += char
#     if direction == "encode":
#         print(f"The encoded text is {encode}")
#     elif direction == "decode":
#         print(f"The decoded text is {decode}")
# caesar(plain_text=text, shift_amount=shift, direction=direction)

#def encrypt(plain_text, shift_amount):
#  cipher_text = ""
#  for letter in plain_text:
 #        position = alphabet.index(letter)
#        new_position = position + shift_amount
#        new_letter = alphabet[new_position]
#        cipher_text += new_letter
#    print(f"The encoded text is {cipher_text}")

#def decrypt(plain_text, new_shift_amount):
#    cipher_text = ""    
#    for letter in plain_text:
#        decrypt_position = alphabet.index(letter)
#        new_decrypt_position = decrypt_position - new_shift_amount
#        new_decrypt_letter = alphabet[new_decrypt_position]
#        cipher_text += new_decrypt_letter
#    print(f"The decoded text is {cipher_text}")

#if direction == "encode":
#    encrypt(plain_text=text, shift_amount=shift)
#elif direction == "decode":
#    decrypt(plain_text=text, new_shift_amount=shift)
