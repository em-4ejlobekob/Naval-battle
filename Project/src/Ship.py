import pygame
from Globals import *


class Ship:

    def __init__(self, x, y, size, rotation):
        self.display = BattleShip
        self.size = size
        self.x, self.y = x, y
        self.hits = []
        self.cells = []
        self.rotation = rotation

        if self.rotation == 'H':
            self.dx, self.dy = 1, 0
        else:
            self.dx, self.dy = 0, 1

    # def test(self)

    def draw(self, fild_x, fild_y):
        a, b = fild_x + 39 * (self.x - 1), fild_y + 39 * (self.y - 1)
        for j in range(self.size):

            if self.dx * (self.x + j) + self.dy * (self.y + j) <= 10 and [self.x + j, self.y + j] not in self.hits:
                self.display.blit(pygame.image.load('assets/BLUE.png'), (a, b))
            else:
                self.display.blit(pygame.image.load('assets/RED.png'), (a, b))

            if self.rotation == 'H':
                a += 39
            else:
                b += 39
