import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

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


def save_data():
    website = website_entry.get().upper()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "email": username,
        "password": password,
    }
    }

    if len(website) == 0 or len(password)==0:
        messagebox.showinfo(title="Oh no", message="Make sure, that you haven't left any fields empty'")
    else:
        try:
            with open("my_passwords.json", "r") as file:
                data = json.load(file)

        except FileNotFoundError:
            with open("my_passwords.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("my_passwords.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


""" SEARCH PASSWORD"""
def find_password():
    website = website_entry.get().upper()
    try:
        with open("my_passwords.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oh no", message="There is no password file found")
    else:
        if website in data:
            new_data = data.get(website)
            messagebox.showinfo(title=website, message=f"Username: {new_data['email']}\nPassowrd: {new_data['password']}")
        else:
            messagebox.showinfo(title="Oh no", message=f"There is no data for {website")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=20)
canvas = Canvas(width=200, height=200)
locker_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=locker_image)
canvas.grid(row=1, column=1)

website_label = Label(text="Website:").grid(row=2, column=0)
website_entry = Entry(width=22)
website_entry.grid(row=2, column=1)

search_button = Button(text="Search", command=find_password).grid(row=2, column=2)

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
