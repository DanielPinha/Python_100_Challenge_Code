# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Get total length of each list to be used in the password generator
length_letters = len(letters)
length_numbers = len(numbers)
length_symbols = len(symbols)

# Generates a weak password with predetermined order: letters, symbols and numbers
weak_password = ""
# Looping from 1 until number requested by user (adding + 1 due to exclusive stop)
for number_letters in range(1, nr_letters + 1):
    # adding random char inside the list into password
    # The same could be achieved with random.choice(letters)
    weak_password += letters[random.randint(0, length_letters - 1)]

for number_symbols in range(1, nr_symbols + 1):
    weak_password += symbols[random.randint(0, length_symbols - 1)]

for number_number in range(1, nr_numbers + 1):
    weak_password += numbers[random.randint(0, length_numbers - 1)]

print(f"The weak password is {weak_password}")

# Generates a strong password with random order for letters, numbers and symbols
# Convert into list in order to use random.shuffle
strong_password_list = list(weak_password)
# it will shuffle each char inside the list
random.shuffle(strong_password_list)
# between each char inside strong_password_list will add ''(in front of .join) to form a string
strong_password = ''.join(strong_password_list)

print(f"The strong password is {strong_password}")
