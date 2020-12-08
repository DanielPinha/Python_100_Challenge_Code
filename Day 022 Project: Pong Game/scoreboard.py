from turtle import Turtle
from global_variables_pong import SCREEN_LENGTH, SCREEN_WIDTH, ALIGNMENT, FONT


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score_paddle_r = 0
        self.score_paddle_l = 0
        self.color('white')
        self.goto(-60, SCREEN_LENGTH / 2 - 60)
        self.draw_score()

    def draw_score(self):
        current_position = self.position()
        self.clear()
        self.write(f"{self.score_paddle_r}", align=ALIGNMENT, font=FONT)
        self.goto(60, SCREEN_LENGTH / 2 - 60)
        self.write(f"{self.score_paddle_l}", align=ALIGNMENT, font=FONT)
        self.goto(current_position)

    def score_paddle_r_increase(self):
        self.score_paddle_r += 1
        self.draw_score()

    def score_paddle_l_increase(self):
        self.score_paddle_l += 1
        self.draw_score()
