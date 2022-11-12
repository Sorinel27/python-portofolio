import html
ans = ""

class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        self.q_text = ""
        global ans
        q = self.question_list[self.question_number]
        ans = q.answer

    def still_has_question(self):
        ok = True
        if self.question_number == len(self.question_list):
            ok = False
        return ok

    def next_question(self):
        global ans
        q = self.question_list[self.question_number]
        ans = q.answer
        self.question_number += 1
        self.q_text = html.unescape(q.text)
        return f"Q.{self.question_number}: {self.q_text}"
        # user_answer = input(f"Q.{self.question_number}: {q_text} (True/False): ")
        # self.check_answer(user_answer, q.answer)

    def check_answer(self, user_answer):
        global ans
        q = self.question_list[self.question_number]
        ans = q.answer
        if user_answer.lower() == ans.lower():
            self.score += 1
        return self.score
