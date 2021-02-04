import tkinter
from tkinter import messagebox, LEFT, DISABLED, NORMAL, END
import time

start_time = 0


def start_submit():
    global start_time
    # Evaluate if button is Start or Submit (represented by else statement)
    if start_submit_button['text'] == 'Start':
        # Allow user typing in the textbox
        text_entry.config(state=NORMAL)
        # Focus on textbox so user will not need to click with mouse
        text_entry.focus()
        # Change button label to Submit
        start_submit_button['text'] = 'Submit'
        # Get system time in seconds at beginning of typing
        start_time = time.time()

    else:
        # Get system time in seconds at end of typing
        final_time = time.time()
        # Get duration time of typing
        typing_time_duration = final_time - start_time

        # Get user input and break word by word
        user_text = text_entry.get("1.0", END).split(' ')
        # Remove '\n' from last word
        user_text[-1] = user_text[-1].split('\n')[0]
        # Get sample text to compare against user input
        sample_text = sample_text_label['text'].split(' ')

        score = 0
        index = 0
        for user_word in user_text:
            if user_word == sample_text[index]:
                score += 1
            index += 1

        # Calculate typing speed in words per min
        typing_speed = round((score / typing_time_duration) * 60)

        messagebox.showinfo(title="Typing Speed Test", message=f"Your typing speed was {typing_speed} words/min")

        # Clear text field
        text_entry.delete("1.0", END)
        # Disable input into the textbox
        text_entry.config(state=DISABLED)
        # Change button label to Start
        start_submit_button['text'] = 'Start'


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Typing Speed Test")
window.config(padx=25, pady=25)

instruction_text = tkinter.Label(justify=LEFT,
                                 text="Please click start and type the sample text shown below."
                                      "\nYou can finish at anypoint by clicking submit."
                                      "\nTyping speed will be calculated based on the numbers of correct words typed.")
instruction_text.grid(row=1, column=1, columnspan=2)

sample_text_label = tkinter.Label(wrap=600, justify=LEFT,
                                  text="Frank Edward McGurrin, a court stenographer from Salt Lake City, Utah who taught typing classes, reportedly invented touch typing in 1888. On a standard keyboard for English speakers the home row keys are: 'ASDF' for the left hand and 'JKL;' for the right hand. The keyboard is called a QWERTY keyboard because these are the first six letters on the keyboard. Most modern computer keyboards have a raised dot or bar on the home keys for the index fingers to help touch typists maintain and rediscover the correct position on the keyboard quickly with no need to look at the keys. More recently, the ability to touch type on touchscreen phones has been made possible with the use of specialized virtual keyboard software for touch typing.")
sample_text_label.grid(row=2, column=1, columnspan=2)

text_entry = tkinter.Text(height=5, state=DISABLED)
text_entry.grid(row=3, column=1, columnspan=2, sticky="EW")

start_submit_button = tkinter.Button(text="Start", command=start_submit)
start_submit_button.grid(row=4, column=2, sticky="EW")

window.mainloop()
