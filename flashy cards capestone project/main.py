BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import random
import pandas as pandas

# -------------------- DATA LOADING -------------------- #
try:
    data = pandas.read_csv("flashy cards capestone project/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("flashy cards capestone project/data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

current_card = {}

# -------------------- FUNCTIONS -------------------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)

    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)

    flip_timer = window.after(2000, flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

def known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("flashy cards capestone project/data/words_to_learn.csv", index=False)
    next_card()

# -------------------- UI SETUP -------------------- #
window = Tk()
window.title("Flashy Cards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(2000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="flashy cards capestone project/images/card_front.png")
card_back_img = PhotoImage(file="flashy cards capestone project/images/card_back.png")

card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))

canvas.grid(row=0, column=0, columnspan=2)

right_img = PhotoImage(file="flashy cards capestone project/images/right.png")
wrong_img = PhotoImage(file="flashy cards capestone project/images/wrong.png")

Button(image=wrong_img, command=next_card).grid(row=1, column=0)
Button(image=right_img, command=known).grid(row=1, column=1)

next_card()
window.mainloop()
