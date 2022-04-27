import pygame
from Globals import main_font, BattleShip
import sys


def next_situation(fild_now, fild_1, fild_2):
    pass


def print_txt(message, x, y, font_type=main_font, font_color=(0, 0, 0), font_size=26, condition=False, dspl=BattleShip):
    font_type = pygame.font.Font(font_type, font_size)
    txt = font_type.render(message, True, font_color)
    dspl.blit(txt, (x, y))


def change_fild(fild_now, fild_1, fild_2):
    if fild_now == fild_1:
        return fild_2
    else:
        return fild_1


def true_function():
    return True


def stop_screen():
    from Globals import change_button
    process = True
    while process:
        BattleShip.fill((0, 0, 0))
        if change_button.draw(740, 375, 'To Battle!', true_function):
            process = False
        pygame.display.update()  # обновляет дисплей
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                sys.exit()
