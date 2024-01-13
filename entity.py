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
        self.delay_timers = {}

    def switch_state(self, new_state):
        if new_state not in self.states:
            raise ValueError(f"Invalid state: {new_state}")
        self.current_state = new_state

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.position[0], self.position[1], BLOCK_SIZE, BLOCK_SIZE))

    def move(self):
        x = random.randint(-1, 1)
        y = random.randint(-1, 1)

        if self.position[0] + self.speed * x > WINDOW_WIDTH:
            x = random.randint(-1, 0)
        elif self.position[0] + self.speed * x < 0:
            x = random.randint(0, 1)

        if self.position[1] + self.speed * y > WINDOW_HEIGHT:
            y = random.randint(-1, 0)
        elif self.position[1] + self.speed * y < 0:
            y = random.randint(0, 1)

        self.position[0] += self.speed * x
        self.position[1] += self.speed * y


    def delay(self, action_name, delay_duration):
        current_time = pygame.time.get_ticks()
        if action_name not in self.delay_timers or current_time - self.delay_timers[action_name] >= delay_duration:
            self.delay_timers[action_name] = current_time
            return True
        return False

    def update(self, screen):
        if self.current_state == "moving" and self.delay("move", 1000):
            self.move()

        self.draw(screen)