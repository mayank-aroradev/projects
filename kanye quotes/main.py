from tkinter import *
import requests
import os

def get_quote():
    response = requests.get("https://api.kanye.rest/")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]

    canvas.itemconfig(quote_text, text=quote)


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)

# 🔧 FIX: correct path handling
base_dir = os.path.dirname(__file__)
background_img = PhotoImage(file=os.path.join(base_dir, "background.png"))

canvas.create_image(150, 207, image=background_img)

quote_text = canvas.create_text(
    150,
    207,
    text="Kanye Quote Goes HERE",
    width=250,
    font=("Arial", 20, "bold"),
    fill="white"
)
canvas.grid(row=0, column=0)

# 🔧 FIX: correct path handling
kanye_img = PhotoImage(file=os.path.join(base_dir, "kanye.png"))
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()
