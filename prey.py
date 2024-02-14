import pygame
from settings import *
from entity import *

class Prey(Entity):
    def __init__(self, position, speed, color):
        super().__init__(position, speed, color)
        self.food = trees
        self.mates = preys

    def destroy(self):
        preys.remove(self)

    def spawn(self, pos):
        preys.append(Prey(pos, BLOCK_SIZE, GREEN))
        

