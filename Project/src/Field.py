from Global import *


class Field(Game):

    def __init__(self, x, y, player, game_):
        Game.__init__(self, game_.project_name)

        self.game = game_
        self.field_cells = []
        self.player = player
        self.start_x = x
        self.start_y = y

        self.size_of_ship_now = 4
        self.ship_collection = [1, 2, 3, 4]
        self.ship_size = [4, 3, 2, 1]
        self.counter = 0
        self.rotation = 'H'

    def draw(self):
        self.project_name.blit(pygame.image.load('assets/FILD.png'), (self.start_x, self.start_y))

    def app(self, x, y, rotation, size):
        x = (x - self.start_x - x_def) / width
        y = (y - self.start_y - y_def) / height
        if rotation == 'H':
            for i in range(size):
                self.field_cells.append([x + i, y])
        else:
            for i in range(size):
                self.field_cells.append([x, y + i])

    def install_ship(self, x, y):
        x = (x - self.start_x - x_def) / width
        y = (y - self.start_y - y_def) / height
        if self.rotation == 'H':
            for i in range(self.size_of_ship_now):
                self.field_cells.append([x + i, y])
        else:
            for i in range(self.size_of_ship_now):
                self.field_cells.append([x, y + i])

        self.ship_collection[self.counter] -= 1
        if not self.ship_collection[self.counter] and self.counter < 3:
            self.counter += 1
            self.size_of_ship_now = self.ship_size[self.counter]

    def swap_rotation(self):
        if self.rotation == 'H':
            self.rotation = 'V'
        else:
            self.rotation = 'H'
