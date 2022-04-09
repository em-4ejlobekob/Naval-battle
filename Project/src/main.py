import time
from Global import *
from Fild import Fild
from Ship import Ship


a = []
process = True
fild_1 = Fild(fild_1_x, fild_1_y, 1, game)
fild_2 = Fild(fild_2_x, fild_2_y, 2, game)
fild_1.start_x, fild_1.start_y = fild_1_x, fild_1_y
fild_2.start_x, fild_2.start_y = fild_2_x, fild_2_y
player_fild = fild_1

x, y = x_def + fild_1_x, y_def + fild_1_y
main_x_fild, main_y_fild = x_def + fild_2_x, y_def + fild_2_y


def draw_square(x_, y_):
    pygame.draw.rect(BattleShip, (64, 128, 255), (x_, y_, 36, 36), 4)  # рисует рамку


# !!!WARNING!!! DEBUG
def draw_ship_in_moment(fild):
    global x, y
    if fild.ship_collection[-1]:
        ship = Ship(x - 1, y - 1, fild)
        ship.draw()


def draw_window(player_fild_, fild_1_, fild_2_):
    global a, x, y
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
def draw_swap(keys_, player_fild_: Fild, fild_1_: Fild, fild_2_: Fild):
    global x, y
    BattleShip.fill((0, 0, 0))
    f = pygame.font.Font(None, 100)
    text = f.render('Очередь другого игрока, нажмите "N"', True, (255, 255, 255))
    BattleShip.blit(text, (10, 50))
    pygame.display.update()  # обновляет дисплей
    if keys_[pygame.K_n]:
        if player_fild_.player == 2:
            x, y = x_def + fild_1_x, y_def + fild_1_y
            return fild_1_
        else:
            x, y = x_def + fild_2_x, y_def + fild_2_y
            return fild_2_
    else:
        return 3


def start_game(keys_, player_fild_: Fild, fild_1_: Fild, fild_2_: Fild):
    global a, x, y
    if not player_fild_.ship_collection[-1]:
        return draw_swap(keys_, player_fild_, fild_1_, fild_2_)
    if keys_[pygame.K_c]:
        player_fild_.swap_rotation()
    if keys_[pygame.K_SPACE]:
        ship = Ship(x - 1, y - 1, player_fild_)
        if ship.test():
            ship.status = player_fild_.player  # Переделать тест так, чтобы он проверял все клетки вокруг
            a.append(ship)
            player_fild_.install_ship(x, y)
        time.sleep(0.1)

    if keys_[pygame.K_LEFT] and x >= 50 + speed + fild_2_.start_x * (player_fild_.player - 1):
        x -= speed
    if keys_[pygame.K_RIGHT] and x <= 460 - width - speed + fild_2_.start_x * (player_fild_.player - 1):
        x += speed
    if keys_[pygame.K_UP] and y >= speed + 30:
        y -= speed
    if keys_[pygame.K_DOWN] and y <= 446 - height - speed:
        y += speed
    # print(player_fild_.player)  # пишет, какой игрок сейчас играет в выводе
    return player_fild_


# !!!WARNING!!! DEBUG
def red_movement_game(keys_, fild):
    for i in a:
        if not draw:
            if i.status == game_1_flag:
                i.draw()
            if i.status == 6 or i.status == 7:
                i.draw()
        else:
            draw = 1
            draw_swap()
    if keys_[pygame.K_n]:
        if draw:
            for i in a:
                if i.status == game_1_flag:
                    i.draw()
                if i.status == 6:
                    i.draw()
            draw = 0
            status_player()
            x = main_x_fild
            y = main_y_fild
            draw_window(a)
        else:
            draw = 1
            draw_swap()
    if keys_[pygame.K_SPACE]:
        x1 = (x - fild.start_x - 50) / 38
        y1 = (y - fild.start_y - 36) / 38

        if [x1, y1] in fild.fild_cells:
            cell = Cell(x, y)
            cell.project_name = BattleShip
            cell.status = 6
            a.append(cell)
        else:
            cell = Cell(x, y)
            cell.project_name = BattleShip
            cell.status = 7
            a.append(cell)
            draw = 1
    if keys[pygame.K_LEFT] and x >= 50 + speed + fild_2_x * game_1_flag:
        x -= speed
    if keys[pygame.K_RIGHT] and x <= 460 - width - speed + fild_2_x * game_1_flag:
        x += speed
    if keys[pygame.K_UP] and y >= speed + 30:
        y -= speed
    if keys[pygame.K_DOWN] and y <= 446 - height - speed:
        y += speed
    if draw == 0:
        if game_1_flag:
            draw_square(x, y)
        else:
            draw_square(x, y)


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
        zz = start_game(keys, player_fild, fild_1, fild_2)
        if zz != 3:
            player_fild = zz
        print(player_fild.player)
    else:
        print(5555)
    pygame.display.update()  # обновляет дисплей

pygame.quit()  # 100% закрытие программы
