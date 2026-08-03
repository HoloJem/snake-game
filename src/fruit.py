# We import pygame, GameObject parent class, and some constants from settings.
from settings import SEGMENT_SIZE, random_color
from game_object import GameObject
import pygame

#The Fruit Class. Imports but does not run the random_color() function until item initilization. Then fruit is always an exciting color.
class Fruit(GameObject):
    def __init__(self,x,y):
        super().__init__(x, y, SEGMENT_SIZE, SEGMENT_SIZE, random_color())

    def draw(self,screen):
        pygame.draw.rect(screen,self.color,(self.x, self.y, SEGMENT_SIZE, SEGMENT_SIZE))