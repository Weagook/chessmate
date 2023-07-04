import pygame
from chessmate import *

# Create class Cell
pygame.init()

window = pygame.display.set_mode((1280, 1024))
b = Board(window, (0, 0), (0, 0))