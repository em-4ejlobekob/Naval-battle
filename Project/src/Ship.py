from Global import *
from Fild import Fild


class Ship(Fild):

    def __init__(self, x_, y_, fild):
        Fild.__init__(self, fild.start_x, fild.start_y, fild.player, fild.game)

        self.fild_cells = fild.fild_cells
        self.ship_collection = fild.ship_collection
        self.size = fild.size_of_ship_now
        self.rotation = fild.rotation
        self.x, self.y = x_, y_
        self.hits = []
        self.cells = []

        if self.rotation == 'H':
            self.dx, self.dy = 1, 0
        else:
            self.dx, self.dy = 0, 1

        a_, b_ = self.x, self.y
        for i in range(self.size):
            x_ = (a_ - self.start_x - x_def) // width + 1
            y_ = (b_ - self.start_y - y_def) // height + 1
            self.cells.append([x_ + 1, y_ + 1])
            if self.rotation == 'H':
                a_ += width
            else:
                b_ += height

    def test(self):
        x_ = (self.x - self.start_x - x_def) // width + 1
        y_ = (self.y - self.start_y - y_def) // height + 1
        if self.dx:
            x_test, y_test = self.size + 2, 3
        else:
            x_test, y_test = 3, self.size + 2
        for i in range(x_, x_ + x_test, 1):
            for j in range(y_, y_ + y_test, 1):
                if [i, j] in self.fild_cells or self.dx * x_ + self.dy * y_ + self.size > 10:
                    return False
        if self.ship_collection[-1]:
            return True
        else:
            return False

    def draw(self):
        a_, b_ = self.x, self.y
        for j in range(self.size):
            x_ = (a_ - self.start_x - x_def) // width + 1
            y_ = (b_ - self.start_y - y_def) // height + 1
            if self.dx * x_ + self.dy * y_ < 10 and [x_ + 1, y_ + 1] not in self.hits:
                self.project_name.blit(pygame.image.load('assets/BLUE.png'), (a_, b_))
            else:
                self.project_name.blit(pygame.image.load('assets/RED.png'), (a_, b_))

            if self.rotation == 'H':
                a_ += width
            else:
                b_ += height

    def delete(self):
        pass
