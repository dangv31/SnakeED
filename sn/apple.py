import pygame
import random

class Apple():
    def __init__(self, width, height):
        self.grid_width = width
        self.grid_height = height
        self.position = self.generate_position_inicial()

    def generate_position(self):
        x = random.randint(0, self.grid_width - 1)
        y = random.randint(0, self.grid_height - 1)
        return (x, y)

    def respawn(self):
        self.position = self.generate_position()

    def generate_position_inicial(self):
        x = 9
        y = 3
        return (x, y)

    def draw(self, screen, GRID_SIZE):
        pygame.draw.rect(screen, (255, 0, 0),
                         (self.position[0] * GRID_SIZE, self.position[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))