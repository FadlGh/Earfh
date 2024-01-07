import pygame
from settings import *
from entity import *

class Predator(Entity):
    def __init__(self):
        self.speed = 1
        self.color = RED
