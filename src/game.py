import pygame
import random

from snake import Snake
from wall import Wall
from fruit import Fruit

from settings import SCREEN_WIDTH, SCREEN_HEIGHT, SEGMENT_SIZE

class Game:
    def __init__(self):
        self.running = True
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        
        pygame.display.set_caption("Snake")
        
        self.clock = pygame.time.Clock()
        
        self.snake = Snake(150,150)

        self.walls = []

        self.create_walls()

        self.fruit = None
        self.spawn_fruit()

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
        if self.snake.collide_self:
            self.running=False
        for wall in self.walls:
            if self.snake.head_as_rect().colliderect(wall.rect):
                self.running=False
        if self.snake.head_as_rect().colliderect(self.fruit.rect):
            self.snake.grow()
            self.spawn_fruit()
        else: 
            self.snake.update()

    def draw(self):
        self.screen.fill((0,0,0))
        self.snake.draw(self.screen)

        for wall in self.walls:
            wall.draw(self.screen)

        self.fruit.draw(self.screen)

        pygame.display.flip()

    def run(self):
        while True:
            self.event_handler()
            self.update()
            self.draw()
            self.clock.tick(60)
