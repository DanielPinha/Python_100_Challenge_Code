from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.setup(width=730, height=491)
screen.title("U.S State Game")
screen.bgpic('blank_states_img.gif')

turtle = Turtle()
turtle.hideturtle()
turtle.penup()

us_state_data = pandas.read_csv("50_states.csv")

# Store the list of states already correctly guessed
state_list_guessed = []

while len(state_list_guessed) < 50:
    user_ans = screen.textinput(f"{len(state_list_guessed)}/50 Enter state", prompt="Please enter state name: ").title()
    if user_ans == 'Exit':
        break
    search_state = us_state_data[us_state_data['state'] == user_ans]
    # If the answer is a correct state, search_state length will not be 0
    if len(search_state) != 0:
        # Evaluate if correct answer is new item to be inserted
        if user_ans not in state_list_guessed:
            state_list_guessed.append(user_ans)
            turtle.goto(int(search_state.x), int(search_state.y))
            turtle.pendown()
            # Two other forms of getting the state information for future reference
            # turtle.write(search_state['state'].to_string(index=False))
            # turtle.write(search_state['state'].item())
            turtle.write(user_ans)
            turtle.penup()

missing_state_list = []
# for all states in the US state data file
for state in us_state_data['state']:
    # if state is  not in guessed list, user did not managed to guess
    if state not in state_list_guessed:
        missing_state_list.append(state)
# Create dataframe based on missing state list and set column to Missing State(s)
missing_state_df = pandas.DataFrame(missing_state_list, columns=["Missing State(s)"])
# Create .csv with all missing states in order to player to learn the missing states
missing_state_df.to_csv("Missing_states_by_player.csv")

