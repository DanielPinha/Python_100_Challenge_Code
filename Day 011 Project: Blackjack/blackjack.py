import blackjack_artwork
import random
import os


def clear():
    """Clear the screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def draw_card(card_list):
    """It will return a random pick from list passed as argument"""
    return random.choice(card_list)


def hand_sum_calculator(hand):
    """It will receive a hand (list) and it will check for blackjack, and in case of a bust it  will evaluate if a Ace
    is present, finally it will return the sum of all cards (items)"""
    if sum(hand) == 21 and len(hand) == 2:
        return 0
    if sum(hand) > 21 and 11 in hand:
        hand[hand.index(11)] = 1
    return sum(hand)


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

match_request = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if match_request == 'y':
    should_continue = True
else:
    should_continue = False

while should_continue:
    # Print blackjack logo artwork
    print(blackjack_artwork.logo)

    # Declares empty player hand and dealer hand
    player_hand = []
    dealer_hand = []

    # Player draw two cards and calculate sum
    player_hand.append(draw_card(cards))
    player_hand.append(draw_card(cards))
    player_hand_sum = hand_sum_calculator(player_hand)

    # Dealer draw two cards and calculate sum
    dealer_hand.append(draw_card(cards))
    dealer_hand.append(draw_card(cards))
    dealer_hand_sum = hand_sum_calculator(dealer_hand)

    # In case of a Blackjack, it will evaluate the winner
    if player_hand_sum == 0 or dealer_hand_sum == 0:
        print(f"    Your final hand: {player_hand}, final score: {player_hand_sum}")
        print(f"    The dealer final card: {dealer_hand}, final score: {dealer_hand_sum}")
        if player_hand_sum == 0 and dealer_hand_sum == 0:
            print("Player and Dealer got a Blackjack! It is a tie")
        elif player_hand_sum == 0:
            print("Player got a Blackjack! Player Won!")
        else:
            print("Dealer got a Blackjack! Player Lose!")
    # Neither Player or Dealer got a blackjack
    else:
        print(f"    Your hand: {player_hand}, current score: {player_hand_sum}")
        print(f"    The dealer first card: {dealer_hand[0]}")
        # Check if Player wants to draw an additional card
        next_draw = input("Type 'y' to get another card, type 'n' to pass:")
        while next_draw == 'y':
            # Player draw one card and recalculate sum
            player_hand.append(draw_card(cards))
            player_hand_sum = hand_sum_calculator(player_hand)

            # If player busts stop asking to player if wants to draw
            if player_hand_sum > 21:
                next_draw = 'n'
            else:
                print(f"    Your hand: {player_hand}, current score: {player_hand_sum}")
                print(f"    The dealer first card: {dealer_hand[0]}")
                next_draw = input("Type 'y' to get another card, type 'n' to pass:")

        # In case of player busts, resolution of game
        if player_hand_sum > 21:
            print(f"    Your final hand: {player_hand}, final score: {player_hand_sum}")
            print(f"    The dealer final card: {dealer_hand}, final score: {dealer_hand_sum}")
            print("You went over, you lose!")
        else:
            # Dealer will draw cards until it ties with player or busts
            while dealer_hand_sum < player_hand_sum and dealer_hand_sum <= 21:
                dealer_hand.append(draw_card(cards))
                dealer_hand_sum = hand_sum_calculator(dealer_hand)
            print(f"    Your final hand: {player_hand}, final score: {player_hand_sum}")
            print(f"    The dealer final card: {dealer_hand}, final score: {dealer_hand_sum}")
            # in case dealer busts
            if dealer_hand_sum > 21:
                print("Dealer went over, You Win!")
            # Resolution of the game in case neither player or dealer busts
            else:
                if player_hand_sum > dealer_hand_sum:
                    print("You Win!")
                elif player_hand_sum == dealer_hand_sum:
                    print("It is a draw!")
                else:
                    print("You Lose!")

    # Request if user wants to play a new match
    match_request = input("Do you want to play another game of Blackjack? Type 'y' or 'n': ")
    if match_request == 'y':
        should_continue = True
        clear()
    else:
        should_continue = False
