import pygame
from settings import *

class Tree():
    def __init__(self, position, color):
        self.position = position
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.position[0], self.position[1], BLOCK_SIZE, BLOCK_SIZE))

    def destroy(self):
        trees.remove(self)