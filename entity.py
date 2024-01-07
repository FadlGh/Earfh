import pygame
from settings import *

class Entity:
    def __init__(self, position, speed, color):
        self.states = ["resting", "moving", "reproducing"]
        self.current_state = "moving"
        self.position = position
        self.speed = speed
        self.color = color

    def switch_state(self, new_state):
        if new_state not in self.states:
            raise ValueError(f"Invalid state: {new_state}")
        self.current_state = new_state

    def update(self):
        if self.current_state == "moving":
            self.position = (self.position[0], self.position[1])

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.position[0], self.position[1], BLOCK_SIZE, BLOCK_SIZE))