import pygame

from sn.apple import Apple
from sn.snake import Snake

pygame.init()

WIDTH, HEIGHT = 520, 520
GRID_SIZE = 40
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
font = pygame.font.Font(None, 36)
game_over_text = font.render("Perdiste", True, (255, 0, 0))
game_over_rect = game_over_text.get_rect(center=(260,150))

def draw_objects(snake):
    screen.fill((255, 255, 255))
    for x in range(GRID_WIDTH):
        pygame.draw.line(screen, (0, 0, 0), (x * GRID_SIZE, 0), (x * GRID_SIZE, HEIGHT))
    for y in range(GRID_HEIGHT):
        pygame.draw.line(screen, (0, 0, 0), (0, y * GRID_SIZE), (WIDTH, y * GRID_SIZE))

    snake.draw(screen, GRID_SIZE)

def main():
    snake = Snake(GRID_WIDTH, GRID_HEIGHT)
    apple = Apple(GRID_WIDTH, GRID_HEIGHT)
    clock = pygame.time.Clock()
    game_over=False
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
        if not game_over:
            snake.mov()
            if snake.limites():
                game_over = True

            if snake.body[0] == apple.position:
                snake.body.append(snake.body[-1])
                apple.respawn()
        draw_objects(snake)
        apple.draw(screen, GRID_SIZE)
        if game_over:
            screen.blit(game_over_text, game_over_rect)
        clock.tick(10)
        pygame.display.update()
main()