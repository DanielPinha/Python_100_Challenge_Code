import caesar_cipher_art


def caesar(user_text, shift_amount, action):
    output_text = ''
    # in case of decode the shift must be to the left hence multiplied by -1
    if action == 'decode':
        shift_amount *= -1
    for letter in user_text:
        try:
            index_position = alphabet.index(letter)
        except ValueError:
            output_text += letter
        else:
            # cipher formula, shifts letters from alphabet by a certain amount specified by user
            index_shift = index_position + shift_amount
            # In case larger shift than alphabet length. the remainder will always be the final position
            index_shift = index_shift % len(alphabet)
            output_text += alphabet[index_shift]
    if action == 'encode' or action == 'decode':
        print(f"The {action}d message is {output_text}")
    else:
        print("Command not accepted. Please when prompted type 'encode' to encrypt or type 'decode' to decrypt")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

# Print caesar logo
print(caesar_cipher_art.logo)

# loop in case user wants to continue after each run or exit
is_user_operating = True
while is_user_operating:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()

    try:
        shift = int(input("Type the shift number:\n"))
    except ValueError:
        print("Please type a integer number for shift when prompted")
    else:
        caesar(text, shift, direction)

    # Evaluate if user wants to continue after each run or exit
    user_replay_feedback = input("type 'yes' to go again or type 'no' to finalize the program\n")
    if user_replay_feedback == 'yes':
        is_user_operating = True
    elif user_replay_feedback == 'no':
        is_user_operating = False
    else:
        print("Invalid Command. Program will exit")
        is_user_operating = False
