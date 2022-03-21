import pygame
import time
from Ship import Ship
from Field import Field
from Cell import Cell

pygame.init()
fild_1_x, fild_1_y = 30, 30
fild_2_x, fild_2_y = 790, 30
BattleShip = pygame.display.set_mode((1600, 800))  # name of the window
pygame.display.set_caption("Battles")  # title of the window
fild_1, fild_1.project_name = Field(fild_1_x, fild_1_y), BattleShip
fild_2, fild_2.project_name = Field(fild_2_x, fild_2_y), BattleShip
fild_1.start_x = fild_1_x
fild_1.start_y = fild_1_y
fild_2.start_x = fild_2_x
fild_2.start_y = fild_2_y
width, height, speed = 38, 38, 38
x_def, y_def = 50, 36
x, y = x_def + fild_1_x, y_def + fild_1_y
size = 4
shipz = [1, 2, 3, 4]
ships = []

start_1_flag = 1
start_2_flag = 0
game_1_flag = 1
game_2_flag = 0
sh_ar_1 = []
sh_ar_2 = []
main_x_fild, main_y_fild = x_def + fild_2_x, y_def + fild_2_y


def draw_square(x_, y_):
    pygame.draw.rect(BattleShip, (64, 128, 255), (x_, y_, 36, 36), 4)  # рисует рамку


def draw_ship_in_moment(flag_size_, flag_ship_, x_, y_, fild_1_x_, fild_1_y_):
    if flag_ship_ % 2 == 0:
        ship = Ship(size, 'H', x_, y_, 0)
    else:
        ship = Ship(size, 'V', x_, y_, 0)
    ship.project_name = BattleShip
    ship.start_x, ship.start_y = fild_1_x_, fild_1_y_
    if flag_size_ and ship.test():
        ship.draw()


def draw_window(object_list):
    global game_1_flag
    BattleShip.fill((0, 0, 0))
    fild_1.draw()
    fild_2.draw()
    for i in object_list:
        if i.status == game_1_flag:
            i.draw()


def draw_swap():
    BattleShip.fill((0, 0, 0))
    f1 = pygame.font.Font(None, 100)
    text1 = f1.render('Очередь другого игрока, нажмите "N"', True, (255, 255, 255))
    BattleShip.blit(text1, (10, 50))
    pygame.display.update()  # обновляет дисплей


def red_movement_start(keys_):
    global x, y, flag_ship, flag_size, size, counter, start_1_flag, start_2_flag, draw, game_1_flag, sh_ar_1, sh_ar_2
    if keys_[pygame.K_n]:
        draw = 0
    if keys_[pygame.K_c] and start_1_flag + start_2_flag:
        flag_ship += 1
    if keys_[pygame.K_SPACE] and flag_size:
        if flag_ship % 2 == 0:
            sh = Ship(size, 'H', x - 1, y - 1, 0)
        else:
            sh = Ship(size, 'V', x - 1, y - 1, 0)
        sh.status = game_1_flag
        sh.project_name = BattleShip
        sh.start_x, sh.start_y = fild_moment_x, fild_moment_y
        if sh.test():
            if game_1_flag:
                sh_ar_1.append(sh)
                fild_1.app(x, y, sh.rotation, sh.size)
            else:
                sh_ar_2.append(sh)
                fild_2.app(x, y, sh.rotation, sh.size)
            a.append(sh)
            flag_size -= 1
            if flag_size == 0 and counter < 3:
                size -= 1
                counter += 1
                flag_size = shipz[counter]
        time.sleep(0.1)

    if keys[pygame.K_LEFT] and x >= 50 + speed + fild_2_x * start_2_flag:
        x -= speed
    if keys[pygame.K_RIGHT] and x <= 460 - width - speed + fild_2_x * start_2_flag:
        x += speed
    if keys[pygame.K_UP] and y >= speed + 30:
        y -= speed
    if keys[pygame.K_DOWN] and y <= 446 - height - speed:
        y += speed


def red_movement_game(keys_, fild):
    global x, y, flag_ship, flag_size, size, counter, start_1_flag, start_2_flag, draw, game_1_flag, a, main_x_fild, main_y_fild
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
        #print([x1, y1, 1])
        #print(fild.field_cells)
        if [x1, y1] in fild.field_cells:
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


def status_player():
    global game_1_flag, game_2_flag, main_x_fild, main_y_fild

    if game_1_flag:
        game_1_flag = 0
        game_2_flag = 1
        main_x_fild = fild_1_x + x_def
        main_y_fild = fild_1_y + y_def
    else:
        game_1_flag = 1
        game_2_flag = 0
        main_x_fild = fild_2_x + x_def
        main_y_fild = fild_2_y + y_def


a = []

flag_ship = 0
flag_size = shipz[0]
counter = 0

fild_moment_x = fild_1_x
fild_moment_y = fild_1_y

moment_x = fild_1_x
moment_y = fild_1_y
moment_start = 1
draw = 0
start = 1
game = 0

process = True
while process:
    pygame.time.delay(50)  # частота обновлений цикла

    for event in pygame.event.get():  # перебираем события
        if event.type == pygame.QUIT:
            process = False  # Если мы нажали на кнопочку закрыть, то мы выходим из приложения
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Нажата кнопка: ", event.button)

    keys = pygame.key.get_pressed()  # список кнопок, которые сейчас нажимаются

    #print(game_1_flag, game_2_flag)

    if draw:
        draw_swap()
    elif start_1_flag:
        draw_window(a)
        draw_ship_in_moment(flag_size, flag_ship, x - 1, y - 1, moment_x, moment_y)
    elif start_2_flag:
        draw_window(a)
        draw_ship_in_moment(flag_size, flag_ship, x - 1, y - 1, moment_x, moment_y)
    else:
        draw_window(a)

    if start:
        red_movement_start(keys)
    else:
        if game_1_flag == 1:
            red_movement_game(keys, fild_2)
        else:
            red_movement_game(keys, fild_1)

    if not (flag_size + start_1_flag + start_2_flag) and start:
        status_player()
        start = 0
        game = 1
    if flag_size:
        if not draw:
            draw_square(x, y)
    elif start_1_flag:
        moment_x, moment_y = fild_2_x, fild_2_y
        fild_moment_x, fild_moment_y = fild_2_x, fild_2_y
        x, y = x_def + fild_2_x, y_def + fild_2_y
        start_1_flag, start_2_flag = 0, 1
        size = 4
        shipz = [1, 2, 3, 4]
        flag_ship = 0
        flag_size = shipz[0]
        counter = 0
        draw = 1
        status_player()
    elif start_2_flag:
        draw = 1
        start_2_flag = 0




    pygame.display.update()  # обновляет дисплей

pygame.quit()  # 100% закрытие программы
