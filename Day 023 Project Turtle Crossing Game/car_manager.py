from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.car_list = []
        self.car_move_speed = STARTING_MOVE_DISTANCE

    def create_new_car(self):
        new_car = Turtle()
        new_car.shape('square')
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        new_car.setheading(180)
        new_y = random.randint(-250, 250)
        new_car.goto(300, new_y)
        self.car_list.append(new_car)

    def increase_speed(self):
        self.car_move_speed += MOVE_INCREMENT

    def move(self):
        for car in self.car_list:
            car.forward(self.car_move_speed)
