import variables as var

from Fild import Fild
from Globals import BattleShip, pygame
from buttons import next_button, start_button, doctor_button, quit_button
from Functions import laugh, change_fild, stop_screen, true_function, winner_screen, print_control

fild_1 = Fild(var.fild_1_x, var.fild_1_y, 1)
fild_2 = Fild(var.fild_2_x, var.fild_2_y, 2)

player = 1
process = True
fild_now = fild_1

while process:
    if fild_1.start == 0:
        fild_1 = Fild(var.fild_1_x, var.fild_1_y, 1)
        fild_2 = Fild(var.fild_2_x, var.fild_2_y, 2)
        player = 1
        process = True
        fild_now = fild_1
        BattleShip.fill((0, 0, 0))
        bcg = pygame.image.load(var.doctor1_path)

        while fild_1.start == 0:
            for event_ in pygame.event.get():
                if event_.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                BattleShip.blit(bcg, (0, 0))

            start_button.draw(var.start_bttn_x, var.start_bttn_y, 'START LEGENDARY BATTLESHIP', fild_1.to_game)
            doctor_button.draw(var.doctor_bttn_x, var.doctor_bttn_y, 'AXAXAXAXAXAXAXAXAXAXXAX', laugh)
            quit_button.draw(var.quit_bttn_x, var.quit_bttn_y, 'NO, I AM AFRAID OF BIG SHIPS', quit)

            pygame.display.update()
            pygame.time.delay(50)

    if fild_1.start == 1:
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
                    fild_1.to_menu()
                elif event.key == pygame.K_e:
                    print(pygame.mixer.music.get_volume())
                    volume = pygame.mixer.music.get_volume()
                    pygame.mixer.music.set_volume(volume + 0.125)  # WARNING!!!
                elif event.key == pygame.K_q:
                    print(pygame.mixer.music.get_volume())
                    volume = pygame.mixer.music.get_volume()
                    pygame.mixer.music.set_volume(volume - 0.125)  # WARNING!!!
                elif event.key == pygame.K_p:
                    print(pygame.mixer.music.get_busy())
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()

            BattleShip.fill((0, 0, 0))
            f1 = fild_1.draw(fild_now.player)
            f2 = fild_2.draw(fild_now.player)
            print_control()

            if (f1 == 'end_start' and fild_1.game == 'start') or (f1 == 'end_part'):
                if next_button.draw(var.next_bttn_x, var.next_bttn_y, 'next player', true_function):
                    stop_screen()
                    fild_1.game = 'game' if f1 == 'end_part' else 'stop'
                    if f1 == 'end_part':
                        fild_1.game = 'game'
                    else:
                        fild_1.game = 'stop'
                    fild_now = change_fild(fild_now, fild_1, fild_2)
                    f1 = None

            if (f2 == 'end_start' and fild_2.game == 'start') or (f2 == 'end_part'):
                if next_button.draw(var.next_bttn_x, var.next_bttn_y, 'next player', true_function):
                    stop_screen()
                    fild_2.game = 'game'
                    if f2 != 'end_part':
                        fild_1.game = 'game'
                    fild_now = change_fild(fild_now, fild_1, fild_2)
                    f2 = None

            if f1 == 'Good game':
                winner_screen('2', fild_1)

            if f2 == 'Good game':
                winner_screen('1', fild_1)

        pygame.display.update()
