# Used to adjust screen size
SCREEN_WIDTH = 800
SCREEN_LENGTH = 600

# Used on scoreboard to adjust score and game over text
ALIGNMENT = 'center'
FONT = ('Courier', 30, 'normal')


STARTING_POSITION_PADDLE1 = [(-SCREEN_WIDTH/2 + 20, 40), (-SCREEN_WIDTH/2 + 20, 20), (-SCREEN_WIDTH/2 + 20, 0),
                             (-SCREEN_WIDTH/2 + 20, -20), (-SCREEN_WIDTH/2 + 20, -40)]
STARTING_POSITION_PADDLE2 = [(SCREEN_WIDTH/2 - 20, 40), (SCREEN_WIDTH/2 - 20, 20), (SCREEN_WIDTH/2 - 20, 0),
                             (SCREEN_WIDTH/2 - 20, -20), (SCREEN_WIDTH/2 - 20, -40)]

# Used to created dashed line on MainScreen
NUM_DASHED_LINE = 20
DASHED_LINE_GAP_SIZE = SCREEN_LENGTH / NUM_DASHED_LINE
# DASHED_LINE_SIZE + DASHED_GAP_SIZE Must be igual to DASHED_LINE_GAP_SIZE
DASHED_LINE_SIZE = DASHED_LINE_GAP_SIZE * (2 / 3)
DASHED_GAP_SIZE = DASHED_LINE_GAP_SIZE * (1 / 3)
