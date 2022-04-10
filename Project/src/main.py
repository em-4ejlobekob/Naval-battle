import time


from Global import *
from Fild import Fild
from Fild import Button
from Ship import Ship
from Cell import Cell
import sys


a = []
process = True
fild_1 = Fild(fild_1_x, fild_1_y, 1, game)
fild_2 = Fild(fild_2_x, fild_2_y, 2, game)
fild_1.start_x, fild_1.start_y = fild_1_x, fild_1_y
fild_2.start_x, fild_2.start_y = fild_2_x, fild_2_y
player_fild = fild_1

x, y = x_def + fild_1_x, y_def + fild_1_y


def default():
    global BattleShip, game, a, fild_1, fild_2, fild_1_x, fild_1_y, fild_2_x, fild_2_y
    global width, height, speed, x, y, x_def, y_def, start_flag, player_fild
    BattleShip = pygame.display.set_mode((1600, 800))  # name of the window
    game = Game(BattleShip)
    pygame.display.set_caption("Battles")  # title of the window

    a = []
    fild_1_x, fild_1_y = 30, 30
    fild_2_x, fild_2_y = 790, 30
    width, height, speed = 38, 38, 38
    x_def, y_def = 50, 36
    start_flag = 0

    a = []
    fild_1 = Fild(fild_1_x, fild_1_y, 1, game)
    fild_2 = Fild(fild_2_x, fild_2_y, 2, game)
    fild_1.start_x, fild_1.start_y = fild_1_x, fild_1_y
    fild_2.start_x, fild_2.start_y = fild_2_x, fild_2_y
    player_fild = fild_1

    x, y = x_def + fild_1_x, y_def + fild_1_y


def draw_square(x_, y_):
    pygame.draw.rect(BattleShip, (64, 128, 255), (x_, y_, 36, 36), 4)  # рисует рамку


# !!!WARNING!!! DEBUG
def draw_ship_in_moment(fild):
    global x, y
    if fild.ship_collection[-1]:
        ship = Ship(x - 1, y - 1, fild)
        ship.draw()


def draw_window(player_fild_, fild_1_, fild_2_):
    global x, y
    BattleShip.fill((0, 0, 0))
    fild_1_.draw()
    fild_2_.draw()
    for i in a:
        if i.status == player_fild_.player:
            i.draw()
    draw_ship_in_moment(player_fild_)
    draw_square(x, y)
    '''
    Статус отвечает за то, какие объекты в данный момент отрисовываются
    Это сделано для того, чтобы игрок не видел корабли противника
    Попадания и промахи отрисовываются методом draw для fild_1 и fild_2
    '''


# !!!WARNING!!! DEBUG
def draw_swap(player_fild_: Fild, fild_1_: Fild, fild_2_: Fild):
    global x, y
    while True:
        BattleShip.fill((0, 0, 0))
        f = pygame.font.Font(None, 100)
        text = f.render('Очередь другого игрока, нажмите "N"', True, (255, 255, 255))
        BattleShip.blit(text, (10, 50))
        pygame.display.update()  # обновляет дисплей
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                sys.exit()
            elif i.type == pygame.KEYDOWN and i.key == pygame.K_n:
                if player_fild_.player == 2:
                    x, y = x_def + fild_1_x, y_def + fild_1_y
                    return fild_1_
                else:
                    x, y = x_def + fild_2_x, y_def + fild_2_y
                    return fild_2_


def cell_move(keys_, player_fild_: Fild):
    global x, y
    if keys_[pygame.K_LEFT] and x >= player_fild_.start_x + x_def + speed:
        x -= speed
    if keys_[pygame.K_RIGHT] and x <= 460 - width - speed + player_fild_.start_x:
        x += speed
    if keys_[pygame.K_UP] and y >= player_fild_.start_y + y_def + speed:
        y -= speed
    if keys_[pygame.K_DOWN] and y <= 446 - height - speed:
        y += speed


def start_game(keys_, player_fild_: Fild, fild_1_: Fild, fild_2_: Fild):
    global x, y
    if not player_fild_.ship_collection[-1]:
        return draw_swap(player_fild_, fild_1_, fild_2_)
    if keys_[pygame.K_c]:
        player_fild_.swap_rotation()
    if keys_[pygame.K_SPACE]:
        ship = Ship(x - 1, y - 1, player_fild_)
        if ship.test():
            ship.status = player_fild_.player  # Переделать тест так, чтобы он проверял все клетки вокруг
            a.append(ship)
            player_fild_.install_ship(x, y)
        time.sleep(0.1)

    cell_move(keys_, player_fild_)
    # print(player_fild_.player)  # пишет, какой игрок сейчас играет в выводе
    return player_fild_


