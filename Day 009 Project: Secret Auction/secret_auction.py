import secret_auction_artwork
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# Show auction logo
print(secret_auction_artwork.logo)

# Create dictionary to store name and bid values of bidders
bidder_dict = {}

# Item to be bidden
print("Today bidding item is a lovely pair of snickers")

# Variable to check if there will be a new bidder
is_new_bidder = True
while is_new_bidder:
    new_bidder_name = input("Please inform your name\n")
    # It will evaluate if the name already exist in the dictionary to avoid overwriting previous bid
    is_name_taken = True
    while is_name_taken:
        if new_bidder_name in bidder_dict:
            new_bidder_name = input("Name already taken, to avoid biding issues please state an new name\n")
        else:
            is_name_taken = False

    # It will confirm that the value inputted is an acceptable value
    bid_value_correct = False
    while not bid_value_correct:
        try:
            new_bidder_value = float(input("Please inform the amount you wish to bid: $"))
        except ValueError:
            print("The input is not valid, please retry")
        else:
            bid_value_correct = True

    # Adding bidder information into dictionary
    bidder_dict[new_bidder_name] = new_bidder_value

    check_new_bidder = input("Is there an additional bidder? type 'yes' or 'no'\n").lower()
    if check_new_bidder == "yes":
        is_new_bidder = True
    elif check_new_bidder == "no":
        is_new_bidder = False
    else:
        print("Invalid input, going to counting the bids")
        is_new_bidder = False

    # Function to clear console for new bidder
    clear()

# It will evaluate the highest bid and store it
winner_name = ''
winner_bid = 0
for bidder_name in bidder_dict:
    if bidder_dict[bidder_name] > winner_bid:
        winner_name = bidder_name
        winner_bid = bidder_dict[bidder_name]

print(f"The winner is {winner_name} and the bid amount is ${winner_bid}")
print(f"Please enjoy your lovely pair of sneakers\n{secret_auction_artwork.sneaker}")
