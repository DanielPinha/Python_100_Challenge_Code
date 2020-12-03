import random
import os
import higher_lower_artwork
from higher_lower_database import data


def clear():
    """Clear Screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def pick_random_element(famous_list):
    """Receives list argument and return random element from list"""
    return random.choice(famous_list)


def check_result(comp_a, comp_b, user_choice):
    """Receive Account A and B, and user choice and return True if user correct guess highest follower"""
    if comp_a['follower_count'] > comp_b['follower_count']:
        return user_choice == 'A'
    else:
        return user_choice == 'B'


def format_account_data(account):
    """Return string with formatted data from account dict"""
    return f"{account['name']}, {account['description']}, from {account['country']}"


user_correct = True
user_score = 0
print(higher_lower_artwork.logo)
account_b = pick_random_element(data)
while user_correct:
    account_a = account_b
    account_b = pick_random_element(data)
    # In case Account B is identical to Account A
    while account_b == account_a:
        account_b = pick_random_element(data)

    # Print Account A VS Account B
    print(f"Compare A: {format_account_data(account_a)}")
    print(higher_lower_artwork.vs_art)
    print(f"Against B: {format_account_data(account_b)}")

    # Collect user choice and check result
    user_account_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    user_correct = check_result(account_a, account_b, user_account_choice)

    # Clear screen and print logo
    clear()
    print(higher_lower_artwork.logo)

    # Action depending if user guess it right or wrong
    if user_correct:
        user_score += 1
        print(f"You're right! Current score: {user_score}")
    else:
        print(f"Sorry, that's wrong. Final score: {user_score}")
