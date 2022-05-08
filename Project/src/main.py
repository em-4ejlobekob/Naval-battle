import init as i

from main_funcs import menu, game

while i.process:
    if i.fild_1.start == 0:
        i.fild_1, i.fild_2, i.fild_now, i.process = menu()
    elif i.fild_1.start == 1:
        i.fild_1 = game()
