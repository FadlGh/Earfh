import pygame
import random
from settings import *
from predator import *
from prey import *
from tree import *

class Enviroment:
    def __init__(self, screen):
        self.screen = screen
        self.delay_timers = {}
        
        for i in range(TREE_COUNT):
            trees.append(Tree([random.randint(0, WINDOW_WIDTH / BLOCK_SIZE) * BLOCK_SIZE, random.randint(0, WINDOW_HEIGHT / BLOCK_SIZE) * BLOCK_SIZE], DARK_GREEN))

        for j in range(PREY_COUNT):
            preys.append(Prey([random.randint(0, WINDOW_WIDTH / BLOCK_SIZE) * BLOCK_SIZE, random.randint(0, WINDOW_HEIGHT / BLOCK_SIZE) * BLOCK_SIZE], BLOCK_SIZE, GREEN, 10))
        
        for k in range(PREDATOR_COUNT):
            predators.append(Predator([random.randint(0, WINDOW_WIDTH / BLOCK_SIZE) * BLOCK_SIZE, random.randint(0, WINDOW_HEIGHT / BLOCK_SIZE) * BLOCK_SIZE], BLOCK_SIZE, RED, 10))

    def draw_grid(self):
        for x in range(0, WINDOW_WIDTH, BLOCK_SIZE):
            for y in range(0, WINDOW_HEIGHT, BLOCK_SIZE):
                rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
                pygame.draw.rect(self.screen, BLACK, rect, 1)

    def delay(self, action_name, delay_duration):
        current_time = pygame.time.get_ticks()
        if action_name not in self.delay_timers:
            self.delay_timers[action_name] = current_time

        if current_time - self.delay_timers[action_name] >= delay_duration:
            # Add to a dictionary the name of the timer or update its time
            self.delay_timers[action_name] = current_time
            return True
        
        return False

    def update(self):
        self.screen.fill(WHITE)
        self.draw_grid()

        for prey in preys:
            prey.update(self.screen)

        for predator in predators:
            predator.update(self.screen)
        
        for tree in trees:
            tree.draw(self.screen)

        if self.delay("tree", 10000):
            trees.append(Tree([random.randint(0, WINDOW_WIDTH / BLOCK_SIZE) * BLOCK_SIZE, random.randint(0, WINDOW_HEIGHT / BLOCK_SIZE) * BLOCK_SIZE], DARK_GREEN))
