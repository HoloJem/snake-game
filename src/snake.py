import pygame
from game_object import GameObject

class Snake(GameObject):
    def __init__(self, x, y):
        super().__init__(x,y,50,50,(255,255,255))
        self.speed = 5
        self.direction = 'right'
    def update(self):
        if self.direction == 'right':
            self.x += self.speed
        elif self.direction == 'left':
            self.x -= self.speed
        elif self.direction == 'up':
            self.y -= self.speed
        elif self.direction == 'down':
            self.y += self.speed

