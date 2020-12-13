import tkinter
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = 8
nr_symbols = 2
nr_numbers = 3

# Get total length of each list to be used in the password generator
length_letters = len(letters)
length_numbers = len(numbers)
length_symbols = len(symbols)


def generate_password():
    # Generates a weak password with predetermined order: letters, symbols and numbers
    # Looping from 1 until number of letters (adding + 1 due to exclusive stop)
    weak_password = [random.choice(letters) for _ in range(1, nr_letters + 1)]
    weak_password += [random.choice(symbols) for _ in range(1, nr_symbols + 1)]
    weak_password += [random.choice(numbers) for _ in range(1, nr_numbers + 1)]

    # Generates a strong password with random order for letters, numbers and symbols
    # Convert into list in order to use random.shuffle
    strong_password_list = list(weak_password)
    # it will shuffle each char inside the list
    random.shuffle(strong_password_list)
    # between each char inside strong_password_list will add ''(in front of .join) to form a string
    strong_password = ''.join(strong_password_list)

    # Clear password entry field and insert strong password calculated
    password_input.delete(0, tkinter.END)
    password_input.insert(0, strong_password)
    pyperclip.copy(strong_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_action():
    website = website_input.get().title()
    email = email_input.get()
    password = password_input.get()

    new_data = {
        website: {'email': email,
                  'password': password,
                  }
    }

    # Check if either field is blank
    if website == '' or email == '' or password == '':
        messagebox.showerror(title='Password Manager', message='Please fill all fields prior to adding to file')
    else:
        user_confirmed = messagebox.askokcancel(title=website, message=f"Please confirm the information below\n"
                                                                       f"Email: {email}\nPassword: {password}")
        if user_confirmed:
            try:
                with open("saved_password.json", mode='r') as file:
                    data = json.load(file)
                    data.update(new_data)
            except FileNotFoundError:
                data = new_data
            finally:
                with open("saved_password.json", mode='w') as file:
                    json.dump(data, file, indent=4)
            messagebox.showinfo(title="Password Manager", message="Information Saved successfully")
            # Clear website and password fields
            website_input.delete(0, tkinter.END)
            password_input.delete(0, tkinter.END)


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_action():
    website = website_input.get().title()
    try:
        with open("saved_password.json", mode='r') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Password Manager", message="Stored password library is empty")
    else:
        if website in data:
            messagebox.showinfo(title="Password Manager", message=f"Found match, loading on screen")

            email_input.delete(0, tkinter.END)
            email_input.insert(0, data[website]['email'])

            password_input.delete(0, tkinter.END)
            password_input.insert(0, data[website]['password'])
        else:
            messagebox.showinfo(title="Password Manager", message=f'{website} data not found in password library')


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=200, height=200)
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# --------- Create Label --------- #
website_label = tkinter.Label(text='Website:')
website_label.grid(row=1, column=0)

email_label = tkinter.Label(text='Email/Username:')
email_label.grid(row=2, column=0)

password_label = tkinter.Label(text='Password:')
password_label.grid(row=3, column=0)

# --------- Create Input box --------- #
website_input = tkinter.Entry()
website_input.grid(row=1, column=1, columnspan=1, sticky="EW")
website_input.focus()

email_input = tkinter.Entry(width=40)
email_input.grid(row=2, column=1, columnspan=2, sticky="EW")
email_input.insert(0, "drjpinha@gmail.com")

password_input = tkinter.Entry(width=21)
password_input.grid(row=3, column=1, sticky="EW")

# --------- Create Buttons --------- #
password_button = tkinter.Button(text='Generate Password', width=14, command=generate_password)
password_button.grid(row=3, column=2, sticky="EW")

add_button = tkinter.Button(text='Add', width=40, command=add_action)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

search_button = tkinter.Button(text='Search', command=search_action)
search_button.grid(row=1, column=2, sticky="EW")

window.mainloop()
