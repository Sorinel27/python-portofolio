from tkinter import *
from quiz_brain import QuizBrain

theme_color = "#375362"


class AppInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(bg=theme_color)

        self.canvas = Canvas(height=250, width=300, bg="white", highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)

        self.image_true = PhotoImage(file="images/true.png")
        self.button_true = Button(image=self.image_true, highlightthickness=0, command=self.right_choice)
        self.button_true.grid(column=0, row=2, pady=20)

        self.image_false = PhotoImage(file="images/false.png")
        self.button_false = Button(image=self.image_false, highlightthickness=0, command=self.wrong_choice)
        self.button_false.grid(column=1, row=2, pady=20)

        self.main_text = self.canvas.create_text(150, 125, text="text", width=280, fill=theme_color,
                                                 font=('Arial', 20, 'italic'))

        self.score_label = Label(text="Score: ", font=("Arial", 11, "normal"), bg=theme_color, fg="white")
        self.score_label.grid(column=1, row=0, pady=20)

        self.get_next_q()

        self.window.mainloop()

    def right_choice(self):
        try:
            x = self.quiz.check_answer(user_answer="True")
            self.score_label.config(text=f"Score: {x}")
            self.get_next_q()
        except IndexError:
            self.canvas.itemconfig(self.main_text, text=f"Your final score: {self.quiz.score}")

    def wrong_choice(self):
        try:
            x = self.quiz.check_answer(user_answer="False")
            self.score_label.config(text=f"Score: {x}")
            self.get_next_q()
        except IndexError:
            self.canvas.itemconfig(self.main_text, text=f"Your final score: {self.quiz.score}")

    def get_next_q(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.main_text, text=q_text)
