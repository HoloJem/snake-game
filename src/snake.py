import pygame
from game_object import GameObject

class Snake(GameObject):
    def __init__(self, x, y):
        super().__init__(x,y,50,50,(255,255,255))

