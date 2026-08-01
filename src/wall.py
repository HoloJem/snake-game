from game_object import GameObject
import pygame

class Wall(GameObject):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, (255,255,255))

    def draw(self,screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
