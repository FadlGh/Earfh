import pygame
from settings import *

class Entity:
    def __init__(self, position):
        self.states = ["resting", "moving", "reproducing"]
        self.current_state = "moving"
        self.position = position

    def switch_state(self, new_state):
        if new_state not in self.states:
            raise ValueError(f"Invalid state: {new_state}")
        self.current_state = new_state