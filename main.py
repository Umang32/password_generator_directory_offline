from tkinter import *
from tkinter import messagebox
import random
import pyperclip
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

    if len(website_input) == 0 or len(password_input) == 0:
        messagebox.showinfo(title = "Please make sure you have not left anything empty")
    else:

        is_okay = messagebox.askokcancel(title=website_input, message=f"These are the details: \n Email = {email_input} \n Password = "
        f"{password_input} \n is it okay?")

        if is_okay:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website_input} | {email_input} | {password_input}\n")
                website_.delete(0, END)
                email_.delete(0, END)
                password_.delete(0, END)





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

window.mainloop()
