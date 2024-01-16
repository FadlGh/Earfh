import pygame
from settings import *
from entity import *

class Predator(Entity):
    def __init__(self, position, speed, color):
        super().__init__(position, speed, color)
        self.interactions = preys

    def destroy(self):
        predators.remove(self)

