import assets
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
        self.ships = set()

    def draw(self):
        self.project_name.blit(pygame.image.load('assets/FILD.png'), (self.start_x, self.start_y))
        for i in self.destroyed_cells:
            i.draw()

    def install_ship(self, x_, y_):
        x_ = (x_ - self.start_x - x_def) // width + 1
        y_ = (y_ - self.start_y - y_def) // height + 1
        print(x_, y_)
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


class Button:
    def __init__(self, width_, height_, color1, color2, color):
        self.width = width_
        self.height = height_
        self.color1 = color1
        self.color2 = color2
        self.color = color

    def draw(self, x, y, message, action):

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            pygame.draw.rect(BattleShip, self.color1, (x, y, self.width, self.height))
            if click[0] == 1:
                action()
                start_flag = 1

        else:
            pygame.draw.rect(BattleShip, self.color2, (x, y, self.width, self.height))

        font = pygame.font.Font(None, 18)
        text = font.render(message, True, self.color)
        BattleShip.blit(text, (x + 10, y + 10))
