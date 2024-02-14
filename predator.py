import pygame
from settings import *
from entity import *

class Predator(Entity):
    def __init__(self, position, speed, color):
        super().__init__(position, speed, color)
        self.food = preys
        self.mates = predators

    def destroy(self):
        predators.remove(self)

    def spawn(self, pos):
        predators.append(Predator(pos, BLOCK_SIZE, GREEN))