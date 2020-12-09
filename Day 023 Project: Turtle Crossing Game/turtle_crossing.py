from turtle import Screen
import time
import random
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

NEW_CAR_CONT_TRIGGER = 6
RANDOM_CAR_UPPER_VALUE = 2

screen = Screen()
screen.setup(width=600, height=600)
screen.title('Turtle Crossing Game')
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move, 'Up')

game_is_on = True
new_car_cont = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if new_car_cont == NEW_CAR_CONT_TRIGGER:
        for _ in range(random.randint(0, RANDOM_CAR_UPPER_VALUE)):
            car_manager.create_new_car()
        new_car_cont = 0

    new_car_cont += 1
    car_manager.move()

    # Check collision with cars
    for car in car_manager.car_list:
        if player.distance(car) < 15:
            game_is_on = False
            scoreboard.game_over()

    # Check if player reach end of level
    if player.is_at_finish_line():
        player.move_to_start()
        scoreboard.increase_level()
        car_manager.increase_speed()

screen.exitonclick()
