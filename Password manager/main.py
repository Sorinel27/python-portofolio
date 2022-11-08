from tkinter import *
from tkinter.messagebox import showinfo
import random
import pyperclip
import json

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def search():
    website = website_input.get()
    with open("data.json", "r") as file:
        data = json.load(file)
        try:
            showinfo(f"{website}", f"Email: {data[website]['email']}\nPassword: {data[website]['password']}")
        except KeyError:
            showinfo("Error", "Wrong website name, check again!")


def add_data():
    new_data = {
        website_input.get(): {
            "email": user_input.get(),
            "password": password_input.get()
        }
    }
    if website_input.get() == "" or user_input.get() == "" or password_input == "":
        showinfo("Oops!", "Please fill all the forms!")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.loads(file.read())
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            password_input.delete(0, END)
            website_input.delete(0, END)
            file.close()


def random_password():
    password_input.delete(0, END)
    generated_password = []
    for i in range(1, 16):
        lns = random.randint(1, 3)
        if lns == 1:
            random.shuffle(letters)
            generated_password.append(letters[0])
        elif lns == 2:
            random.shuffle(numbers)
            generated_password.append(numbers[0])
        elif lns == 3:
            random.shuffle(symbols)
            generated_password.append(symbols[0])
    result = ''.join(generated_password)
    pyperclip.copy(result)
    password_input.insert(0, result)


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=189, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 95, image=lock_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_input = Entry()
website_input.grid(column=1, row=1, sticky=W, ipadx=30, pady=3)

user_input = Entry()
user_input.grid(column=1, row=2, columnspan=2, sticky=W, ipadx=97, pady=3)

password_input = Entry()
password_input.grid(column=1, row=3, sticky=W, ipadx=30, pady=3)

generate_password = Button(text="Generate Password", command=random_password)
generate_password.grid(column=2, row=3, pady=3)

search_button = Button(text="Search", command=search)
search_button.grid(column=2, row=1, sticky=W, ipadx=36, pady=3)

add_button = Button(text="Add", command=add_data)
add_button.grid(column=1, row=4, columnspan=2, sticky=W, ipadx=143, pady=3)
window.mainloop()
