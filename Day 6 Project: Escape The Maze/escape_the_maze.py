"""
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
Please go to link above and replace the code there with the one commented below
"""
"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# One way of solving infinite loop due to random maze position specific to this maze setup
while not is_facing_north():
    turn_left()
turn_left()

# Second way of solving infinite loop due to random maze position
# while front_is_clear():
#         move()
# turn_left()

while not at_goal():
    if not wall_on_right():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
"""
