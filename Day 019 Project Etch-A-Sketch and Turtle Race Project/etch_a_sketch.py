from turtle import Turtle, Screen


def move_turtle1_forward():
    turtle1.forward(10)


def move_turtle1_backwards():
    turtle1.backward(10)


def turn_turtle1_clockwise():
    turtle1.right(10)


def turn_turtle1_anti_clockwise():
    turtle1.left(10)


def clear_screen():
    screen.resetscreen()


turtle1 = Turtle()
screen = Screen()


screen.listen()
screen.onkeypress(key='w', fun=move_turtle1_forward)
screen.onkeypress(key='s', fun=move_turtle1_backwards)
screen.onkeypress(key='d', fun=turn_turtle1_clockwise)
screen.onkeypress(key='a', fun=turn_turtle1_anti_clockwise)
screen.onkeypress(key='c', fun=clear_screen)
screen.exitonclick()
