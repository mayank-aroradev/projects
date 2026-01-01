from tkinter import *
from tkinter import messagebox
import json



def generate():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")
    nr_letters = random.randint(0,10)
    nr_symbols = random.randint(2,4)
    nr_numbers = random.randint(2,4)
    password_letters =[random.choice(letters) for _ in range(nr_letters)]
    password_symbol = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers =[random.choice(numbers) for _ in range (nr_numbers)]

    password_list = password_letters + password_symbol + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list) 

    password_entry.insert(0, password)

 
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            "email": email,
            "password": password,

        }
    }

    if len(website)== 0 or len(password)==0:
        messagebox.showinfo(title= "oops", message="please make sure you havent left any field")
    else:  
        try: 
    
        
    

            with open(r"C:\Users\dell\Desktop\projects\password manager\data.json", "r") as data_files:
                #reading old data
                data = json.load(data_files)
        
            #updating old data with new one 
        except FileNotFoundError:
             with open("C:/Users/dell/Desktop/projects/password manager/data.json", "w") as data_file:

                 json.dump(new_data,data_file, indent=4)

        else:
             data.update(new_data)
        
            
             with open(r"C:\Users\dell\Desktop\projects\password manager\data.json", "w") as data_files:
                json.dump(data, data_files, indent=4)
            
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0,END)

def search():
    website2 = website_entry.get()

    try:
        with open(r"C:\Users\dell\Desktop\projects\password manager\data.json", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")

    else:
        if website2 in data:
            email = data[website2]["email"]
            password = data[website2]["password"]
            messagebox.showinfo(
                title="Your Info",
                message=f"Email: {email}\nPassword: {password}"
            )
        else:
            messagebox.showinfo(title="Not Found", message="No details for this website")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file=r"C:\Users\dell\Desktop\projects\password manager\logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()  # cursor focus

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "example@gmail.com")  # optional default

password_entry = Entry(width=35)
password_entry.grid(row=3, column=1,columnspan=2)

# Buttons
generate_password_button = Button(text="Generate Password",width= 20, command= generate)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command= save )
add_button.grid(row=4, column=1, columnspan=2)

search_button= Button(text="Search", width=20, command= search)
search_button.grid(row=1, column=2, columnspan=2)
window.mainloop() 
