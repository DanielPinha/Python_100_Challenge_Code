import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# Get user choice and convert into integer
user_hand = int(input("What do you choose? type 0 for rock, 1 for paper and 2 for scissors\n"))

if user_hand == 0 or user_hand == 1 or user_hand == 2:
    # Create list to facilitate print of hands
    hand_emoji = [rock, paper, scissors]

    # Use pseudo random generator integer and value 0 = rock, 1 = paper and 2 = scissors
    computer_hand = random.randint(0, 2)

    # Print user hand, and computer random choice
    print(hand_emoji[user_hand])
    print("Computer chose:")
    print(hand_emoji[computer_hand])

    # Define winner, exception to rule are both extremes user = rock and computer = scissor and vice-versa
    if user_hand == 0 and computer_hand == 2:
        print("You win!")
    elif user_hand == 2 and computer_hand == 0:
        print("You lose!")
    elif user_hand < computer_hand:
        print("You lose!")
    elif user_hand == computer_hand:
        print("It is a draw!")
    else:
        print("You win!")
else:
    print("You are not dexterous enough to do anything other than rock, paper and scissors. You lose!")
