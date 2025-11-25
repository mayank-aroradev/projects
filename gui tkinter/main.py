from tkinter import *
window = Tk()
window.title("my First GUI Program")
window.minsize(width=500, height=300)

my_label = Label(text="i am a Label ", font=("Arial",24,"bold"))
my_label.pack()

def button_clicked():
    print("i got clicked")
    new_text = input.get()

    my_label.config(text= new_text)

button = Button(text="click Me ", command= button_clicked)
button.pack()

input = Entry(width=10)
input.pack()
print(input.get())










window.mainloop()
