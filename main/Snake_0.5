import pygame
import sys
import random

class Snake():
    def __init__(self, width, height):
        self.body = [(6, 6), (6, 7), (6,8)]
        self.direction = (0,0)

    def draw(self, screen, GRID_SIZE):
        for i, segment in enumerate(self.body):
            if i == 0:  # La cabeza de la serpiente
                pygame.draw.rect(screen, (0, 0, 0), (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
            else:  # El cuerpo de la serpiente
                pygame.draw.rect(screen, (100, 100, 100), (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    def mov(self):
        if self.direction != (0,0):
            head = (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1])
            self.body.insert(0, head)
            self.body.pop()

    def limites(self):
        head_x, head_y = self.body[0]
        if (head_x<0 or head_x>12) or (head_y<0 or head_y>12):
            return True

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
        pygame.draw.rect(screen, (255, 0, 0), (self.position[0] * GRID_SIZE, self.position[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))




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
                game_over=True
            
            if snake.body[0] == apple.position:
                snake.body.append(snake.body[-1])
                apple.respawn()

        draw_objects(snake)
        apple.draw(screen, GRID_SIZE)

        if game_over:
            screen.blit(game_over_text, game_over_rect)

        pygame.display.flip()
        clock.tick(10)

        

main()
