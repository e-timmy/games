import math

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Player settings
PLAYER_START_SIZE = 20
PLAYER_ACCELERATION = 0.2
PLAYER_MAX_SPEED = 5
PLAYER_FRICTION = 0.02
PLAYER_ROTATION_SPEED = 5

# Bubble settings
INITIAL_BUBBLE_COUNT = 10
MAX_TOTAL_BUBBLES = 15
MIN_BUBBLE_SIZE = 5
MAX_BUBBLE_SIZE = 40
MIN_BUBBLE_SPEED = 0.5
MAX_BUBBLE_SPEED = 2
WOBBLE_AMOUNT = 0.5
MIN_BUBBLE_DISTANCE = 50

# Absorption mechanics
ABSORPTION_RATE = 0.05  # How quickly bubbles are absorbed (size units per frame)