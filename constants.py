import pathlib
from game.casting.color import Color

# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# GAME
GAME_NAME = "Batter"
FRAME_RATE = 60

# SCREEN
SCREEN_WIDTH = 448
SCREEN_HEIGHT = 556
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# FIELD
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
FONT_FILE = "assets/fonts/zorque.otf"
FONT_SMALL = 32
FONT_LARGE = 48

# SOUND
BOUNCE_SOUND = "assets/sounds/boing.wav"
WELCOME_SOUND = "assets/sounds/start.wav"
OVER_SOUND = "assets/sounds/over.wav"

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)

# KEYS
UP = "up"
RIGHT = "right"
DOWN = "DOWN"
LEFT = "left"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"

# SCENES
NEW_GAME = 0
TRY_AGAIN = 1
NEXT_LEVEL = 2
IN_PLAY = 3
GAME_OVER = 4

# LEVELS
LEVEL_FILE = "assets/data/level-{:03}.txt"
BASE_LEVELS = 5

# -------------------------------------------------------------------------------------------------- 
# SCRIPTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# -------------------------------------------------------------------------------------------------- 
# CASTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# STATS
STATS_GROUP = "stats"
DEFAULT_LIVES = 3
MAXIMUM_LIVES = 5

# HUD
HUD_MARGIN = 15
LEVEL_GROUP = "level"
LIVES_GROUP = "lives"
SCORE_GROUP = "score"
LEVEL_FORMAT = "LEVEL: {}"
LIVES_FORMAT = "LIVES: {}"
SCORE_FORMAT = "SCORE: {}"

# BALL
GHOST_GROUP = "balls"
GHOST_IMAGE = "assets/images/000.png"
GHOST_WIDTH = 2
GHOST_HEIGHT = 2
GHOST_RATE = 6
GHOST_VELOCITY = 2

BLINKY_IMAGES = {
    "up": [f"assets/images/{n:02}.png" for n in range(111,113)],
    "right": [f"assets/images/{n:02}.png" for n in range(121, 123)],
    "down": [f"assets/images/{n:02}.png" for n in range(131, 133)],
    "left": [f"assets/images/{n:02}.png" for n in range(141, 143)]
}

PINKY_IMAGES = {
    "up": [f"assets/images/{i:03}.png" for i in range(211,213)],
    "right": [f"assets/images/{i:03}.png" for i in range(221, 223)],
    "down": [f"assets/images/{i:03}.png" for i in range(231,233)],
    "left": [f"assets/images/{i:03}.png" for i in range(241,243)]
}

INKY_IMAGES = {
    "up": [f"assets/images/{i:03}.png" for i in range(311,313)],
    "right": [f"assets/images/{i:03}.png" for i in range(321, 323)],
    "down": [f"assets/images/{i:03}.png" for i in range(331,333)],
    "left": [f"assets/images/{i:03}.png" for i in range(341,343)]
}

CLYDE_IMAGES = {
    "up": [f"assets/images/{i:03}.png" for i in range(411,413)],
    "right": [f"assets/images/{i:03}.png" for i in range(421, 423)],
    "down": [f"assets/images/{i:03}.png" for i in range(431,433)],
    "left": [f"assets/images/{i:03}.png" for i in range(441,443)]
}

SCARED_IMAGES = {
    "up": [f"assets/images/{i:03}.png" for i in range(511, 513)],
    "right": [f"assets/images/{i:03}.png" for i in range(511, 513)],
    "down": [f"assets/images/{i:03}.png" for i in range(511, 513)],
    "left": [f"assets/images/{i:03}.png" for i in range(511, 513)]
}

EYE_IMAGES = {
    "up": [f"assets/images/611.png"],
    "right": [f"assets/images/612.png"],
    "down": [f"assets/images/613.png"],
    "left": [f"assets/images/614.png"]
}

# RACKET
PACMAN_GROUP = "pacman"
PACMAN_IMAGES = {
    "up": [f"assets/images/0{n:02}.png" for n in range(11, 15)],
    "right": [f"assets/images/0{n:02}.png" for n in range(21, 25)],
    "down": [f"assets/images/0{n:02}.png" for n in range(31, 35)],
    "left": [f"assets/images/0{n:02}.png" for n in range(41, 45)]
}
PACMAN_WIDTH = 2
PACMAN_HEIGHT = 2
PACMAN_RATE = 6
PACMAN_VELOCITY = 2

# BRICK
WALL_GROUP = "walls"
WALL_IMAGE = f"assets/images/blank.png"
WALL_THRESHOLD = PACMAN_VELOCITY*2

PATH_GROUP = "paths"
PATH_WIDTH = 2
PATH_HEIGHT = 2
PATH_FILE = "assets/data/paths.txt"

BG_GROUP = "background"
BG_IMAGE = "assets/images/background.png"
BG_WIDTH = 448
BG_HEIGHT = 496

# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
PREP_TO_LAUNCH = "PREPARING TO LAUNCH"
WAS_GOOD_GAME = "GAME OVER"

# DIRECTION
DIR_UP = 0
DIR_RIGHT = 1
DIR_DOWN = 2
DIR_LEFT = 3