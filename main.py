import pygame
from chessmate import *
from time import sleep

# Create class Cell
pygame.init()
print(RES_DIR)
window = pygame.display.set_mode((800, 600))
b = Board(window)

number = 1
for el in b.cells:
    print(str(number) + ':', el.position)
    number += 1

clock = pygame.time.Clock()
game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    clock.tick(40)
    b.update()
    pygame.display.update()
