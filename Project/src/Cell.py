from Fild import Fild
import pygame
import assets


class Cell(Fild):
    def __init__(self, x, y, fild):
        Fild.__init__(self, fild.start_x, fild.start_y, fild.player, fild.game)

        """
        status: 
        0 - клетка свободна 
        1 - рядом с клеткой корабль
        2 - рядом с клеткой два корабля
        3 - рядом с клеткой три корабля
        4 - рядом с клектой четыре корабля
        5 - на клетке корабль
        6 - на клетке уничтоженный корабль
        7 - промах
        """

        self.x = x
        self.y = y
        self.status = -1

    def draw(self):
        if self.status == 6:
            self.project_name.blit(pygame.image.load('assets/BLUE_CROSS.png'), (self.x, self.y))
        elif self.status == 7:
            self.project_name.blit(pygame.image.load('assets/MIST.png'), (self.x, self.y))
