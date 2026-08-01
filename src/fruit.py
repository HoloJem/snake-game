from settings import SEGMENT_SIZE, FRUIT_COLOR
from game_object import GameObject
import pygame

class Fruit(GameObject):
    def __init__(self,x,y):
        super().__init__(x, y, SEGMENT_SIZE, SEGMENT_SIZE, FRUIT_COLOR)

    def draw(self,screen):
        pygame.draw.rect(screen,FRUIT_COLOR,(self.x, self.y, SEGMENT_SIZE, SEGMENT_SIZE))