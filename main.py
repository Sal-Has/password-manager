from tkinter import *
import os
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generatepass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []



    password_list=[random.choice(letters) for x in range(nr_letters)]



    password_list.extend([random.choice(symbols) for x in range(nr_symbols)])

    password_list.extend([random.choice(numbers) for x in range(nr_numbers)])
    random.shuffle(password_list)

    password= ''.join(password_list)
    password_e=password_entry.get()
    if len(password_e) == 0:
        password_entry.insert(0,password)

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
        website= website_entry.get()
        email  = email_entry.get()
        password =password_entry.get()
        new_data = {website:{
            'email':email,
            'password':password, }
        }

        if len(password)==0 or len(website)==0:
                messagebox.showinfo(title="Oops",message="Please don't leave any fields empty!")
        else:
            try:
                with open("data.json", mode="r") as recent_file:
                        # Reading old data
                        data=json.load(recent_file)
                        # Updating old data with new data
                        data.update(new_data)
            except FileNotFoundError:
                with open("data.json","w") as recent_file:
                        # Saving updated data
                        json.dump(new_data,recent_file,indent=4)

                        website_entry.delete(0, "end")
                        password_entry.delete(0, "end")
            else:
                with open("data.json","w") as recent_file:
                    json.dump(data,recent_file,indent=4)
                    website_entry.delete(0, "end")
                    password_entry.delete(0, "end")



# ---------------------------- SAVE PASSWORD -------------------------- #
def find_password():
    try:
        with open("data.json","r") as file:
            data = json.load(file)
            website=website_entry.get()
            if website in data.keys():
               messagebox.showinfo(title=website,message=f"Email: {data[website]['email']}\nPassword: {data[website]['password']}")
            else:
                messagebox.showinfo(title=website,message="No details for the website exists")
    except FileNotFoundError:
            messagebox.showinfo(title="Error",message="No Data File Found.")



# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20,bg="white")


canvas = Canvas(width=200,height=200,background="white",highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1,row=0)

# Labels
website_label = Label(text='Website:',bg='white')
email_label = Label(text='Email/Username:',bg='white')
password_label =Label(text='Password:',bg='white')

website_label.grid(column=0,row=1)
email_label.grid(column=0,row=2)
password_label.grid(column=0,row=3)

website_entry = Entry(width=16)
website_entry.focus()
website_entry.grid(column=1,row=1,)
email_entry = Entry(width=35)
email_entry.grid(column=1,row=2,columnspan=2)
email_entry.insert(0,'salimiddi64@gmail.com')

password_entry=Entry(width=16)
password_entry.grid(column=1,row=3)





search_button = Button(text="Search",width=15,command=find_password)
search_button.grid(column=2,row=1)

generate_button = Button(text='Generate Password',command=generatepass)
generate_button.grid(column=2,row=3)



add_button = Button(text="Add",width=30,command=save)
add_button.grid(column=1,row=4,columnspan=2)






window.mainloop()