from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# created a list so the program can access any character they want
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
               'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
               'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # initializes the password variable to accumulate the data from the for loops below
    password = ""

    # used a for loop to allow the computer to randomly select a user specified amount of characters
    for letter in range(0, 5):
        password += random.choice(letters)

    for letter in range(0, 2):
        password += random.choice(symbols)

    for letter in range(0, 2):
        password += random.choice(numbers)

    # used the list function to turn each character of the string into an array(list)
    password = list(password)

    # used the shuffle function to shuffle the array
    random.shuffle(password)

    # used the join function to rejoin the list
    password = ''.join(password)

    # displays the password to the user
    password_entry.insert(0, password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    # this fetches the user's entry and stores it into these files
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # if the user is not satisfied with their entry then it will not save.
    # If they are then it will tell them their data had been saved.

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Error", message="You've left a field empty.")
    else:
        # this asks the user a prompt
        is_ok = messagebox.askokcancel(message="Are you sure your information is correct?")

        # this chunk of code retains then user's information if they're not happy with their initial input
        if is_ok:
            with open("password_data.txt", "a") as data_file:
                data_file.write(f"\n---------\nWebsite: {website}\nEmail: {email}\nPassword: {password}")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
            # this informs the user that everything went smoothly
            messagebox.showinfo(message="Your information has been saved!")


#  ---------------------------- UI SETUP ------------------------------- #
# sets up the window
window = Tk()

window.title("Password Manager")

window.config(padx=20, pady=50)

# adds a canvas
canvas = Canvas(width=200, height=189, highlightthickness=0)

canvas.grid(row=0, column=1)

# adds a lock image onto the canvas
lock = PhotoImage(file="logo.png")

lock_img = canvas.create_image(100, 95, image=lock)

# __________________

# adds a website label
website_label = Label(text="Website:", fg="black")

website_label.grid(row=1, column=0)

# adds a email/username label
email_label = Label(text="Email/Username:", fg="black")

email_label.grid(row=2, column=0)

# adds a password label
password_label = Label(text="Password:", fg="black")

password_label.grid(row=3, column=0)

# ______________

# adds the website label corresponding entry box
website_entry = Entry(width=35)

website_entry.grid(row=1, column=1, columnspan=3, sticky="EW")

# makes the cursor focus on this entry box on start up
website_entry.focus()

# adds the email/username label corresponding entry box
email_entry = Entry(width=35)

email_entry.insert(0, "sample@email.com")
email_entry.grid(row=2, column=1, columnspan=3, sticky="EW")

# adds the password label corresponding entry box
password_entry = Entry(width=33)

password_entry.grid(row=3, column=1)

# ______________

# adds a "generate password" button
password_button = Button(text="Generate Password", fg="Black", command=password_generator)

password_button.grid(row=3, column=2)

# adds the "Add" button

add_button = Button(text="Add", fg="Black", width=35, command=save)

add_button.grid(row=4, column=1, columnspan=3, sticky="EW")

window.mainloop()
