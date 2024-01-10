import pygame
from settings import *
import random

class Entity:
    def __init__(self, position, speed, color):
        self.states = ["resting", "moving", "reproducing"]
        self.current_state = "moving"
        self.position = position
        self.speed = speed
        self.color = color
        self.last_move_time = pygame.time.get_ticks()

    def switch_state(self, new_state):
        if new_state not in self.states:
            raise ValueError(f"Invalid state: {new_state}")
        self.current_state = new_state

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.position[0], self.position[1], BLOCK_SIZE, BLOCK_SIZE))

    def move(self):
        self.position[0] += self.speed * random.randint(-1, 1)
        self.position[1] += self.speed * random.randint(-1, 1)

    def delay(self, duration):
        current_time = pygame.time.get_ticks()
        time_elapsed_since_last_move = current_time - self.last_move_time

        return(time_elapsed_since_last_move >= duration)

    def update(self, screen):
        if self.current_state == "moving":
            if self.delay(1000):
                self.move()
                self.last_move_time = pygame.time.get_ticks() 


        self.draw(screen)