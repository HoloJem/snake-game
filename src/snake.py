import pygame
from game_object import GameObject
import time
from settings import SEGMENT_SIZE, OBJECT_COLOR

class Snake(GameObject):
    def __init__(self, x, y):
        
        super().__init__(x,y,SEGMENT_SIZE,SEGMENT_SIZE,OBJECT_COLOR)
        self.direction = 'right'
        self.last_movement_time=time.time()
        self.movement_delay=0.2
        self.body = [
            (x,y),
            (x-SEGMENT_SIZE,y),
            (x-2*SEGMENT_SIZE,y)
        ]
        self.growth=False
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
    def update(self):
        if time.time() - self.last_movement_time < self.movement_delay:
            return
        self.last_movement_time=time.time()
        self.move()
        if self.growth:
            self.growth = False
        else:
            self.body.pop()
    def head_as_rect(self):
        return pygame.Rect(self.body[0][0], self.body[0][1], SEGMENT_SIZE, SEGMENT_SIZE)
    def change_direction(self, direction):
        self.direction = direction
    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, OBJECT_COLOR, (segment[0],segment[1],50,50))
    def collide_self(self):
        return self.body[0] in self.body[1:]
    def grow(self):
        self.growth=True