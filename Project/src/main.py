import time
from Global import *
from Fild import Fild
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
            not_player_fild_.destroyed_cells.append(cell)
        else:
            cell.status = 7
            not_player_fild_.destroyed_cells.append(cell)
            return draw_swap(player_fild_, fild_1_, fild_2_)
    return player_fild_


player_flag = 1
while process:
    pygame.time.delay(50)  # частота обновлений цикла
    for event in pygame.event.get():  # перебираем события
        if event.type == pygame.QUIT:
            process = False  # Если мы нажали на кнопочку закрыть, то мы выходим из приложения
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Нажата кнопка: ", event.button)

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
    elif len(fild_1.destroyed_cells) < 20 and len(fild_2.destroyed_cells) < 20:
        player_fild = continue_game(keys, player_fild, fild_1, fild_2)

    pygame.display.update()  # обновляет дисплей

pygame.quit()  # 100% закрытие программы
