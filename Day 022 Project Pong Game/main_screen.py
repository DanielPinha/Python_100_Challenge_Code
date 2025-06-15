from turtle import Screen, Turtle
from global_variables_pong import SCREEN_LENGTH, SCREEN_WIDTH, NUM_DASHED_LINE, DASHED_LINE_SIZE, DASHED_GAP_SIZE


class MainScreen:
    def __init__(self):
        self.screen = Screen()

        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_LENGTH)
        self.screen.bgcolor('black')
        self.screen.title('Pong Game')
        self.screen.tracer(0)

        self.pen = Turtle()
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.color('white')
        self.draw_boundary()
        self.draw_center_dashed_line()

    def draw_boundary(self):
        initial_pos = self.pen.position()
        self.pen.goto(SCREEN_WIDTH / 2, SCREEN_LENGTH / 2)
        self.pen.pendown()
        self.pen.pencolor('white')
        self.pen.goto(SCREEN_WIDTH / 2, -SCREEN_LENGTH / 2)
        self.pen.goto(-SCREEN_WIDTH / 2, -SCREEN_LENGTH / 2)
        self.pen.goto(-SCREEN_WIDTH / 2, SCREEN_LENGTH / 2)
        self.pen.goto(SCREEN_WIDTH / 2, SCREEN_LENGTH / 2)
        self.pen.penup()
        self.pen.goto(initial_pos)

    def draw_center_dashed_line(self):
        self.pen.goto(0, SCREEN_LENGTH/2)
        for _ in range(NUM_DASHED_LINE):
            self.pen.pendown()
            self.pen.goto(0, self.pen.ycor() - DASHED_LINE_SIZE)
            self.pen.penup()
            self.pen.goto(0, self.pen.ycor() - DASHED_GAP_SIZE)

