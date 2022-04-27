import pygame
pygame.init()

BattleShip = pygame.display.set_mode((1600, 800))  # name of the window
ships = [[4, 1], [3, 2], [2, 3], [1, 4]]
fonts = ['assets/Fonts/font_1', 'asserts/Fonts/font_2', 'asserts/Fonts/font_3',
         'asserts/Fonts/font_4', 'asserts/Fonts/font_5']
main_font = fonts[0] + '.otf'

from Button import Button
next_button = Button(150, 50)
change_button = Button(120, 50)
