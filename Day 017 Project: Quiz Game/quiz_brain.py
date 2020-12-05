class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_ans = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
        self.check_answer(user_ans, current_question.answer)

    def check_answer(self, user_input, q_answer):
        if user_input.lower() == q_answer.lower():
            self.score += 1
            print("You answer correctly")
        else:
            print("You answer is wrong")
        print(f"Current answer is: {q_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}\n\n")
