import pygame
from Globals import *


class Cell:
    def __init__(self, x, y, player):
        self.display = BattleShip
        self.player = player
        self.status = '0'
        self.x = x
        self.y = y
        self.hit = 0
        self.ship = 0
        self.height = 39
        self.wight = 39
        self.active_colour = (23, 204, 58)
        self.inactive_colour = (13, 162, 58,)

    def draw(self, x, y, player):
        coord = None
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] <= x + self.wight and y < mouse[1] <= y + self.height:

            self.display.blit(pygame.image.load('assets/BLUE.png'), (x, y))
            coord = [[self.x, self.y], 1] if click[0] else [[self.x, self.y], 0]

        if self.player == player:

            if self.status == 'ship':
                self.display.blit(pygame.image.load('assets/BLUE.png'), (x, y))
            elif self.status == 'hit':
                self.display.blit(pygame.image.load('assets/MIST.png'), (x, y))
            elif self.status == 'ship_hit':
                self.display.blit(pygame.image.load('assets/RED.png'), (x, y))

        elif self.player != player:

            if self.status == 'hit':
                self.display.blit(pygame.image.load('assets/MIST.png'), (x, y))
            elif self.status == 'ship_hit':
                self.display.blit(pygame.image.load('assets/RED_CROSS.png'), (x, y))

        pygame.draw.rect(self.display, self.inactive_colour, (x, y, self.wight, self.height), 1)  # рисует рамку
        return coord
