from artwork import logo
theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}


def print_board(board):
    """
    Print the Tic Tac Toe board in the console

    :param board: dictionary representing Tic Tac Toe board
    :return: None
    """
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


def player_has_won(board):
    """
    Check if player has won in any allowed combination of Tic Tac Toe

    :param board: dictionary representing Tic Tac Toe board
    :return: True if player has won and False if player did not managed to win
    """
    if board['7'] == board['8'] == board['9'] != ' ':  # across the top
        return True
    elif board['4'] == board['5'] == board['6'] != ' ':  # across the middle
        return True
    elif board['1'] == board['2'] == board['3'] != ' ':  # across the bottom
        return True
    elif board['1'] == board['4'] == board['7'] != ' ':  # down the left side
        return True
    elif board['2'] == board['5'] == board['8'] != ' ':  # down the middle
        return True
    elif board['3'] == board['6'] == board['9'] != ' ':  # down the right side
        return True
    elif board['7'] == board['5'] == board['3'] != ' ':  # diagonal
        return True
    elif board['1'] == board['5'] == board['9'] != ' ':  # diagonal
        return True
    else:
        return False


# Show logo and input rules
print(logo)
print("The fields options follow the num keypad order 789 (top line), 456 (second line) and 123 (bottom line)")

game_is_on = True
while game_is_on:
    # Print the board
    print_board(theBoard)

    # Get Player 1 input
    player1_choice_complete = False
    while not player1_choice_complete:
        player_choice = input("Player 1 (X) Please select a empty field: ")
        # Handle invalid input scenario
        try:
            # Evaluate if player input is an empty field
            if theBoard[player_choice] == ' ':
                theBoard[player_choice] = 'X'
                player1_choice_complete = True
            else:
                print("Field already taken, please choose another when prompt!")
                player1_choice_complete = False
        except KeyError:
            print("Invalid input, allowed inputs are: 789 (top line), 456 (second line) and 123 (bottom line)")
            player1_choice_complete = False

    # Print the board
    print_board(theBoard)

    # Check if Player 1 won
    if player_has_won(theBoard):
        print("\nGame Over.\n")
        print(f"Player 1 (X) won.")
        game_is_on = False
        break

    # Check if all fields are completed if so it is a tie.
    if ' ' not in theBoard.values():
        game_is_on = False
        print("\nGame Over.\n")
        print("It is a tie")
        break

    # Get Player 2 input
    player2_choice_complete = False
    while not player2_choice_complete:
        player_choice = input("Player 2 (O) Please select a empty field: ")
        # Handle invalid input scenario
        try:
            # Evaluate if player input is an empty field
            if theBoard[player_choice] == ' ':
                theBoard[player_choice] = 'O'
                player2_choice_complete = True
            else:
                print("Field already taken, please choose another when prompt!")
                player2_choice_complete = False
        except KeyError:
            print("Invalid input, allowed inputs are: 789 (top line), 456 (second line) and 123 (bottom line)")
            player2_choice_complete = False

    # Check if Player 2 won
    if player_has_won(theBoard):
        print("\nGame Over.\n")
        print(f"Player 2 (O) won.")
        game_is_on = False
        break
