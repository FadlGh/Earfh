import pygame
from settings import *
from entity import *

class Prey(Entity):
    def __init__(self, position, speed, color, energy):
        super().__init__(position, speed, color, energy)
        self.food = trees
        self.mates = preys

    def destroy(self):
        preys.remove(self)

    def spawn(self):
        x = random.randint(0, 10)

        if x % 2 == 0:
            preys.append(Prey([random.randint(0, WINDOW_WIDTH / BLOCK_SIZE) * BLOCK_SIZE, random.randint(0, WINDOW_HEIGHT / BLOCK_SIZE) * BLOCK_SIZE], BLOCK_SIZE, GREEN, 10))
