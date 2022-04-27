from Globals import pygame, BattleShip
from Functions import print_txt


class Button:

    def __init__(self, wight, height):
        self.wight = wight
        self.height = height
        self.inactive_colour = (13, 162, 58,)
        self.active_colour = (23, 204, 58)
        self.display = BattleShip

    def draw(self, x, y, message, action=None, condition=False):

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x + self.wight and y < mouse[1] < y + self.height:
            pygame.draw.rect(self.display, self.active_colour, (x, y, self.wight, self.height))
            print_txt(message, x + 10, y + 10)
            if click[0] and action is not None:
                pygame.time.delay(200)
                return action()
            else:
                return None
        else:
            pygame.draw.rect(self.display, self.inactive_colour, (x, y, self.wight, self.height))
            print_txt(message, x + 10, y + 10, condition=True) if condition else print_txt(message, x + 10, y + 10)
