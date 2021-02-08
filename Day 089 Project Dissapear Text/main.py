from tkinter import Label, END, Tk, Entry


def clear_entry():
    entry.delete("0", END)


def click(key):
    global timer
    if timer:
        window.after_cancel(timer)
    timer = window.after(5000, clear_entry)


timer = None

window = Tk()
window.title("Typing Disappear Text")

instruction_text = Label(text="Text disappear in 5 seconds if typing stops")
instruction_text.grid()
entry = Entry(width=200)
entry.grid()
# Bind entry to any keypress
entry.bind("<Key>", click)

window.mainloop()
