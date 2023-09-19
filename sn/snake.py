import pygame

class Snake():
    def __init__(self, width, height):
        self.body = [(width//2, height//2), (width//2, height//2+1), (width//2, height//2+2)]
        self.direction = (0, 0)

    def draw(self, screen, GRID_SIZE):
        for cuerpo in self.body:
            pygame.draw.rect(screen, (0, 117, 227),(cuerpo[0]*GRID_SIZE, cuerpo[1]*GRID_SIZE, GRID_SIZE, GRID_SIZE))

    def mov(self):
        head = (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1])
        self.body.insert(0, head)
        self.body.pop()


