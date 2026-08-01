from snake import Snake
import pygame
from settings import SEGMENT_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT
from wall import Wall
import random
from fruit import Fruit


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake")

snake = Snake(150,150)

#generating the boundaries of the arena, the "walls".
walls = []

#first top and bottom wall generation. 
for x in range(0, SCREEN_WIDTH, SEGMENT_SIZE):
    walls.append(Wall(x, 0, SEGMENT_SIZE, SEGMENT_SIZE))
    walls.append(Wall(x, SCREEN_HEIGHT - SEGMENT_SIZE, SEGMENT_SIZE, SEGMENT_SIZE))

#then the left and right walls
for y in range(0, SCREEN_HEIGHT, SEGMENT_SIZE):
    walls.append(Wall(0, y, SEGMENT_SIZE, SEGMENT_SIZE))
    walls.append(Wall(SCREEN_WIDTH - SEGMENT_SIZE, y, SEGMENT_SIZE, SEGMENT_SIZE))


clock = pygame.time.Clock()
pygame.time.wait(1600)


running = True
fruit_exists = False
while running:
#INPUT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.change_direction('right')
            elif event.key == pygame.K_LEFT:
                snake.change_direction('left')
            elif event.key == pygame.K_UP:
                snake.change_direction('up')
            elif event.key == pygame.K_DOWN:
                snake.change_direction('down')
    if not fruit_exists :
        x = random.randrange(0+SEGMENT_SIZE,SCREEN_WIDTH-SEGMENT_SIZE,SEGMENT_SIZE)
        y = random.randrange(0+SEGMENT_SIZE,SCREEN_HEIGHT-SEGMENT_SIZE,SEGMENT_SIZE)
        fruit = Fruit(x,y)
        fruit_exists = True
    


#UPDATE
    screen.fill((0,0,0))
    if snake.head_as_rect().colliderect(fruit.rect):
        snake.grow()
        fruit_exists=False
    else:
        snake.update()
    for wall in walls:
        if snake.head_as_rect().colliderect(wall.rect):
            running = False
    snake.draw(screen)
    for wall in walls : 
        wall.draw(screen)
    fruit.draw(screen)
    if snake.collide_self():
        running = False
    
#DRAW    
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()

