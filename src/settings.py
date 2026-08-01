import random
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SEGMENT_SIZE = 50
SNAKE_START_LOCATION = (100,100)
OBJECT_COLOR = (255,255,255)
def RANDOM_COLOR():
    return (random.randrange(50,205,1),random.randrange(50,205,1),random.randrange(50,205,1))

MOVEMENT_DELAY = 0.25