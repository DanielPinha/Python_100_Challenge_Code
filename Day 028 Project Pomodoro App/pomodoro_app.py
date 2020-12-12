import tkinter
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
# ---------------------------- VARIABLES ------------------------------- #
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps, timer
    reps = 0
    window.after_cancel(timer)

    action_label.config(text='Timer', fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    pomodoro_label.config(text='')

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    reps += 1
    if reps % 2 == 1:
        # pomodoro_label.config(text=f"")
        count_down(work_sec)
        action_label.config(text='Work', fg=GREEN)
    elif reps % 8 == 0:
        count_down(long_break_sec)
        action_label.config(text='Break', fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        action_label.config(text='Break', fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global reps, timer
    count_min = math.floor(count / 60)
    count_sec = (count % 60)
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    count_format = f"{count_min}:{count_sec}"
    
    canvas.itemconfig(timer_text, text=count_format)
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        checks = '✔' * int(reps / 2)
        pomodoro_label.config(text=checks)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

action_label = tkinter.Label(text='Timer', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40))
action_label.grid(row=0, column=1)

pomodoro_label = tkinter.Label(bg=YELLOW, fg=GREEN)
pomodoro_label.grid(row=3, column=1)

start_button = tkinter.Button(text='Start', command=start_timer)
start_button.grid(row=2, column=0)

reset_button = tkinter.Button(text='Reset', command=reset_timer)
reset_button.grid(row=2, column=2)

window.mainloop()
