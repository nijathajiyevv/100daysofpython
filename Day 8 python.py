# def greet():
#     print("Hello")
#     print("How are you?")

# Function that allows for input
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How are you doing {name}?")
# greet_with_name("John")

# Function with more than 1 input
# def greet_wth_name_age(name, location):
#     print(f"Hello {name}, are you in {location} ?")
# greet_wth_name_age("John", "New York")


#Write your code below this line 👇
# def paint_calc(height, width, cover):
#     num_of_cans = round((height * width) / cover)
#     print(f"You'll need {num_of_cans} cans of paint")
#
# #Write your code above this line 👆
# # Define a function called paint_calc() so that the code below works.
#
# # 🚨 Don't change the code below 👇
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)


#Write your code below this line 👇
# def prime_checker(number):
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#     if is_prime:
#         print("It's a prime number.")
#     else:
#         print("It's not a prime number.")
#
# #Write your code above this line 👆
#
# #Do NOT change any of the code below👇
# n = int(input("Check this number: "))
# prime_checker(number=n)

# Caesar Cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type *encode* to encrypt, type *decode* to decrypt: \n")
if direction != "encode" and direction != "decode":
    print("Wrong input. Please use ONLY encode OR decode")
    exit()

text = input("Type your message: \n").lower()

shift = int(input("Type the shift number: \n"))
if shift == 0:
    print("You can't shift by 0")
    exit()
elif shift < 0:
    shift = -1 * shift
    print("You shifted by a negative number")
    print("It's now positive")


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    print(f"The {cipher_direction}d text is: {end_text}")
    again = input("Do you want to go again? Type *yes* or *no*. \n")
    if again == "yes":
        direction = input("Type *encode* to encrypt, type *decode* to decrypt: \n")
        # depeding on the direction, encode or decode inputted text
        text = input("Type your message: \n").lower()
        shift = int(input("Type the shift number: \n"))
        caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    elif again == "no":
        print("Goodbye")
        exit()
    elif again !="yes" or again!="no":
        print("Wrong input. Please use ONLY yes or no")
        exit()

# Separate version
# def encrypt(encrypt_text, shift_amount):
#     new_text = ""
#     for letter in encrypt_text:
#         if letter in alphabet:
#             new_index = alphabet.index(letter) + shift_amount
#             new_text += alphabet[new_index]
#     print(f"The encrypted message is: {new_text}")
#
# def decrypt(decrypt_text, shift_amount):
#     new_text2 = ""
#     for letter in decrypt_text:
#         if letter in alphabet:
#             new_index = alphabet.index(letter) - shift_amount
#             new_text2 += alphabet[new_index]
#     print(f"The decrypted message is: {new_text2}")
#
# if direction == "encode":
#     encrypt(encrypt_text=text, shift_amount=shift)
# elif direction == "decode":
#     decrypt(decrypt_text=text, shift_amount=shift)
# else:
#     print("Wrong input")
#     exit()
if shift > len(alphabet):
    shift = shift % len(alphabet)

caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
