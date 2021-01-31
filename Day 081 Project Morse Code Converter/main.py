# Morse code dictionary to convert Letters and numbers into morse code format
morse_code_dict = {
    "A": '.-',
    "B": '-...',
    "C": '-.-.',
    "D": '-..',
    "E": '.',
    "F": '..-.',
    "G": '--.',
    "H": '....',
    "I": '..',
    "J": '.---',
    "K": '-.-.',
    "L": '.-..',
    "M": '--',
    "N": '-.',
    "O": '---',
    "P": '.--.',
    "Q": '--.-',
    "R": '.-.',
    "S": '...',
    "T": '-',
    "U": '..-',
    "V": '...-',
    "W": '.--',
    "X": '-..-',
    "Y": '-.--',
    "Z": '--..',
    "1": '.----',
    "2": '..---',
    "3": '...--',
    "4": '....-',
    "5": '.....',
    "6": '-....',
    "7": '--...',
    "8": '---..',
    "9": '----.',
    "0": '-----',
    # Ignore white spaces as it will be handle inside the for loop
    ' ': '',
}

# User text input
text_input = input("Please write the text to be converted to morse code:\n")

# Create list by taking all characters from text input in upper case to match morse_code_dict keys
text_to_convert = [char for char in text_input.upper()]

# morse text converted and code output
morse_text = ''
# Variable to help check if char is the last character in order to avoid including space in the end of morse_text
cont_last_char = 1
for char in text_to_convert:
    morse_text += (morse_code_dict[char])
    # If not last character on the list include white space between letters and "/ " between words
    if cont_last_char != len(text_to_convert):
        if char == ' ':
            morse_text += '/ '
        else:
            morse_text += ' '
    cont_last_char += 1
print(f"The converted text in morse code is:\n{morse_text}")
