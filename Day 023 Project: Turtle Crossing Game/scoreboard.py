from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.color('black')
        self.goto(-270, 250)
        self.draw_level()

    def draw_level(self):
        self.clear()
        self.write(f"LEVEL: {self.level}", font=FONT)

    def increase_level(self):
        self.level += 1
        self.draw_level()

    def game_over(self):
        self.goto(-100, 0)
        self.write("GAME OVER", font=FONT)
