from main_screen import MainScreen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from global_variables_pong import SCREEN_WIDTH
import time


def reset_game():
    paddle_r.reset_pos()
    paddle_l.reset_pos()
    ball.restart()


main_screen = MainScreen()

paddle_r = Paddle((SCREEN_WIDTH / 2 - 30, 0))
paddle_l = Paddle((-SCREEN_WIDTH / 2 + 30, 0))

ball = Ball()

scoreboard = Scoreboard()

main_screen.screen.listen()
main_screen.screen.onkeypress(key='Up', fun=paddle_r.up)
main_screen.screen.onkeypress(key='Down', fun=paddle_r.down)
main_screen.screen.onkeypress(key='w', fun=paddle_l.up)
main_screen.screen.onkeypress(key='s', fun=paddle_l.down)

time_sleep = 0.05
while True:
    main_screen.screen.update()
    time.sleep(time_sleep)

    # move ball
    ball.move()

    # Check collision with upper and lower wall
    ball.check_hit_y_wall()

    # Check collision with paddles
    if ball.distance(paddle_r) < 50 and ball.xcor() > SCREEN_WIDTH / 2 - 40:
        ball.hit_paddle_bounce()

    if ball.distance(paddle_l) < 50 and ball.xcor() < -SCREEN_WIDTH / 2 + 40:
        ball.hit_paddle_bounce()

    # Check Paddle_l misses
    if ball.xcor() > SCREEN_WIDTH / 2 - 10:
        reset_game()
        scoreboard.score_paddle_r_increase()
    # Check Paddle_r misses
    if ball.xcor() < -SCREEN_WIDTH / 2 + 10:
        reset_game()
        scoreboard.score_paddle_l_increase()
