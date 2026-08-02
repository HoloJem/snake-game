import pygame
import random

from snake import Snake
from wall import Wall
from fruit import Fruit

from settings import SCREEN_WIDTH, SCREEN_HEIGHT, SEGMENT_SIZE, random_color

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
        self.snake = Snake(150,150)



    def create_walls(self):
        for x in range(0, SCREEN_WIDTH, SEGMENT_SIZE):
            self.walls.append(Wall(x,0,SEGMENT_SIZE,SEGMENT_SIZE))
            self.walls.append(Wall(x,SCREEN_HEIGHT-SEGMENT_SIZE,SEGMENT_SIZE,SEGMENT_SIZE))

        for y in range(0, SCREEN_HEIGHT, SEGMENT_SIZE):
            self.walls.append(Wall(0,y,SEGMENT_SIZE,SEGMENT_SIZE))
            self.walls.append(Wall(SCREEN_WIDTH-SEGMENT_SIZE, y, SEGMENT_SIZE, SEGMENT_SIZE))
    
    def spawn_fruit(self):
        x = random.randrange(SEGMENT_SIZE, SCREEN_WIDTH-SEGMENT_SIZE, SEGMENT_SIZE)
        y = random.randrange(SEGMENT_SIZE, SCREEN_HEIGHT-SEGMENT_SIZE, SEGMENT_SIZE)
        self.fruit = Fruit(x,y)

    def show_score(self):
        text = self.font.render(f"Score: {self.score}",True,self.score_color)
        self.screen.blit(text,(10,10))
        

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


    def update(self):
        if self.snake.collide_self():
            self.game_over=True
        for wall in self.walls:
            if self.snake.head_as_rect().colliderect(wall.rect):
                self.game_over=True
        if self.snake.head_as_rect().colliderect(self.fruit.rect):
            self.snake.grow()
            self.score += 1
            self.spawn_fruit()
        else: 
            self.snake.update()

    def draw(self):
        if self.game_over:
            self.show_game_over()
        else:
            self.screen.fill((0,0,0))
            self.snake.draw(self.screen)

            for wall in self.walls:
                wall.draw(self.screen)

            self.fruit.draw(self.screen)

            self.show_score()

        pygame.display.flip()

    def show_game_over(self):
        self.screen.fill((0,0,0))
        self.screen.blit(self.tombstone, (233,0))
        score_text = self.smallfont.render(f"Your high score was {self.score}", True, (0,0,0))
        thanks_text = self.smallfont.render(f"Thank you for playing my game.", True, (0,0,0))
        quit_text = self.smallfont.render(f"Press any key to exit.", True, (0,0,0))
        self.screen.blit(score_text, (355, 325))
        self.screen.blit(thanks_text, (355, 350))
        self.screen.blit(quit_text, (355, 375))

    def death_check(self):
        if self.game_over:
            event = pygame.event.wait()
            if event.type == pygame.KEYDOWN:
                self.running = False

            
    def run(self):
        while self.running:
            self.death_check()
            self.event_handler()
            self.update()
            self.draw()
            self.clock.tick(60)

