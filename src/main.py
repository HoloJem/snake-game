from snake import Snake
import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Snake")
snake = Snake(100,100)

clock = pygame.time.Clock()
pygame.time.wait(1600)


running = True
while running:
#INPUT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
#UPDATE
    screen.fill((0,0,0))
    snake.update()
    snake.draw(screen)

#DRAW    
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()

