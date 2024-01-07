import pygame
from settings import *
from entity import *

class Prey(Entity):
    def __init__(self, position, speed, color):
        super().__init__(position, speed, color)
