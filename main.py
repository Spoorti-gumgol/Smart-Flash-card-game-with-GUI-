from tkinter import * # type: ignore
import pandas as pd
import random
import time
BACKGROUND_COLOR = "#B1DDC6"

#-------------------------------------Func-----------------------------------
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    orignal_data = pd.read_csv("data/ja_letters.csv")
    to_learn = orignal_data.to_dict(orient="records")
else:

    to_learn = data.to_dict(orient="records")
current_card = {}


def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title,text="Japanese",fill="black")
    canvas.itemconfig(card_word,text=current_card["Letters"],fill="black")
    canvas.itemconfig(card_background,image=card_front_img)

def flip_card():
    
    canvas.itemconfig(card_title,title="English",fill="white")
    canvas.itemconfig(card_word,text=current_card["English"],fill="white")
    canvas.itemconfig(card_background,image=card_back_img)

def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index=False)
    next_card()

#----------------------------------------UI----------------------------------
window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer = window.after(5000, func=flip_card)

canvas = Canvas(width=600,height=500)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(300,250,image = card_front_img)
card_title = canvas.create_text(300,139,text="",font=("Ariel",40,"italic"))
card_word = canvas.create_text(300,250,text="",font=("Ariel",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)


cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image,highlightthickness=0,command=next_card)
unknown_button.grid(row=1,column=0)

check_img = PhotoImage(file="images/right.png")
known_button = Button(image=check_img,highlightthickness=0,command=is_known)
known_button.grid(row=1,column=1)

next_card()









window.mainloop()