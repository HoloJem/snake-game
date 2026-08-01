import pygame
from game_object import GameObject
import time

class Snake(GameObject):
    def __init__(self, x, y):
        self.color=(255,255,255)
        super().__init__(x,y,50,50,self.color)
        self.speed = 50
        self.direction = 'right'
        self.last_movement_time=time.time()
        self.movement_delay=0.2
        self.body = [
            (x,y),
            (x-50,y),
            (x-100,y)
        ]
    
    def update(self):
        if time.time() - self.last_movement_time < self.movement_delay:
            return

        self.last_movement_time=time.time()
         
        head_x, head_y = self.body[0]

        if self.direction == 'right':
            head_x += self.speed
        elif self.direction == 'left':
            head_x -= self.speed
        elif self.direction == 'up':
            head_y -= self.speed
        elif self.direction == 'down':
            head_y += self.speed
        
        self.body.insert(0,(head_x, head_y))
        self.body.pop()

    def change_direction(self, direction):
        self.direction = direction
    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, self.color, (segment[0],segment[1],50,50))
