from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_numbers + password_letters + password_symbols

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password):
        messagebox.showinfo(title="Oh no", message="Make sure, that you haven't left any fields empty'")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are detail entered:\n\n Email: {username}\n Password: {password}\n\nSave?")
        if is_ok:
            with open("my_passwords.txt", "a") as file:
                file.write(f"{website} | {username} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=20)
canvas = Canvas(width=200, height=200)
locker_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=locker_image)
canvas.grid(row=1, column=1)

website_label = Label(text="Website:").grid(row=2, column=0)
website_entry = Entry(width=35)
website_entry.grid(row=2, column=1, columnspan=2)

username_label = Label(text="Username/Email:").grid(row=3, column=0)
username_entry = Entry(width=35)
username_entry.grid(row=3, column=1, columnspan=2)

password_label = Label(text="Password:", )
password_label.grid(row=4, column=0)

password_entry = Entry(width=22)
password_entry.grid(row=4, column=1)

username_entry.insert(0, "sloneczny4")

generate_button = Button(text="Generate", command=generate_password).grid(row=4, column=2)

add_button = Button(text="Add", width=36, command=save_data).grid(row=5, column=1, columnspan=2)

window.mainloop()
