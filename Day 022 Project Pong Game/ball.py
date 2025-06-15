from turtle import Turtle
from global_variables_pong import SCREEN_LENGTH, SCREEN_WIDTH


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.speed(0)
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.penup()
        self.x_add = 10
        self.y_add = 10

    def move(self):
        self.goto(self.xcor() + self.x_add, self.ycor() + self.y_add)

    def restart(self):
        self.goto(0, 0)
        self.y_add = 10
        self.x_add *= -1

    def check_hit_y_wall(self):
        if self.ycor() > SCREEN_LENGTH/2 - 20 or self.ycor() < -SCREEN_LENGTH/2 + 20:
            self.y_add *= -1

    def hit_paddle_bounce(self):
        self.x_add *= -1
        # Check if ball is going straight and add little curve to avoid stuck the game
        if 0 < self.y_add < 10:
            self.y_add += 10
        elif 0 > self.y_add > -10:
            self.y_add -= 10

