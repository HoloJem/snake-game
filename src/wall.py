#First we import pygame and GameObject, the parent class
from game_object import GameObject
from settings import OBJECT_COLOR
import pygame

#Walls are a relatively simple game object. 
class Wall(GameObject):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, OBJECT_COLOR)

