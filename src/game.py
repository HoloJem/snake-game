# importing everything we need, pygame and random, Snake, Wall, Fruit, some constants, and my random_color() function.
import pygame
import random

from snake import Snake
from wall import Wall
from fruit import Fruit

from settings import SCREEN_WIDTH, SCREEN_HEIGHT, SEGMENT_SIZE, SNAKE_START_LOCATION, FONT_COLOR, BACKGROUND_COLOR, random_color

# Game is the actual game that main will call. Going through the variables one by one... Running flag allows the game loop to continue.
# screen is the screen that pygame is rendering to user.
# tombstone is a placeholder for a game over image I will show to the user later.
# Then we set the window title to Snake, create a clock to help with fps, and create two fonts. A big one for score, and a small one for game over.
# The gameover boolean is used for a conditional later: Render the game world, or render the game over screen?
# Score is an integer that increases with every fruit eaten.
# The score can be almost any color. I thought this would be fun.
# Then we create an empty list called walls, and run the create walls function, which populates walls with a list of Wall objects.
# We initialize self.fruit, then call the spawn_fruit function, which creates a fruit object.
# We initialize a snake object as well. With a battlefield, a snake, walls, and a fruit, the game is set at this point.
# finally we start the mixer, give it our sound effect "oof.mp3" saved for later as death_sound, give it our song alexei.mp3, set the volume at a cool 40%, and loop it.

class Game:
    def __init__(self):
        self.running = True
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.tombstone = pygame.image.load("assets/tombstone.jpg").convert()
        pygame.display.set_caption("Snake")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None,36)
        self.smallfont = pygame.font.Font(None,18)

        self.game_over = False
        self.score = 0
        self.score_color=random_color()
        self.walls = []
        self.create_walls()
        self.fruit = None
        self.spawn_fruit()
        self.snake = Snake(SNAKE_START_LOCATION)
        self.death_sound = pygame.mixer.Sound("assets/ouch.wav")
        pygame.mixer.music.load("assets/alexei.mp3")
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(-1)

#The create walls function is a helper function for easier readability. Each wall is actually as many 'rectangular segments' as can fit into the screen. First top and bottom
# then left and right walls.
    def create_walls(self):
        for x in range(0, SCREEN_WIDTH, SEGMENT_SIZE):
            self.walls.append(Wall(x,0,SEGMENT_SIZE,SEGMENT_SIZE))
            self.walls.append(Wall(x,SCREEN_HEIGHT-SEGMENT_SIZE,SEGMENT_SIZE,SEGMENT_SIZE))

        for y in range(0, SCREEN_HEIGHT, SEGMENT_SIZE):
            self.walls.append(Wall(0,y,SEGMENT_SIZE,SEGMENT_SIZE))
            self.walls.append(Wall(SCREEN_WIDTH-SEGMENT_SIZE, y, SEGMENT_SIZE, SEGMENT_SIZE))

# The spawn_fruit function chooses a random x and y coordinate using the randrange function. Anywhere thats within the screen boundaries, but not within the wall. 
    def spawn_fruit(self):
        x = random.randrange(SEGMENT_SIZE, SCREEN_WIDTH-SEGMENT_SIZE, SEGMENT_SIZE)
        y = random.randrange(SEGMENT_SIZE, SCREEN_HEIGHT-SEGMENT_SIZE, SEGMENT_SIZE)
        self.fruit = Fruit(x,y)

# show_score renders the text Score: {self.score} Up on the top of the screen in a random color. 
    def show_score(self):
        text = self.font.render(f"Score: {self.score}",True,self.score_color)
        self.screen.blit(text,(10,10))

# The event_handler program... handles events. Key presses modify directions, and QUIT quits the game. 
    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.snake.change_direction("right")
                elif event.key == pygame.K_LEFT:
                    self.snake.change_direction("left")
                elif event.key == pygame.K_UP:
                    self.snake.change_direction("up")
                elif event.key == pygame.K_DOWN:
                    self.snake.change_direction("down")

