from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_symbols = [random.choice(numbers) for sym in range(nr_symbols)]
    password_numbers = [random.choice(symbols) for num in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)


    password = "".join(password_list)

    password_.insert(0,f"{password}")
    # print(f"Your password is: {password}")
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():


    website_input = website_.get()
    email_input = email_.get()
    password_input = password_.get()
    new_data = {
        website_input: {
            "email": email_input,
            "password": password_input,
        }
    }

    if len(website_input) == 0 or len(password_input) == 0:
        messagebox.showinfo(title = "Error",message="Please make sure you have not left anything empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                #read and update the data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            website_.delete(0, END)
            password_.delete(0, END)



def find_password():
    website_input = website_.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title = "Error", message = "No record found" )
    else:
        if website_input in data:
            email = data[website_input]["email"]
            password = data[website_input]["password"]
            messagebox.showinfo(title=website_input, message=f"Email: {email}\n, Password: {password}")

        else:
            messagebox.showinfo(title = "error", message = "No details found")
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password")
window.config(padx=50, pady=40, bg="white")

canvas = Canvas(width=250, height=270, bg="purple")
image = PhotoImage(file="new_logo.png")
canvas.create_image(126, 130, image=image)
canvas.grid(column=2, row=1)

# ------------------Labels---------------------------
website = Label(text="Website:")
website.grid(column=1, row=2)
email = Label(text="Email/Username:")
email.grid(column=1, row=3)
password = Label(text="Password:")
password.grid(column=1, row=4)

# ------------------Entry---------------------------
website_ = Entry(width=35)
website_.grid(column=2, row=2, columnspan=2)
website_.focus()
website_input = website_.get()

email_ = Entry(width =35)
email_.grid(column=2, row=3, columnspan=2 )
email_.insert(0, "abcd@gmail.com")
password_ = Entry(width =21)
password_.grid(column=2, row=4)


# ------------------Button---------------------------
generate = Button(text="Generate Password", command = generate_password)
generate.grid(column=3, row= 4)

add= Button(text= "Add", command = save_password)
add.grid(column = 2, row = 5, columnspan=2)

search = Button(text = "Search", command = find_password)
search.grid(column= 3, row=2, columnspan=2)

window.mainloop()
