import sys
import buttons as bt
import variables as var

from Globals import main_font, BattleShip, pygame


def laugh():
    laugh_sound = pygame.mixer.Sound(var.laugh_path)
    pygame.mixer.Sound.play(laugh_sound)
    pygame.time.delay(300)


def print_txt(message, x, y, font_type=main_font, font_color=(0, 0, 0), font_size=var.print_font_size, dspl=BattleShip):
    """Выводит поданный текст в указанную область диплея"""
    font_type = pygame.font.Font(font_type, font_size)
    txt = font_type.render(message, True, font_color)
    dspl.blit(txt, (x, y))


def change_fild(fild_now, fild_1, fild_2):
    """Меняет активного игрока во время игры"""
    if fild_now == fild_1:
        return fild_2
    else:
        return fild_1


def true_function():
    """Возвращает True

    Класс Button принимает как дополнительный параметр функцию, и при нажатии на неё, вызывает поданную функцию,
    вызывает её и возвращает её return.

    """
    return True


def stop_screen():
    """Запускает перебивающую плашку"""
    process = True
    while process:
        BattleShip.fill((0, 0, 0))
        if bt.change_button.draw(var.change_bttn_x, var.change_bttn_y, 'To Battle!', true_function):
            process = False
        pygame.display.update()  # обновляет дисплей
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                sys.exit()


def winner_screen(player_number, fild):
    """Выводит победителя в конце игры и предлагает вернуться в меню"""
    win = pygame.image.load(var.doctor_path)
    winner_player = 'And the winner is Player' + player_number + '!'
    process = True
    while process:
        BattleShip.fill((0, 0, 0))
        BattleShip.blit(win, (var.win_x, var.win_y))
        print_txt(winner_player, var.winner_player_x, var.winner_player_y, main_font, var.cell_active_colour)
        if bt.menu_button.draw(var.menu_bttn_x, var.menu_bttn_y, 'To Menu', fild.to_menu):
            process = False
        pygame.display.update()  # обновляет дисплей
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                sys.exit()


def print_control():
    """Печатает инструкции управления"""
    for i in range(var.len_var_txt):
        print_txt(var.txt[i], var.control_start_x, var.control_start_y + var.indent * i,
                  font_color=var.white)
    print_txt('Esc - вернуться в меню', var.esc_x, var.esc_y, font_color=var.white)
