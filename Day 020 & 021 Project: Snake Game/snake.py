from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.snake_position = STARTING_POSITION
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in self.snake_position:
            new_segment = Turtle(shape='square')
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.snake_position) - 1, 0, -1):
            self.segments[seg_num].goto(self.snake_position[seg_num - 1])
            self.snake_position[seg_num] = self.segments[seg_num].position()
        self.head.forward(MOVE_DISTANCE)
        self.snake_position[0] = self.head.position()

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
