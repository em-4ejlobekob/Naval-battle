from Global import *
from Field import Field


class Ship(Field):

    def __init__(self, x, y, fild):
        Field.__init__(self, fild.start_x, fild.start_y, fild.player, fild.game)

        self.size = fild.size_of_ship_now
        self.rotation = fild.rotation
        self.x, self.y = x, y
        self.hits = 0
        self.cells = []

        if self.rotation == 'H':
            self.dx, self.dy = 1, 0
        else:
            self.dx, self.dy = 0, 1

        for i in range(0, self.size):
            self.cells.append([self.x, self.y, 1])

    def test(self):
        x = (self.x - self.start_x - x_def) / width
        y = (self.y - self.start_y - y_def) / height
        if self.dx * x + self.dy * y + self.size <= 10:
            return True
        else:
            return False

    def draw(self):
        a, b = self.x, self.y
        for j in range(self.size):
            if self.cells[j][2]:
                self.project_name.blit(pygame.image.load('assets/BLUE.png'), (a, b))
            else:
                self.project_name.blit(pygame.image.load('assets/BLUE_CROSS.png'), (a, b))

            if self.rotation == 'H':
                a += width
            else:
                b += height
