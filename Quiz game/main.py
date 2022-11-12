from question_model import Question
from question_data import data
from quiz_brain import QuizBrain
from ui import AppInterface


def main():
    question_bank = []
    for item in data:
        q = item["question"]
        a = item["correct_answer"]
        obj = Question(q, a)
        question_bank.append(obj)
    quiz = QuizBrain(question_bank)
    quiz_ui = AppInterface(quiz)
    # while quiz.still_has_question():
    #     quiz.next_question()
    print("\nYou've completed the quiz.")
    print(f"Your final score was: {quiz.score}/{quiz.question_number}.")


if __name__ == "__main__":
    main()
