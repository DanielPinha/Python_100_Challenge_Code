from turtle import Turtle, Screen
import random

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400
SCREEN_OFFSET = 10
# Max allowed is 29 turtles
NUMBER_OF_TURTLES = 8
TURTLE_SPACES = SCREEN_HEIGHT / NUMBER_OF_TURTLES

turtle_colours = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'black', 'brown', 'pink', 'gray',
                  'olive', 'cyan', 'forestgreen', 'limegreen', 'darkorange', 'gold', 'steelblue', 'magenta', 'peru',
                  'coral', 'silver', 'moccasin', 'deepskyblue', 'teal', 'tan', 'lightgreen', 'fuchsia', 'chocolate'
                  ]

for _ in range(NUMBER_OF_TURTLES):
    turtle_obj = Turtle(shape='turtle')

screen = Screen()

# Raise pen and set turtle color
race_pos = 0
for turtle in screen.turtles():
    turtle.penup()
    turtle.color(turtle_colours[race_pos])
    race_pos += 1

# Set screen width and height
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

# Get user bet input and shown the available colours to bet
available_colours = []
for colour in range(NUMBER_OF_TURTLES):
    available_colours.append(turtle_colours[colour])
user_bet = screen.textinput(title="Bet on turtles", prompt=f"Available colours: {available_colours}\n"
                                                           "Which turtle will win the race? Enter a colour: ")

# lower case the user input if any
if user_bet is not None:
    user_bet = user_bet.lower()

# Adjust turtle position for race based on screen width and height, include offset to make turtle visible
race_pos = 0
for turtle in screen.turtles():
    turtle.goto(x=-(SCREEN_WIDTH / 2 - SCREEN_OFFSET), y=(SCREEN_HEIGHT / 2 - SCREEN_OFFSET) - TURTLE_SPACES * race_pos)
    race_pos += 1

# Set winning turtle parameter and start race
winning_turtle = turtle_obj
race_on_going = True
while race_on_going:
    # Move turtle at random amount
    for turtle in screen.turtles():
        step_movement = random.randint(0, 10)
        turtle.forward(step_movement)
        # Check current turtle that is closest to finish line
        if turtle.xcor() > winning_turtle.xcor():
            winning_turtle = turtle

    # If winning turtle is on the end of the screen, the turtle won.
    # All turtles are 40x40. so the head is advanced in the x cor by 20
    if winning_turtle.xcor() >= (SCREEN_WIDTH / 2 - 20):
        race_on_going = False
        screen.bye()

# Check if user bet on the right turtle
if user_bet == winning_turtle.color()[0]:
    print(f"You won the bet! the winning turtle is {winning_turtle.color()[0]}")
else:
    print(f"You lost the bet! the winning turtle is {winning_turtle.color()[0]}")
