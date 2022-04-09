from Field import Field
import pygame
from Cell import Cell
import assets


class Ship(Field):

    def __init__(self, size, rotation, x, y, field):
        Field.__init__(self, x, y)
        self.size = size
        self.rotation = rotation
        if rotation == 'H':
            self.dx = 1
            self.dy = 0
        else:
            self.dx = 0
            self.dy = 1
        self.x = x
        self.y = y
        self.hits = 0
        self.cells = []
        for i in range(0, size):
            self.cells.append([x, y, 1])

    def test(self):
        x = (self.x - self.start_x - 50) / 38
        y = (self.y - self.start_y - 36) / 38
        if self.dx * x + self.dy * y + self.size <= 10:
            return True
        else:
            return False

    def draw(self):
        a, b = self.x, self.y
        if self.rotation == 'H':
            for j in range(self.size):
                if self.cells[j][2]:
                    self.project_name.blit(pygame.image.load('assets/BLUE.png'), (a, b))
                else:
                    self.project_name.blit(pygame.image.load('assets/BLUE_CROSS.png'), (a, b))
                a += 38
        else:
            for j in range(self.size):
                if self.cells[j][2]:
                    self.project_name.blit(pygame.image.load('assets/BLUE.png'), (a, b))
                else:
                    self.project_name.blit(pygame.image.load('assets/BLUE_CROSS.png'), (a, b))
                b += 38
