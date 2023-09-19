import pygame
import sys
import random

from sn.snake import Snake

pygame.init()

WIDTH, HEIGHT = 520, 520
GRID_SIZE = 40
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

def draw_objects(snake):
    screen.fill((24, 227, 0))
    for x in range(GRID_SIZE):
        if x%2 == 0:
            for y in range(GRID_SIZE):
                if y%2 == 0:
                    grass = pygame.Rect(x * GRID_SIZE,y*GRID_SIZE, GRID_SIZE,GRID_SIZE)
                    pygame.draw.rect(screen, (27, 255, 0), grass)
        else:
            for y in range(GRID_SIZE):
                if y%2 != 0:
                    grass = pygame.Rect(x * GRID_SIZE,y*GRID_SIZE, GRID_SIZE,GRID_SIZE)
                    pygame.draw.rect(screen, (27, 255, 0), grass)

    snake.draw(screen, GRID_SIZE)
def main():
    snake = Snake(GRID_WIDTH, GRID_HEIGHT)
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != (0, 1):
                    snake.direction = (0, -1)
                elif event.key == pygame.K_DOWN and snake.direction != (0, -1):
                    snake.direction = (0, 1)
                elif event.key == pygame.K_LEFT and snake.direction != (1, 0):
                    snake.direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and snake.direction != (-1, 0):
                    snake.direction = (1, 0)
        snake.mov()
        draw_objects(snake)
        clock.tick(10)

        pygame.display.flip()

main()