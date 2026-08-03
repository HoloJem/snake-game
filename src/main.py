# The master class, main. Imports pygame. and Game.
import pygame
from game import Game

#We start pygame, initialize a new instance of Game() and run it. When the cycle completes, pygame.quit is ran. Simple.

pygame.init()

game = Game()

game.run()

pygame.quit()


