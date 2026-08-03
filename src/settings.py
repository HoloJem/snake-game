# These are all the constants and functions that will be imported! Whoever is reading this, you can modify any of these variables!
# A smaller segment size makes the game easier.
# All values in the form (255,255,255) are color values. (255,255,255) is white, (0,0,0) is black, experiment and have fun.
# Movement_Delay controls how fast the snake moves! 0.25 means every 0.25 seconds the snake moves.


import random
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SEGMENT_SIZE = 50
SNAKE_COLOR=(75,75,75)
SNAKE_START_LOCATION = (150,150)
OBJECT_COLOR = (255,255,255)
BACKGROUND_COLOR = (0,0,0)
FONT_COLOR = (0,0,0)
def random_color():
    return (random.randrange(50,205,1),random.randrange(50,205,1),random.randrange(50,205,1))

MOVEMENT_DELAY = 0.25