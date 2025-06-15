from turtle import Turtle, Screen
import random
color_list = [(131, 166, 205), (222, 148, 106), (31, 42, 61), (199, 134, 147), (165, 59, 48), (140, 184, 162), (39, 105, 157), (238, 212, 89), (152, 58, 66), (217, 81, 70), (169, 29, 33), (236, 165, 156), (50, 112, 90), (35, 61, 55), (17, 97, 71), (156, 33, 30), (231, 160, 165), (53, 44, 49), (170, 188, 221), (57, 51, 48), (189, 100, 110), (31, 60, 109), (103, 127, 161), (34, 151, 209), (174, 200, 188), (65, 66, 56), (105, 140, 123), (152, 202, 228), (50, 68, 71), (130, 128, 122)]

SPACE_DOTS = 50
DOT_WIDTH = 20

screen = Screen()
screen.colormode(255)

turtle1 = Turtle()
turtle1.shape('classic')
turtle1.speed('fastest')
turtle1.penup()
turtle1.hideturtle()

column_pos = -5
line_pos = -5

while line_pos <= 4:
    turtle1.setpos(column_pos*SPACE_DOTS, line_pos*SPACE_DOTS)
    turtle1.dot(DOT_WIDTH, random.choice(color_list))

    column_pos += 1
    if column_pos > 4:
        column_pos = -5
        line_pos += 1

screen.exitonclick()
