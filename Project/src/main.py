from Fild import Fild
from Globals import *
from Functions import *
fild_1 = Fild(50, 50, 1)
fild_2 = Fild(800, 50, 2)

player = 1
process = True
fild_now = fild_1
while process:
    # if должен начинаться по другому: должно быть такое условие, чтобы мы при запуске сюда попадали сразу и всё, что
    # внутри, рисовало меню и кнопки меню. Уже else должен отправлять в то, что сейчас идёт после if True.
    # В конце есть ещё комментарии, там должна быть кнопка, возвращающая меню. Пусть в неё передаются параметры fild_1
    # and fild_2, которые внутри функции будут заново инициализироваться теми же параметрами, что идут перед циклом
    # while - так поля просто обнулятся. То, что в начале будут передаваться поля fild_1 and fild_2 - ничего плохого.
    if True:
        for event in pygame.event.get():  # перебираем события
            if event.type == pygame.QUIT:
                process = False  # Если мы нажали на кнопочку закрыть, то мы выходим из приложения
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print("Нажата кнопка: ", event.button)
                if event.button == 3:
                    fild_now.change_rotation()
                elif event.button == 5:
                    fild_now.next_ship()
                elif event.button == 4:
                    fild_now.previous_ship()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    start_flag = 0
                    pygame.mixer.pause()

            BattleShip.fill((0, 0, 0))
            f1 = fild_1.draw(fild_now.player)
            f2 = fild_2.draw(fild_now.player)

            if f1 == 'end_start' and fild_1.game == 'start':
                if next_button.draw(1200, 600, 'next player', true_function):
                    stop_screen()
                    fild_1.game = 'stop'
                    fild_now = change_fild(fild_now, fild_1, fild_2)
                    f1 = None

            if f1 == 'end_part':
                if next_button.draw(1200, 600, 'next player', true_function):
                    stop_screen()
                    fild_1.game = 'game'
                    fild_now = change_fild(fild_now, fild_1, fild_2)
                    f1 = None

            if f2 == 'end_start' and fild_2.game == 'start':
                if next_button.draw(1200, 600, 'next player', true_function):
                    stop_screen()
                    fild_1.game = 'game'
                    fild_2.game = 'game'
                    fild_now = change_fild(fild_now, fild_1, fild_2)
                    player = fild_now.player
                    f2 = None

            if f2 == 'end_part':
                if next_button.draw(1200, 600, 'next player', true_function):
                    stop_screen()
                    fild_2.game = 'game'
                    fild_now = change_fild(fild_now, fild_1, fild_2)
                    player = fild_now.player
                    f2 = None

            if f1 == 'Good game':
                pass
                # тут должна быть функция, которая вызывает плашку о том, что победил первый игрок
                # и кнопка вернуться в меню

            if f2 == 'Good game':
                pass
                # тут должна быть функция, которая вызывает плашку о том, что победил второй игрок
                # и кнопка вернуться в меню

        pygame.display.update()
