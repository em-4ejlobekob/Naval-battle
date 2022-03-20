from Game import Game
import pygame


class Field(Game):

    def __init__(self, x, y):
        Game.__init__(self)
        self.field_cells = []
        self.start_x = x
        self.start_y = y

    def draw(self):
        self.project_name.blit(pygame.image.load('FILD.png'), (self.start_x, self.start_y))

    def app(self, x, y, rotation, size):
        x = (x - self.start_x - 50) / 38
        y = (y - self.start_y - 36) / 38
        if rotation == 'H':
            for i in range(size):
                self.field_cells.append([x + i, y])
                self.status = 1
        else:
            for i in range(size):
                self.field_cells.append([x, y + i])
                self.status = 1
