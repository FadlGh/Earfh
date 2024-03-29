import pygame
from settings import *
import random
import math

class Entity:
    def __init__(self, position, speed, color, energy):
        self.states = ["resting", "moving"]
        self.current_state = "moving"
        self.position = position
        self.speed = speed
        self.color = color
        self.energy = energy
        self.delay_timers = {}
        self.food = []
        self.mates = []

    def switch_state(self, new_state):
        if new_state not in self.states:
            raise ValueError(f"Invalid state: {new_state}")
        self.current_state = new_state

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.position[0], self.position[1], BLOCK_SIZE, BLOCK_SIZE))

    def move(self):
        x = random.randint(-1, 1)
        y = random.randint(-1, 1)

        if self.position[0] + self.speed * x > WINDOW_WIDTH - BLOCK_SIZE:
            x = random.randint(-1, 0)
        elif self.position[0] + self.speed * x < 0:
            x = random.randint(0, 1)

        if self.position[1] + self.speed * y > WINDOW_HEIGHT - BLOCK_SIZE:
            y = random.randint(-1, 0)
        elif self.position[1] + self.speed * y < 0:
            y = random.randint(0, 1)

        self.position[0] += self.speed * x
        self.position[1] += self.speed * y

        self.energy -= 0.5


    def delay(self, action_name, delay_duration):
        current_time = pygame.time.get_ticks()
        if action_name not in self.delay_timers:
            self.delay_timers[action_name] = current_time

        if current_time - self.delay_timers[action_name] >= delay_duration:
            # Add to a dictionary the name of the timer or update its time
            self.delay_timers[action_name] = current_time
            return True
        
        return False
    
    def destroy(self):
        pass

    def spawn(self):
        pass

    def kill(self, interaction):
        self.position = interaction.position
        interaction.destroy()
        self.energy += 3

    def reproduce(self, interaction):
        interaction.spawn()

    def check_interaction(self, interactions):
        closest_interaction = min(interactions, key=lambda interaction: math.dist(self.position, interaction.position))
        distance_to_closest_interaction = math.dist(self.position, closest_interaction.position)
        if distance_to_closest_interaction <= math.hypot(BLOCK_SIZE + 0.1, BLOCK_SIZE + 0.1): 
            # Check the hypotenuse of a isoceles right triangle because distance may vary based on which of the 8 neighbouring blocks the interaction is 
            if closest_interaction in self.food:
                self.kill(closest_interaction)
            elif closest_interaction in self.mates:
                self.reproduce(closest_interaction)

    def update(self, screen):
        if self.energy < 1:
            self.destroy()

        if self.current_state == "moving" and self.delay("move", 1000):
            self.check_interaction(self.food)
            self.move()
        
        if self.delay("reproducing", 20000):
            self.check_interaction(self.mates)

        self.draw(screen)