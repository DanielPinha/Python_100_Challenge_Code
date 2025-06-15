from turtle import Turtle
from global_variables_pong import  SCREEN_LENGTH


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(position)
        self.initial_pos = self.position()

    def up(self):
        if self.ycor() < SCREEN_LENGTH / 2:
            self.goto(self.xcor(), self.ycor() + 60)

    def down(self):
        if self.ycor() > -SCREEN_LENGTH / 2:
            self.goto(self.xcor(), self.ycor() - 60)

    def reset_pos(self):
        self.goto(self.initial_pos)
