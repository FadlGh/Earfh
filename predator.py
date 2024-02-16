import pygame
from settings import *
from entity import *

class Predator(Entity):
    def __init__(self, position, speed, color, energy):
        super().__init__(position, speed, color, energy)
        self.food = preys
        self.mates = predators

    def destroy(self):
        predators.remove(self)

    def spawn(self):
        x = random.randint(0, 10)
        
        if x % 2 == 0:
            predators.append(Predator([random.randint(0, WINDOW_WIDTH / BLOCK_SIZE) * BLOCK_SIZE, random.randint(0, WINDOW_HEIGHT / BLOCK_SIZE) * BLOCK_SIZE], BLOCK_SIZE, RED, 10))