# !!!WARNING!!! DEBUG
def continue_game(keys_, player_fild_: Fild, fild_1_: Fild, fild_2_: Fild):
    global x, y
    cell_move(keys_, player_fild_)
    if keys_[pygame.K_SPACE]:
        x_ = (x - player_fild_.start_x - x_def) // width + 1
        y_ = (y - player_fild_.start_y - y_def) // height + 1
        if player_fild_ == fild_1_:
            not_player_fild_ = fild_2_
        else:
            not_player_fild_ = fild_1_
        cell = Cell(x, y, not_player_fild_)
        if [x_, y_] in player_fild_.fild_cells:
            for i in a:
                if [x_, y_] in i.cells and i.status == not_player_fild_.player:
                    i.hits.append([x_, y_])
                    break
            cell.status = 6
            not_player_fild_.ships.add(cell)
            #print(len(not_player_fild_.ships))
            not_player_fild_.destroyed_cells.append(cell)
        else:
            cell.status = 7
            not_player_fild_.destroyed_cells.append(cell)
            return draw_swap(player_fild_, fild_1_, fild_2_)
    return player_fild_


laugh_sound = pygame.mixer.Sound('assets/laugh.mp3')
bcg_music = pygame.mixer.Sound('assets/bcg.mp3')


def laugh():
    pygame.mixer.Sound.play(laugh_sound)
    pygame.time.delay(300)


def win_test():
    k1, k2 = 0, 0
    for i in a:
        if i.status == 1 and i.cells == i.hits:
            k1 += 1
    for i in a:
        if i.status == 1 and i.cells == i.hits:
            k1 += 1
    if k1 == 20 or k2 == 20:
        return False
    else:
        return True


def start_flag_change():
    print("Hello, Kolya!")
    global start_flag
    start_flag = 1
    pygame.mixer.pause()
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.Sound.play(bcg_music)


def draw_menu(image):
    BattleShip.fill((0, 0, 0))
    bcg = pygame.image.load(image)
    start_button = Button(210, 30, (70, 70, 70), (70, 75, 70), (70, 200, 70))
    doctor_button = Button(210, 30, (70, 70, 70), (70, 75, 70), (70, 200, 70))
    quit_button = Button(210, 30, (70, 70, 70), (70, 75, 70), (70, 200, 70))
    while start_flag == 0:
        for event_ in pygame.event.get():
            if event_.type == pygame.QUIT:
                 pygame.quit()
                 quit()
            BattleShip.blit(bcg, (0, 0))

        start_button.draw(30, 80, 'START LEGENDARY BATTLESHIP', start_flag_change)
        doctor_button.draw(30, 115, 'AXAXAXAXAXAXAXAXAXAXXAX', laugh)
        quit_button.draw(30,150, 'NO, I AM AFRAID OF BIG SHIPS', quit)

        pygame.display.update()
        pygame.time.delay(50)


player_flag = 1
while process:

    if start_flag == 0:
        default()
        draw_menu('assets/doctor.jpg')
    else:
        pygame.time.delay(50)  # частота обновлений цикла
        for event in pygame.event.get():  # перебираем события
            if event.type == pygame.QUIT:
                process = False  # Если мы нажали на кнопочку закрыть, то мы выходим из приложения
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print("Нажата кнопка: ", event.button)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                start_flag = 0
                pygame.mixer.pause()

        draw_window(player_fild, fild_1, fild_2)
        keys = pygame.key.get_pressed()  # список кнопок, которые сейчас нажимаются
        if fild_1.ship_collection[-1] or fild_2.ship_collection[-1]:
            player_fild = start_game(keys, player_fild, fild_1, fild_2)
        elif player_flag:
            zz = draw_swap(player_fild, fild_1, fild_2)
            player_fild = fild_1
            fild_1.player = 2
            fild_2.player = 1
            fild_1, fild_2 = fild_2, fild_1
            fild_1_x, fild_2_x = fild_2_x, fild_1_x
            fild_1_y, fild_2_y = fild_2_y, fild_1_y
            player_fild = draw_swap(player_fild, fild_1, fild_2)
            player_flag = 0
        elif len(fild_1.ships) < 20 and len(fild_2.ships) < 20:
            player_fild = continue_game(keys, player_fild, fild_1, fild_2)

        if len(fild_1.ships) == 20 or len(fild_2.ships) == 20:
            print(4)

        pygame.display.update()  # обновляет дисплей

pygame.quit()  # 100% закрытие программы
