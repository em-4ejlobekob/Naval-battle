from Global import *


class Fild(Game):

    def __init__(self, x_, y_, player, game_):
        Game.__init__(self, game_.project_name)

        self.game = game_
        self.fild_cells = []
        self.destroyed_cells = []
        self.player = player
        self.start_x = x_
        self.start_y = y_

        self.size_of_ship_now = 4
        self.ship_collection = [1, 2, 3, 4]
        self.ship_size = [4, 3, 2, 1]
        self.counter = 0
        self.rotation = 'H'

    def draw(self):
        self.project_name.blit(pygame.image.load('assets/FILD.png'), (self.start_x, self.start_y))
        for i in self.destroyed_cells:
            i.draw()

    def install_ship(self, x_, y_):
        x_ = (x_ - self.start_x - x_def) // width + 1
        y_ = (y_ - self.start_y - y_def) // height + 1
        for i in range(self.size_of_ship_now):
            if self.rotation == 'H':
                self.fild_cells.append([x_ + i, y_])
                # print('|', x + i, y, '|')
            else:
                self.fild_cells.append([x_, y_ + i])
                # print('|', x, y + i, '|')

        self.ship_collection[self.counter] -= 1
        # print(self.ship_collection, self.ship_size)
        if not self.ship_collection[self.counter] and self.counter < 3:
            self.counter += 1
            self.size_of_ship_now = self.ship_size[self.counter]

    def swap_rotation(self):
        if self.rotation == 'H':
            self.rotation = 'V'
        else:
            self.rotation = 'H'
