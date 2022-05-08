import buttons as bt
import init as i
import variables as var

from Fild import Fild
from Functions import print_control, laugh, true_function, stop_screen, change_fild, winner_screen
from Globals import BattleShip, pygame


def start_init():
    """Инициализирует стартовые параметры"""
    fild_1 = Fild(var.fild_1_x, var.fild_1_y, 1)
    fild_2 = Fild(var.fild_2_x, var.fild_2_y, 2)
    process = True
    fild_now = fild_1
    BattleShip.fill((0, 0, 0))
    bcg = pygame.image.load(var.doctor1_path)
    return fild_1, fild_2, fild_now, bcg, process


def draw_display(fild_now, fild_1, fild_2):
    """Рисует игровое поле во время игры"""
    BattleShip.fill((0, 0, 0))
    f1 = fild_1.draw(fild_now.player)
    f2 = fild_2.draw(fild_now.player)
    print_control()
    return f1, f2


def control(process, fild_now, fild_1, fild_2):
    """Отвечает за управление"""
    for event in pygame.event.get():  # перебираем события
        if event.type == pygame.QUIT:
            process = False  # Если мы нажали на кнопочку закрыть, то мы выходим из приложения
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                fild_now.change_rotation()
            elif event.button == 5:
                fild_now.next_ship()
            elif event.button == 4:
                fild_now.previous_ship()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                fild_1.to_menu()
            elif event.key == pygame.K_e:
                volume = pygame.mixer.music.get_volume()
                pygame.mixer.music.set_volume(volume + 0.125)  # WARNING!!!
            elif event.key == pygame.K_q:
                volume = pygame.mixer.music.get_volume()
                pygame.mixer.music.set_volume(volume - 0.125)  # WARNING!!!
            elif event.key == pygame.K_p:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
    return process, fild_now, fild_1, fild_2


def draw_menu(bcg, fild_1):
    """Рисует меню при запуске игры"""
    start_init()
    while fild_1.start == 0:
        for event_ in pygame.event.get():
            if event_.type == pygame.QUIT:
                pygame.quit()
                quit()
            BattleShip.blit(bcg, (0, 0))

        bt.start_button.draw(var.start_bttn_x, var.start_bttn_y, 'START LEGENDARY BATTLESHIP', fild_1.to_game)
        bt.doctor_button.draw(var.doctor_bttn_x, var.doctor_bttn_y, 'AXAXAXAXAXAXAXAXAXAXXAX', laugh)
        bt.quit_button.draw(var.quit_bttn_x, var.quit_bttn_y, 'NO, I AM AFRAID OF BIG SHIPS', quit)

        pygame.display.update()
        pygame.time.delay(50)
    return fild_1.start


def fild_1_change_func(f1, fild_now, fild_1, fild_2):
    """Меняет состояние первого поля в зависимости от действий игрока"""
    if (f1 == 'end_start' and fild_1.game == 'start') or (f1 == 'end_part'):
        if bt.next_button.draw(var.next_bttn_x, var.next_bttn_y, 'next player', true_function):
            stop_screen()
            fild_1.game = 'game' if f1 == 'end_part' else 'stop'
            if f1 == 'end_part':
                fild_1.game = 'game'
            else:
                fild_1.game = 'stop'
            fild_now = change_fild(fild_now, fild_1, fild_2)
            f1 = None
    return f1, fild_1, fild_now


def fild_2_change_func(f2, fild_now, fild_1, fild_2):
    """Меняет состояние первого и/или второго поля в зависимости от действий игрока"""
    if (f2 == 'end_start' and fild_2.game == 'start') or (f2 == 'end_part'):
        if bt.next_button.draw(var.next_bttn_x, var.next_bttn_y, 'next player', true_function):
            stop_screen()
            fild_2.game = 'game'
            if f2 != 'end_part':
                fild_1.game = 'game'
            fild_now = change_fild(fild_now, fild_1, fild_2)
            f2 = None
    return f2, fild_now, fild_1, fild_2


def winner(f1, f2, fild_1):
    """Выводит победителя"""
    if f1 == 'Good game':
        winner_screen('2', fild_1)

    if f2 == 'Good game':
        winner_screen('1', fild_1)


def menu():
    while i.fild_1.start == 0:
        i.fild_1, i.fild_2, i.fild_now, bcg, i.process = start_init()
        i.fild_1.start = draw_menu(bcg, i.fild_1)
    return i.fild_1, i.fild_2, i.fild_now, i.process


def game():
    while i.fild_1.start == 1:
        i.process, i.fild_now, i.fild_1, i.fild_2 = control(i.process, i.fild_now, i.fild_1, i.fild_2)
        f1, f2 = draw_display(i.fild_now, i.fild_1, i.fild_2)
        f1, i.fild_1, fild_now = fild_1_change_func(f1, i.fild_now, i.fild_1, i.fild_2)
        f2, i.fild_now, i.fild_1, i.fild_2 = fild_2_change_func(f2, fild_now, i.fild_1, i.fild_2)
        winner(f1, f2, i.fild_1)
        pygame.display.update()
    return i.fild_1
