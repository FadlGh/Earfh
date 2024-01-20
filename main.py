import pygame
import sys
from enviroment import *
from settings import *
from predator import *
from prey import *
from tree import * 

pygame.init()

SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Earfh")

clock = pygame.time.Clock()

e = Enviroment(SCREEN)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    e.update()

    pygame.display.flip()

    clock.tick(FPS)
