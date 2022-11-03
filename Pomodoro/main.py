from tkinter import *
import math


GREEN = "#9bdeac"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
check = ""
timer = None


def reset_timer():
    window.after_cancel(timer)
    global reps
    global check
    reps = 0
    check = ""
    label.config(text="Timer")
    canvas.itemconfig(time_text, text="00:00")
    check_marks.config(text="")


def start_timer():
    global reps
    reps += 1
    if reps % 2 != 0:
        count_down(WORK_MIN * 60)
        label.config(text="Work!")
    if reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        label.config(text="Break!")
    if reps % 2 == 8:
        count_down(LONG_BREAK_MIN * 60)
        label.config(text="Break!")


def count_down(count):
    global check
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(time_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            check += "✔"
        check_marks.config(text=check)


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=GREEN)

canvas = Canvas(width=200, height=224, bg=GREEN, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
time_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=GREEN)
label.grid(column=1, row=0)

button_start = Button(text="Start", highlightthickness=0, command=start_timer)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
button_reset.grid(column=2, row=2)

check_marks = Label(bg=GREEN)
check_marks.grid(column=1, row=2)

window.mainloop()
