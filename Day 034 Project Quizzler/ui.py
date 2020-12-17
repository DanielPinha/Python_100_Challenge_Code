import tkinter
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT = ('arial', 20, 'italic')


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_text = tkinter.Label(text=f'Score: {self.quiz.score}', bg=THEME_COLOR, fg='white')
        self.score_text.grid(row=0, column=1)

        self.canvas = tkinter.Canvas(width=300, height=250)
        self.canvas.config(highlightthickness=0, bg='white')
        self.question_text = self.canvas.create_text(150, 125, text='Question', font=FONT, fill=THEME_COLOR, width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = tkinter.PhotoImage(file='./images/true.png')
        self.true_button = tkinter.Button(image=true_img, highlightthickness=0,
                                          command=lambda: self.get_answer_eval('True'))
        self.true_button.grid(row=2, column=0)

        false_img = tkinter.PhotoImage(file='./images/false.png')
        self.false_button = tkinter.Button(image=false_img, highlightthickness=0,
                                           command=lambda: self.get_answer_eval('False'))
        self.false_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def get_answer_eval(self, user_ans: str):
        is_user_right = self.quiz.check_answer(user_ans)
        if is_user_right:
            self.canvas.config(bg='lightgreen')
        else:
            self.canvas.config(bg='red')
        self.window.after(500, self.update_score_question)

    def update_score_question(self):
        self.canvas.config(bg='white')
        self.score_text.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            self.get_next_question()
        else:
            self.end_of_question()

    def end_of_question(self):
        self.canvas.itemconfig(self.question_text, text='You reached the end of the quiz')
        self.true_button.config(state='disabled')
        self.false_button.config(state='disabled')
