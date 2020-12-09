with open("./Input/Names/invited_names.txt") as invited:
    names = invited.read().splitlines()

with open("./Input/Letters/starting_letter.docx") as base_letter:
    letter = base_letter.read()

for name in names:
    new_letter = letter.replace('[name]', name)
    with open(f"./Output/ReadyToSend/letter_for_{name}.docx", mode='w') as final_letter:
        final_letter.write(new_letter)
