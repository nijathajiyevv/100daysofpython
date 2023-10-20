# number guessing game
import random

def guess_number_game(attempts, number):
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == number:
            print(f"You got it! The answer was {number}.")
            return
        elif guess > number:
            print("Too high.")
        else:
            print("Too low.")
        attempts -= 1
    print(f"You've run out of attempts! The number was {number}.")

difficulty = input("Choose a difficulty (easy/hard): ")

if difficulty == "easy":
    attempts = 10
    number = random.randint(1, 100)
    guess_number_game(attempts, number)
elif difficulty == "hard":
    attempts = 5
    number = random.randint(1, 100)
    guess_number_game(attempts, number)
else:
    print("Invalid difficulty choice.")

