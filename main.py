import pygame
import sys
from settings import *
from predator import *
from prey import *

pygame.init()

SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Grid Simulation")

clock = pygame.time.Clock()


def draw_grid():
    for x in range(0, WINDOW_WIDTH, BLOCK_SIZE):
        for y in range(0, WINDOW_HEIGHT, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, BLACK, rect, 1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    SCREEN.fill(WHITE)
    draw_grid()
    
    p = Predator((200, 200), 1, RED)
    p.draw(SCREEN)

    pre = Prey((300, 200), 1, GREEN)
    pre.draw(SCREEN)

    pygame.display.flip()

    clock.tick(fps)
