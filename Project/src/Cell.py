import variables as var

from Globals import BattleShip, pygame


class Cell:
    """Класс Клетка

    Экземпляром класса является клетка игрового поля

    """
    def __init__(self, x, y, player):
        self.display = BattleShip
        self.player = player
        self.status = '0'
        self.x = x
        self.y = y
        self.hit = 0
        self.ship = 0
        self.height = var.cell_height
        self.wight = var.cell_wight
        self.active_colour = var.cell_active_colour
        self.inactive_colour = var.cell_inactive_colour

    def draw(self, x, y, player):
        """Рисует клетку в нужном цвете в зависимости от статуса игры и того, есть ли на ней корабль"""
        coord = None
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] <= x + self.wight and y < mouse[1] <= y + self.height:

            self.display.blit(pygame.image.load(var.cell_BLUE_path), (x, y))
            coord = [[self.x, self.y], 1] if click[0] else [[self.x, self.y], 0]

        if self.player == player:

            if self.status == 'ship':
                self.display.blit(pygame.image.load(var.cell_BLUE_path), (x, y))
            elif self.status == 'hit':
                self.display.blit(pygame.image.load(var.cell_MIST_path), (x, y))
            elif self.status == 'ship_hit':
                self.display.blit(pygame.image.load(var.cell_RED_path), (x, y))

        elif self.player != player:

            if self.status == 'hit':
                self.display.blit(pygame.image.load(var.cell_MIST_path), (x, y))
            elif self.status == 'ship_hit':
                self.display.blit(pygame.image.load(var.cell_RED_CROSS_path), (x, y))

        pygame.draw.rect(self.display, self.inactive_colour, (x, y, self.wight, self.height), var.frame_wight)
        return coord
