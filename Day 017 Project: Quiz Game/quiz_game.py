from quiz_data import question_data
from quiz_question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_bank.append(Question(question['question'], question['correct_answer']))

brain = QuizBrain(question_bank)
while brain.still_has_questions():
    brain.next_question()

print("You reach the end of the quiz")
print(f"Your final score is {brain.score}/{brain.question_number}")
