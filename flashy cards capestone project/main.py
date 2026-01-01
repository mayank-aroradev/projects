BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
from tkinter import messagebox
import random
import json

window= Tk()
window.title("flashy cards")
window.config(bg= BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(width=800, height=526, bg= BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="flashy cards capestone project/images/card_front.png")
card_back_img = PhotoImage(file="flashy cards capestone project/images/card_back.png")
card_background = canvas.create_image(400,263, image= card_front_img)
canvas.grid(row=0, column=0, columnspan=2)
card_title = canvas.create_text(400,150, text="english", font=("Ariel", 40, "italic"))
card_word= canvas.create_text(400,263, text="word",font=("Ariel", 60, "bold"))

my_image= PhotoImage(file="flashy cards capestone project/images/right.png")
button = Button(image=my_image,text="Button")
button.grid(row=1, column=1)

window.mainloop() 