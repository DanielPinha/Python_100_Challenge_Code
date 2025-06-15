from turtle import Turtle
from global_variables import SCREEN_LENGTH, SCREEN_WIDTH, ALIGNMENT, FONT


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.color('white')
        self.goto(0, SCREEN_LENGTH/2 - 30)
        self.draw_score()

    def score_increase(self):
        self.score += 1
        self.draw_score()

    def draw_score(self):
        self.clear()
        self.draw_boundary()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over!", align=ALIGNMENT, font=FONT)

    def draw_boundary(self):
        initial_pos = self.position()
        self.goto(SCREEN_WIDTH/2 - 2, SCREEN_LENGTH/2 - 2)
        self.pendown()
        self.pencolor('white')
        self.goto(SCREEN_WIDTH/2 - 2, -SCREEN_LENGTH/2 + 2)
        self.goto(-SCREEN_WIDTH/2 + 2, -SCREEN_LENGTH/2 + 2)
        self.goto(-SCREEN_WIDTH / 2 + 2, SCREEN_LENGTH / 2 - 2)
        self.goto(SCREEN_WIDTH / 2 - 2, SCREEN_LENGTH / 2 - 2)
        self.penup()
        self.goto(initial_pos)