#a helper function to compress the code a little. Plays a sound, stops the music..
    def die_snake(self):
        self.game_over=True
        pygame.mixer.music.stop()
        self.death_sound.play()

# The update function. First htis checks for collisions in the current game state of the world. Did the head hit the body? Did the head hit the walls? If so,
# we set the game_over tag to true. If the snake head collided with fruit, then we run the setter function for the growth flag, increase score by 1, and spawn a new fruit.
# If we didnt hit the fruit, then we just update the snake. Easy.
    def update(self):
        if self.snake.collide_self():
            self.die_snake()
        for wall in self.walls:
            if self.snake.head_as_rect().colliderect(wall.rect):
                self.die_snake()
        if self.snake.head_as_rect().colliderect(self.fruit.rect):
            self.snake.grow()
            self.score += 1
            self.spawn_fruit()
        else: 
            self.snake.update()




# The draw function first sets the data to display to user, and then at the very end uses display.flip to render that data to a visible format.
# First things first, if the game_over flag is set, we jump straight to show_game_over(). That function will be discussed later. For now, 
# if the game_over boolean is not set, then we simply fill the screen with the background color, and then call every object's draw function:
# snake, walls fruit. Then the score displays itself.
# Finally, pygame.display.flip shows the user the new display.

    def draw(self):
        if self.game_over:
            self.show_game_over()
        else:
            self.screen.fill(BACKGROUND_COLOR)
            self.snake.draw(self.screen)
            for wall in self.walls:
                wall.draw(self.screen)
            self.fruit.draw(self.screen)
            self.show_score()
        pygame.display.flip()

# The show_game_over function. If the flag was set, this function will be called. Rather than rendering and drawing the snake, the walls, fruit and score, that
# is no longer necessary. Now we have a different set of drawing and rendering instructions.
# We fill the screen with background color, then blit our image of the tombstone, in roughly the center of the screen.
# we save 3 strings. score_text showing the users score. Thanks_text, thanking them, and quit_text, teaching them how to exit. They can stare at the art as long as they want.
# We blit all 3 strings onto the screen at readable locations.
# The True means "anti-aliasing". Feel free to modify.

    def show_game_over(self):
        self.screen.fill(BACKGROUND_COLOR)
        self.screen.blit(self.tombstone, (233,0))
        score_text = self.smallfont.render(f"Your high score was {self.score}", True, FONT_COLOR)
        thanks_text = self.smallfont.render(f"Thank you for playing my game.", True, FONT_COLOR)
        quit_text = self.smallfont.render(f"Press any key to exit.", True, FONT_COLOR)
        self.screen.blit(score_text, (355, 325))
        self.screen.blit(thanks_text, (355, 350))
        self.screen.blit(quit_text, (355, 375))

# death_check is a function with a simple use. After the tombstone is rendered, we want to wait for the user to press a key. So death_check
# checks if the game_over flag is set, and if it is, it calls the event "Wait for event and then store that event, so we can refer to it".
# With "press any key to exit," it wont be long before the user presses a key. At that point, event will be a KEYDOWN event, which will set
# self.running to False, triggering a program close. This just allows the user to observe their score and show to their friends. 
    def death_check(self):
        if self.game_over:
            event = pygame.event.wait()
            if event.type == pygame.KEYDOWN:
                self.running = False
            else:
                self.death_check()

# The run function just organizes things. death_check was the very last function built. Originally the work flow was check and handle user events, update the field
# and then draw it. Now death_check sets a conditional branch: If its gameover, we're going to handle rendering, drawing, AND user input differently than before.   
# The final command self.clock.tick(60),  sets the fps at 60 fps.
    def run(self):
        while self.running:
            self.death_check()
            self.event_handler()
            self.update()
            self.draw()

            self.clock.tick(60)

