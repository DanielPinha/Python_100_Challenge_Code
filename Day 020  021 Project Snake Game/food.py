from turtle import Turtle
import random
from global_variables import SCREEN_LENGTH, SCREEN_WIDTH


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('green')
        self.speed('fastest')
        self.refresh_pos()

    def refresh_pos(self):
        random_x = random.randint(-SCREEN_WIDTH/2 + 20, SCREEN_WIDTH/2 - 20)
        random_y = random.randint(-SCREEN_LENGTH/2 + 20, SCREEN_LENGTH/2 - 20)
        self.goto(random_x, random_y)
