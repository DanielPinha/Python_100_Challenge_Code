from turtle import Turtle
from global_variables import SCREEN_LENGTH, SCREEN_WIDTH, STARTING_POSITION, MOVE_DISTANCE, UP, DOWN, LEFT, RIGHT


class Snake:

    def __init__(self):
        self.segments = []
        self.snake_position = STARTING_POSITION
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in self.snake_position:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape='square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def head_hit_body(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                return True
            return False

    def head_hit_wall(self):
        if self.head.xcor() > SCREEN_WIDTH/2 - 2 or self.head.xcor() < -SCREEN_WIDTH/2 + 2 \
                or self.head.ycor() > SCREEN_LENGTH/2 - 2 or self.head.ycor() < -SCREEN_LENGTH/2 + 2:
            return True
        return False

    def extend(self):
        new_position_x = self.snake_position[-1][0] - 20
        new_position_y = self.snake_position[-1][1]
        new_position = (new_position_x, new_position_y)
        self.add_segment(new_position)
        self.snake_position.append((new_position_x, new_position_y))

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
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
