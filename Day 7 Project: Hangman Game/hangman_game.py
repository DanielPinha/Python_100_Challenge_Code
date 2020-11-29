import random
from hangman_word import word_list
from hangman_art import stages, logo

# TODO-1.1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)

print(logo)
# TODO-2.1: - Create an empty List called display.
chosen_word_length = len(chosen_word)
display_word = '_'*chosen_word_length

# TODO-4.1: - Create a variable called 'lives' to keep track of the number of lives left.
player_lives = 6
# TODO-1.2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# TODO-3.1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the
#             letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
end_of_game = False
print(stages[player_lives])
print(display_word)
guessed_letters = []
while not end_of_game:
    guess = (input("Please guess a letter: ")).lower()

    if guess in guessed_letters:
        print("You already guessed this letter")
    else:
        guessed_letters.append(guess)
        # TODO-1.3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
        # TODO-2.2: - If the letter at that position matches 'guess' then reveal that letter in the display at
        #             that position.
        for char_position in range(chosen_word_length):
            if guess == chosen_word[char_position]:
                display_word = display_word[:char_position] + guess + display_word[char_position + 1:]
        # TODO-4.2: - If guess is not a letter in the chosen_word, Then reduce 'lives' by 1.
        if guess not in chosen_word:
            print(f"the letter '{guess}' is not part of the word")
            player_lives -= 1
            if player_lives == 0:
                end_of_game = True
                print("You Lose!")

        if "_" not in display_word:
            end_of_game = True
            print("You Win!")
    # TODO-2.3: - Print 'display' and the guessed letter must  be in the correct position and other letter with "_".
    print(stages[player_lives])
    print(f"Guessed letters so far: {guessed_letters}")
    print(display_word)
