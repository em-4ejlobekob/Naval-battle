import variables as var

from Globals import BattleShip, pygame


class Ship:
    """Класс Корабль

    Основная задача класса рисовать во время расстановки кораблей выбранный корабль на поле

    """
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

    def draw(self, fild_x, fild_y):
        """Рисует корабль на поле во время расстановке кораблей"""
        a, b = fild_x + var.cell_wight * (self.x - 1), fild_y + var.cell_height * (self.y - 1)
        for j in range(self.size):

            if self.dx * (self.x + j) + self.dy * (self.y + j) <= var.fild_size and \
                    [self.x + j, self.y + j] not in self.hits:
                self.display.blit(pygame.image.load(var.cell_BLUE_path), (a, b))
            else:
                self.display.blit(pygame.image.load(var.cell_RED_path), (a, b))

            if self.rotation == 'H':
                a += var.cell_wight
            else:
                b += var.cell_height
