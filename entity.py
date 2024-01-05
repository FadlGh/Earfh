import pygame
from settings import *

class Entity:
    def __init__(self, color, position):
        self.color = color
        self.states = ["idle", "reproduce"]
        self.current_state = "idle"
        self.position = position

    def switch_state(self, new_state):
        if new_state not in self.states:
            raise ValueError(f"Invalid state: {new_state}")
        self.current_state = new_state

    def update(self):
        # Common logic for all entities
        pass

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, BLOCK_SIZE)