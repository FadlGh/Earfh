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

    def spawn(self):
        print("d")
        predators.append(Predator([random.randint(0, WINDOW_WIDTH / BLOCK_SIZE) * BLOCK_SIZE, random.randint(0, WINDOW_HEIGHT / BLOCK_SIZE) * BLOCK_SIZE], BLOCK_SIZE, RED))
