import pandas as pd
import random
from deep_translator import GoogleTranslator
from tkinter import *
import tkinter as tk

list_words = []
new_list = []
data_dict = {"Romanian": [], "English": []}
BACKGROUND_COLOR = "#B1DDC6"
LABEL_BACKGROUND_COLOR = "#91C2AF"
ro = ""
en = ""
WORDS_NUMBER = 0
FILE_NEW = "ro_words.csv"
FILE_OLD = "words_to_learn.csv"

"""
This function takes the most used romanian words in movie/tv series subtitles,
and puts them in a csv file along with their translation in english
"""


def from_txt_to_csv():
    global list_words
    global new_list
    global data_dict
    global WORDS_NUMBER
    nr = -1
    with open("ro.txt", "r+", encoding="utf8") as file:
        for i in file:
            nr += 1
            list_words.append(i)
            # first 5000 romanian words to be translated
            if nr == 5000:
                break
        file.close()
    WORDS_NUMBER = nr
    for row in list_words:
        word = ""
        ok = True
        while ok:
            for i in range(len(row)):
                if row[i] != " ":
                    word += row[i]
                else:
                    ok = False
                    break
        new_list.append(word)
    for item in new_list:
        data_dict["Romanian"].append(item)
        data_dict["English"].append(GoogleTranslator(source='ro', target='en').translate(item))
        print(data_dict)
    new_data = pd.DataFrame(data_dict)
    new_data.to_csv("ro_words.csv", index=False, encoding="utf-8-sig")


def wrong_choice():
    print(WORDS_NUMBER)
    window.after_cancel(window)
    global ro
    global en
    col_names = ['Romanian', 'English']
    ro_words = []
    en_words = []
    if FILE_OLD:
        file = FILE_OLD
    else:
        file = FILE_NEW
    try:
        words_data = pd.read_csv(file)
    except FileNotFoundError:
        words_data = pd.read_csv(FILE_NEW)
    for item in words_data[col_names[0]]:
        ro_words.append(item)
    for item in words_data[col_names[1]]:
        en_words.append(item)
    random_index = random.randint(0, WORDS_NUMBER)
    print(random_index)
    ro = ro_words[random_index]
    en = en_words[random_index]
    canvas.itemconfig(canvas_image, image=front_card)
    label_word.config(text=ro, bg="white", fg="black")
    label_language.config(text="Romanian", bg="white", fg="black")
    window.after(3000, change_card)


def right_choice():
    print(WORDS_NUMBER)
    window.after_cancel(window)
    global ro
    global en
    global data_dict
    col_names = ['Romanian', 'English']
    ro_words = []
    en_words = []
    data_dict[col_names[0]].remove(ro)
    data_dict[col_names[1]].remove(en)
    new_data = pd.DataFrame(data_dict)
    new_data.to_csv("words_to_learn.csv", index=False, encoding="utf-8-sig")
    if FILE_OLD:
        file = FILE_OLD
    else:
        file = FILE_NEW
    try:
        words_data = pd.read_csv(file)
    except FileNotFoundError:
        words_data = pd.read_csv(FILE_NEW)
    for item in words_data[col_names[0]]:
        ro_words.append(item)
    for item in words_data[col_names[1]]:
        en_words.append(item)
    print(WORDS_NUMBER)
    random_index = random.randint(0, WORDS_NUMBER)
    print(random_index)
    ro = ro_words[random_index]
    en = en_words[random_index]
    canvas.itemconfig(canvas_image, image=front_card)
    label_word.config(text=ro, bg="white", fg="black")
    label_language.config(text="Romanian", bg="white", fg="black")
    window.after(3000, change_card)


def change_card():
    global en
    global ro
    canvas.itemconfig(canvas_image, image=back_card)
    label_word.config(text=en, bg=LABEL_BACKGROUND_COLOR, fg="white")
    label_language.config(text="English", bg=LABEL_BACKGROUND_COLOR, fg="white")


def random_word():
    global ro
    global en
    global WORDS_NUMBER
    global data_dict
    col_names = ['Romanian', 'English']
    ro_words = []
    en_words = []
    if FILE_OLD:
        file = FILE_OLD
    else:
        file = FILE_NEW
    try:
        words_data = pd.read_csv(file)
    except FileNotFoundError:
        words_data = pd.read_csv(FILE_NEW)
    for item in words_data[col_names[0]]:
        WORDS_NUMBER += 1
        ro_words.append(item)
        data_dict[col_names[0]].append(item)
    for item in words_data[col_names[1]]:
        en_words.append(item)
        data_dict[col_names[1]].append(item)
    random_index = random.randint(0, WORDS_NUMBER)
    ro = ro_words[random_index]
    en = en_words[random_index]


# uncomment the line below if you don't have the ro-en csv file
# from_txt_to_csv()

window = Tk()
window.title("Flash card")
# window.wm_attributes('-transparentcolor', window['bg'])
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=527, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card = PhotoImage(file="images/card_front.png")
back_card = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_card)
canvas.grid(column=0, row=0, columnspan=2)

label_language = Label(text="Romanian", font=("Ariel", 40, "italic"), bg="white")
label_language.place(anchor='center', x=400, y=150)

random_word()
label_word = Label(text=ro, font=("Ariel", 60, "bold"), bg="white")
label_word.place(anchor='center', x=400, y=263)

image_button_wrong = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=image_button_wrong, command=wrong_choice, highlightthickness=0, bg=BACKGROUND_COLOR,
                      borderwidth=0)
button_wrong.grid(column=0, row=1)

image_button_right = PhotoImage(file="images/right.png")
button_right = Button(image=image_button_right, command=right_choice, highlightthickness=0, bg=BACKGROUND_COLOR,
                      borderwidth=0)
button_right.grid(column=1, row=1)

window.after(3000, change_card)

window.mainloop()
