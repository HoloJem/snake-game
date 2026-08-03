# we need to import pygame and its functions, GameObject the parent class, and some constants from settings. Also imported time .
import pygame
from game_object import GameObject
import time
from settings import SEGMENT_SIZE, OBJECT_COLOR, MOVEMENT_DELAY

# Snake class. For the snake object the player controls. 
# initializes as a game object with location, witdth and height SEGMENT_SIZE, and color OBJECT_COLOR.
# We start a timer object. This will help with our movement delay. By finding the difference between timestamps and setting them to MOVEMENT_DELAY, 
# the snake will move at a reasonable speed.
# the snake is initialized as a "head rectable" which the player controls, and two body segments.
# The body segments are autonomous, and simply travel in locations the head has already visited.
# the self.growth flag helps with growth. V1.0 had the fruit instantly make the snake bigger and it was difficult to control. The growth flag waits until next cycle 
# before the snake grows, for 'smoother gameplay'.

class Snake(GameObject):
    def __init__(self, position):
        x = position[0]
        y = position[1]
        super().__init__(x,y,SEGMENT_SIZE,SEGMENT_SIZE,OBJECT_COLOR)
        self.direction = 'right'
        self.last_movement_time=time.time()
        self.movement_delay=MOVEMENT_DELAY
        self.body = [
            (x,y),
            (x-SEGMENT_SIZE,y),
            (x-2*SEGMENT_SIZE,y)
        ]
        self.growth=False

# the movement function is dependent upon self.direction. Initialized as right, the player can change this via key input.
# direction is stored, and next movement cycle the head will "travel" one SEGMENT_SIZE in that direction.
# this happens by creating a new 'head' object, and inserting it into the front of the self.body list of segments.
# Next growth cycle, we will decide whether to "pop" the oldest segment, symbolizing movement, or "grow" the snake by retaining that last segment.

    def move(self):
        head_x, head_y = self.body[0]
        if self.direction == 'right':
            head_x += SEGMENT_SIZE
        elif self.direction == 'left':
            head_x -= SEGMENT_SIZE
        elif self.direction == 'up':
            head_y -= SEGMENT_SIZE
        elif self.direction == 'down':
            head_y += SEGMENT_SIZE
        self.body.insert(0,(head_x, head_y))

# The update function first checks if difference between 'current time' and 'last movement time' is greater than or equal to the movement delay.
# if it is not, then it simply returns to the main function that called update, as it has nothing to do.
# However, if enough time has passed, it updates 'last movement time' as the current time.
# Then it immediately calls move function, which adds a new head segment.
# If the self.growth flag is active, it turns that flag off, and allows the snake to be one segment larger, simulating 'growth'.
# if the self.growth flag is not active, it pops the last segment, simulating 'movement'.

    def update(self):
        if time.time() - self.last_movement_time <= self.movement_delay:
            return
        self.last_movement_time=time.time()
        self.move()
        if self.growth:
            self.growth = False
        else:
            self.body.pop()

# Head_as_rectangle takes the two first variables in the first segment in self.body, and returns a rectangle. Meaning, it takes the x and y coordinates of the 
# head segment of the snake, and SEGMENT_SIZE twice, and returns a Rectangle object of the same x y coordinates, of size SEGMENT_SIZE. Using pygame's built-in Rectangle
# class, we can use its Rectangle Detect Collision built-in function, which is a lot easier than building my own collision detection system.
# Also, the head of the snake is the only portion of the snake worth tracking for collision detection as the "protagonist". If the head does not collide with a wall or
# fruit, and the body follows the head, it logically follows we dont need to monitor the body, as it will travel in a 'safe' location.


    def head_as_rect(self):
        return pygame.Rect(self.body[0][0], self.body[0][1], SEGMENT_SIZE, SEGMENT_SIZE)

# Other functions will eventually need a setter function for the snakes direction variable. This is that.    
    def change_direction(self, direction):
        self.direction = direction

# Every class has their own draw function. Snake's draw function draws every segment in its body sequentially of the form x,y, SEGMENT_SIZE, SEGMENT_SIZE, using
# Pygames rectangle class's built in draw function.        
    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, OBJECT_COLOR, (segment[0],segment[1],SEGMENT_SIZE,SEGMENT_SIZE))

# Collide_self checks if the snake's head segment, is inside the list body [1,....]. It returns true or false.
    def collide_self(self):
        return self.body[0] in self.body[1:]

# The grow function is a setter function for the snake's variable growth. 
    def grow(self):
        self.growth=True