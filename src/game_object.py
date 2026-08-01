import pygame

#GameObject is a base class that all objects, meaning.. the Snake, the walls, the fruit bonuses share: A location, a size, and a color. 
#A rect is also constructed so we have access to pygame's built in collision detection.
class GameObject:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(
            self.x,
            self.y,
            self.width,
            self.height
        )

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def collide_with(self, other):
        return self.rect.colliderect(other.rect)
    