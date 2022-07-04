from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ------------------------------SEARCH FEATURE------------------------------------#
def search():
    # gets the user's entry in the website box
    website = website_entry.get()

    # opens the JSON data file
    with open("password_data.json", "r") as data_file:
        # reads the file and stores the data into a variable
        value = json.load(data_file)

        # searches for the user's entry inside the JSON database
        if website in value:
            # searches for and assigns the user's information into it's respective variable
            website_username = value[website]["email"]
            website_password = value[website]["password"]
            # prompts the user their information in a clean easy to read way
            messagebox.showinfo(title="User Information",
                                message=f"Username: {website_username}\n Password: {website_password}")
        else:
            # if the requested website's information isn't available the program tells the user
            messagebox.showinfo(message="The information for this website is not in record")


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
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    # if the user is not satisfied with their entry then it will not save.
    # If they are then it will tell them their data had been saved.

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Error", message="You've left a field empty.")
    else:
        # this asks the user a prompt
        is_ok = messagebox.askokcancel(message="Are you sure your information is correct?")

        # this chunk of code retains then user's information if they're not happy with their initial input
        if is_ok:
            try:
                with open("password_data.json", "r") as data_file:

                    # Reading the old data
                    data = json.load(data_file)
                    # Updating old data with new data

            except FileNotFoundError:
                with open("password_data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)

            else:
                data.update(new_data)

                with open("password_data.json", "w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)

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
website_entry = Entry(width=33)

website_entry.grid(row=1, column=1)

# makes the cursor focus on this entry box on start up
website_entry.focus()

# adds the email/username label corresponding entry box
email_entry = Entry(width=33)

email_entry.insert(0, "sample@email.com")

email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")

# adds the password label corresponding entry box
password_entry = Entry(width=33)

password_entry.grid(row=3, column=1)

# ______________

# adds a "generate password" button and assign's the function password_generator() to it
password_button = Button(text="Generate Password", fg="Black", command=password_generator)

password_button.grid(row=3, column=2)

# adds a "search" button and assign's the function search() to it
search_button = Button(text="Search", fg="Black", command=search)

search_button.grid(row=1, column=2, sticky=EW)

# adds the "Add" button

add_button = Button(text="Add", fg="Black", width=35, command=save)

add_button.grid(row=4, column=1, columnspan=3, sticky="EW")

window.mainloop()
