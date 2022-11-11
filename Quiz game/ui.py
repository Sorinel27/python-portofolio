from tkinter import *

theme_color = "#375362"


class AppInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quiz App")
        self.button_true = Button(column=0, row=2)
        self.button_false = Button(column=1, row=2)
        #to be completed...



        self.window.mainloop()
