import pygame

class Snake():
    def __init__(self, width, height):
        self.body = [(width//2, height//2), (width//2, height//2+1), (width//2, height//2+2)]
        self.direction = (0, 0)

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
