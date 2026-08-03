import pygame

# GameObject is a base class that all objects, meaning.. the Snake, the walls, the fruit bonuses share: A location, a size, and a color. 
# A rect is also constructed so we have access to pygame's built in collision detection, and the Rect class's built in draw function too.

# x and y coordinates represent the object's location.
# height and width represent the height and width.
# color represents the color of the object to be displayed.
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

# the draw function, for general use.
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

# the collide_with function. Can be used to check if two rectangle objects collide with each other.
    def collide_with(self, other):
        return self.rect.colliderect(other.rect)
    