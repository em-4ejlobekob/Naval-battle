import pygame

from variables import dspl_x, dspl_y


pygame.init()

BattleShip = pygame.display.set_mode((dspl_x, dspl_y))  # name of the window
fonts = ['assets/Fonts/font_1', 'assets/Fonts/font_2', 'assets/Fonts/font_3',
         'assets/Fonts/font_4', 'assets/Fonts/font_5']
main_font = fonts[0] + '.otf'

start_flag = 0
