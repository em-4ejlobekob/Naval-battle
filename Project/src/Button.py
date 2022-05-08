import variables as var

from Globals import pygame, BattleShip, main_font


class Button:
    """Класс Кнопка

    Экземпляром класса является кнопка, на которую можно нажать. При наведении на кнопку она будет подсвечиваться
    цветом active_colour. При нажатии будет вызвана функция action, и возвращено значение этой функции, либо None
    через метод draw.

    """
    def __init__(self, wight, height):
        self.wight = wight
        self.height = height
        self.inactive_colour = var.inactive_button_colour
        self.active_colour = var.active_button_colour
        self.display = BattleShip

    def print_button_txt(self, message, x, y, font_type=main_font,
                         font_color=var.button_font_color, font_size=var.button_font_size):
        """Выводит слова, которые написаны на кнопке"""
        font_type = pygame.font.Font(font_type, font_size)
        txt = font_type.render(message, True, font_color)
        self.display.blit(txt, (x + var.bttn_indent_x, y + var.bttn_indent_y))

    def draw(self, x, y, message, action=None,):
        """Метод рисует кнопку на поле

        На вход подаются координаты, где кнопка рисуется, слова, которые будут на ней написаны и как необязательный
        аргумент - имя функции. Если курсор наведён на кнопку, то она подсвечивается цветом active_color.
        Если нажать на кнопку, то она вызовет поданную функцию action() и вернёт её результат, либо вернёт None.
        Если курсор не наведён на кнопку, то она подсвечивается цветом inactive_color.

        """
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x + self.wight and y < mouse[1] < y + self.height:
            pygame.draw.rect(self.display, self.active_colour, (x, y, self.wight, self.height))
            self.print_button_txt(message, x, y)
            if click[0] and action is not None:
                pygame.time.delay(200)
                return action()
            else:
                return None
        else:
            pygame.draw.rect(self.display, self.inactive_colour, (x, y, self.wight, self.height))
            self.print_button_txt(message, x, y)
