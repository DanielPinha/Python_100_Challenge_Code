import random
from number_guessing_artwork import logo
print(logo)
print("Welcome to the Number Guessing Game")

guess_number = random.randint(1, 100)
print("I'm thinking of a number between 1 to 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == 'easy':
    attempts = 10
else:
    attempts = 5

while attempts:
    print(f"You have {attempts} attempts remaining to guess the number.")
    try:
        user_guess = int(input("Make a guess: "))
    except ValueError:
        print("Invalid input! Considering player guess as 0")
        user_guess = 0
    if guess_number > user_guess:
        print("Too low")
        attempts -= 1
    elif guess_number < user_guess:
        print("Too High")
        attempts -= 1
    else:
        print(f"You got it! The answer was {guess_number}.")
        attempts = 0

if user_guess != guess_number:
    print("You run out of attempts, you lost!")
