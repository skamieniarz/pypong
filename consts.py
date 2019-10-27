''' Module containing constants. '''

# SCREEN
SCREEN_WIDTH = 254
SCREEN_WIDTH_ONE_QUARTER = SCREEN_WIDTH * 0.25
SCREEN_WIDTH_HALF = SCREEN_WIDTH * 0.5
SCREEN_WIDTH_TWO_THIRDS = SCREEN_WIDTH * 0.67
SCREEN_WIDTH_THREE_QUARTERS = SCREEN_WIDTH * 0.75
SCREEN_HEIGHT = 150
SCREEN_HEIGHT_ONE_QUARTER = SCREEN_HEIGHT * 0.25
SCREEN_HEIGHT_HALF = SCREEN_HEIGHT * 0.5
SCREEN_HEIGHT_THREE_QUARTERS = SCREEN_HEIGHT * 0.75
SCALE = 3

# MARGINS
SMALL_MARGIN = 5
MEDIUM_MARGIN = 10
BIG_MARGIN = 20

# COLORS
BLACK = 0
DARK_GREEN = 3
DARK_GREY = 5
WHITE = 7
RED = 8
ORANGE = 9
BLUE = 12

# PADDLE
PADDLE_LENGTH = 20
PADDLE_WIDTH = 2
PADDLE_HALF = PADDLE_LENGTH * 0.5
PADDLE_SPEED = 3
PADDLE_TIP = 3

# BALL
BALL_RADIUS = 2
BALL_SPEED = 4

# MENUS
MENU_SCREENS = ['start', 'controls', 'bot', 'pause', 'win']
START_SCREEN = ['Single-player mode', 'Two-players mode', 'Controls', 'Quit']
CONTROLS_SCREEN_OPTIONS = ['Back']
BOT_SCREEN_OPTIONS = ['Easy', 'Medium', 'Hard', 'Back']
PAUSE_SCREEN_OPTIONS = ['Continue', 'Restart']
WIN_SCREEN = ['Play again', 'Quit']
CONTROLS = [
    'W and S to move the first player\'s paddle,',
    'UP and DOWN arrows to move the second player\'s paddle,',
    'Q or P to pause the game,', 'ESC to quit the game.'
]
