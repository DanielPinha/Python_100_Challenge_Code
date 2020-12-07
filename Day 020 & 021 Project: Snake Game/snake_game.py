from turtle import Screen
from food import Food
from scoreboard import Scoreboard
from global_variables import SCREEN_LENGTH, SCREEN_WIDTH
import time
from snake import Snake

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_LENGTH)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(key='Up', fun=snake.up)
screen.onkeypress(key='Down', fun=snake.down)
screen.onkeypress(key='Left', fun=snake.left)
screen.onkeypress(key='Right', fun=snake.right)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Check collision with food
    if snake.head.distance(food) < 15:
        food.refresh_pos()
        snake.extend()
        scoreboard.score_increase()

    # Check collision with wall
    if snake.head_hit_wall():
        game_is_on = False
        scoreboard.game_over()

    # check snake body collision
    if snake.head_hit_body():
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
