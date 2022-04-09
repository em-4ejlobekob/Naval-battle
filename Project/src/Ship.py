from Global import *
from Fild import Fild


class Ship(Fild):

    def __init__(self, x, y, fild):
        Fild.__init__(self, fild.start_x, fild.start_y, fild.player, fild.game)

        self.fild_cells = fild.fild_cells
        self.ship_collection = fild.ship_collection
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
            self.cells.append([self.x, self.y])

    def test(self):
        x = (self.x - self.start_x - x_def) // width + 1
        y = (self.y - self.start_y - y_def) // height + 1
        # print(x, y)
        if self.dx:
            x_test, y_test = self.size + 2, 3
        else:
            x_test, y_test = 3, self.size + 2
        # print(self.fild_cells, x_test, y_test)
        for i in range(x, x + x_test, 1):
            for j in range(y, y + y_test, 1):
                # print(i, j)
                if [i, j] in self.fild_cells or self.dx * x + self.dy * y + self.size > 10:
                    return False
        if self.ship_collection[-1]:
            return True
        else:
            return False

    def draw(self):
        a, b = self.x, self.y
        for j in range(self.size):
            x = (a - self.start_x - x_def) // width + 1
            y = (b - self.start_y - y_def) // height + 1
            # print(x, y, self.dx, self.dy)
            if self.dx * x + self.dy * y < 10:
                self.project_name.blit(pygame.image.load('assets/BLUE.png'), (a, b))
            else:
                self.project_name.blit(pygame.image.load('assets/RED.png'), (a, b))

            if self.rotation == 'H':
                a += width
            else:
                b += height

    def delete(self):
        pass
