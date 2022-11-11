import  html

class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        self.current_question = None

    def still_has_question(self):
        ok = True
        if self.question_number == len(self.question_list):
            ok = False
        return ok

    def next_question(self):
        q = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(q.text)
        user_answer = input(f"Q.{self.question_number}: {q_text} (True/False): ")
        self.check_answer(user_answer, q.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("That's correct!")
            self.score += 1
        else:
            print("That's wrong.")
            print(f"The correct answer was {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
