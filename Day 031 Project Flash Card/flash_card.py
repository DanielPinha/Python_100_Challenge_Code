import tkinter
import pandas
import random
from tkinter import messagebox
# ---------------------------- Set Constants ---------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
# ---------------------------- Set Variables ---------------------------- #
current_card = {}
# ---------------------------- Manage data file ---------------------------- #

try:
    word_data = pandas.read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    word_data = pandas.read_csv('./data/french_words.csv')
finally:
    to_learn = word_data.to_dict(orient="records")

# ---------------------------- User Input Handler ---------------------------- #


def next_card():
    global current_card, to_learn, word_data

    canvas.itemconfig(lang_label, text='French', fill='black')
    canvas.itemconfig(canvas_image, image=card_front)
    try:
        current_card = random.choice(to_learn)
    except IndexError:
        messagebox.showinfo(title='Flash Card', message='You completed all flash cards, restarting list')
        word_data = pandas.read_csv('./data/french_words.csv')
        to_learn = word_data.to_dict(orient="records")
        current_card = random.choice(to_learn)
    canvas.itemconfig(word_label, text=current_card['French'], fill='black')
    flip_timer = window.after(3000, flip_card)


def right_action():
    global current_card

    to_learn.remove(current_card)
    to_learn_csv = pandas.DataFrame(pandas.DataFrame.from_records(to_learn))
    to_learn_csv.to_csv("./data/words_to_learn.csv", index=False)

    next_card()


# ---------------------------- Flip Card ---------------------------- #


def flip_card():
    global current_card
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(lang_label, text='English', fill='white')
    english_word = current_card['English']
    canvas.itemconfig(word_label, text=english_word, fill='white')


# ---------------------------- UI Setup ---------------------------- #
# ----------- Create Window ----------- #
window = tkinter.Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# ----------- Load Image ----------- #
card_front = tkinter.PhotoImage(file="./images/card_front.png")
card_back = tkinter.PhotoImage(file="./images/card_back.png")
right_image = tkinter.PhotoImage(file="./images/right.png")
wrong_image = tkinter.PhotoImage(file="./images/wrong.png")

# ----------- Create flash card ----------- #
canvas = tkinter.Canvas(width=800, height=526)
canvas_image = canvas.create_image(400, 263, image=card_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
lang_label = canvas.create_text(400, 150, text='', font=("Ariel", 40, "italic"))
word_label = canvas.create_text(400, 263, text='', font=("Ariel", 60, "bold"))

# ----------- Create buttons----------- #
wrong_button = tkinter.Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_button = tkinter.Button(image=right_image, highlightthickness=0, command=right_action)
right_button.grid(row=1, column=1)


# ---------------------------- Initialize ---------------------------- #
next_card()
window.mainloop()
