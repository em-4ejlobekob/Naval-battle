import variables as var

from Cell import Cell
from Globals import BattleShip, pygame
from Ship import Ship


class Fild:
    """Класс Поле

    Экземпляром класса является игровое поле 10 на 10

    """
    def __init__(self, x, y, player):
        self.winner = None
        self.start = 0
        self.game = 'start'
        self.display = BattleShip
        self.x = x
        self.y = y
        self.player = player
        self.cells = dict()
        self.rotation = 'H'
        self.destroyed_ships = 0
        for i in range(var.fild_size + 2):
            for j in range(var.fild_size + 2):
                self.cells[i, j] = Cell(i, j, self.player)

        self.ships = [[4, 1], [3, 2], [2, 3], [1, 4]]

    def test_install(self, ship):
        """Проверяет возможность поставить корабль в выбранный сектор поля"""
        if len(self.ships):
            if ship.dx:
                x_test, y_test = ship.size + 1, 2
            else:
                x_test, y_test = 2, ship.size + 1

            for i in range(ship.x - 1, ship.x + x_test):
                for j in range(ship.y - 1, ship.y + y_test):
                    if self.cells[i, j].status != '0' or \
                            ship.dx * ship.x + ship.dy * ship.y + ship.size > var.fild_size + 1:
                        pygame.mixer.Sound.play(pygame.mixer.Sound(var.not_allowed_path))
                        return False
            pygame.mixer.Sound.play(pygame.mixer.Sound(var.bell_sound_path))
            return True
        pygame.mixer.Sound.play(pygame.mixer.Sound(var.not_allowed_path))
        return False

    def install(self, ship):
        """Устанавливает корабль на поле"""
        if self.test_install(ship):
            if ship.dx:
                for i in range(ship.x, ship.x + ship.size):
                    self.cells[i, ship.y].status = 'ship'
            else:
                for i in range(ship.y, ship.y + ship.size):
                    self.cells[ship.x, i].status = 'ship'
            self.ships[0][1] -= 1
            if self.ships[0][1] == 0:
                if len(self.ships):
                    self.ships.pop(0)

    def test_hit(self, x, y):
        """Проверяет убит корабль или ранен"""
        counter, start_x, end_x, start_y, end_y = 1, x, x, y, y
        counter_hit = 1 if self.cells[x, y].status == 'ship_hit' else 0
        # Если статут длиннее трёх символов, значит на клетке стоит либо целый корабль, либо уничтоженный
        # Статус длиннее 4-х символов имеет только 'ship_hit'
        while len(self.cells[start_x - 1, y].status) > 3 or len(self.cells[end_x + 1, y].status) > 3 or len(
                self.cells[x, start_y - 1].status) > 3 or len(self.cells[x, end_y + 1].status) > 3:
            if len(self.cells[start_x - 1, y].status) > 3:
                counter_hit += 1 if len(self.cells[start_x - 1, y].status) > 4 else 0
                start_x -= 1
                counter += 1
            if len(self.cells[end_x + 1, y].status) > 3:
                counter_hit += 1 if len(self.cells[end_x + 1, y].status) > 4 else 0
                end_x += 1
                counter += 1
            if len(self.cells[x, start_y - 1].status) > 3:
                counter_hit += 1 if len(self.cells[x, start_y - 1].status) > 4 else 0
                start_y -= 1
                counter += 1
            if len(self.cells[x, end_y + 1].status) > 3:
                counter_hit += 1 if len(self.cells[x, end_y + 1].status) > 4 else 0
                end_y += 1
                counter += 1

        if counter == counter_hit:
            pygame.mixer.Sound.play(pygame.mixer.Sound(var.wilhelm_scream_path))
            self.destroyed_ships += counter_hit
            if start_y == end_y:
                self.cells[start_x - 1, start_y].status = self.cells[end_x + 1, start_y].status = 'hit'
                for i in range(start_x - 1, end_x + 2):
                    self.cells[i, start_y - 1].status = self.cells[i, start_y + 1].status = 'hit'
            elif start_x == end_x:
                self.cells[start_x, start_y - 1].status = self.cells[end_x, start_y + 1].status = 'hit'
                for i in range(start_y - 1, end_y + 2):
                    self.cells[start_x - 1, i].status = self.cells[start_x + 1, i].status = 'hit'
        else:
            pass
            pygame.mixer.Sound.play(pygame.mixer.Sound(var.damage_path))

    def draw(self, player):
        """Актуально рисует игровое поле для игрока"""
        pygame.draw.rect(self.display, var.cell_inactive_colour, (self.x, self.y, var.fild_size * var.cell_wight + 2,
                                                                  var.fild_size * var.cell_height + 1), 2)

        for i in range(var.fild_size):
            for j in range(var.fild_size):
                coord = self.cells[i + 1, j + 1].draw(self.x + 1 + var.cell_wight * i,
                                                      self.y + 1 + var.cell_height * j, player)
                if self.game == 'start':

                    if coord is not None and player == self.player and len(self.ships):
                        ship = Ship(i + 1, j + 1, self.ships[0][0], self.rotation)
                        ship.draw(self.x + 1, self.y + 1)
                        if coord[1] and self.test_install(ship):
                            self.install(ship)

                elif self.game == 'game':

                    if coord is not None and player != self.player and coord[1]:
                        if self.cells[i + 1, j + 1].status == 'ship':
                            self.cells[i + 1, j + 1].status = 'ship_hit'
                            self.test_hit(i + 1, j + 1)
                        elif self.cells[i + 1, j + 1].status == '0':
                            pygame.mixer.Sound.play(pygame.mixer.Sound(var.bubble_path))
                            self.cells[i + 1, j + 1].status = 'hit'
                            self.game = 'next_player'

                elif self.game == 'end':
                    pass

                self.cells[i + 1, j + 1].draw(self.x + 1 + var.cell_wight * i, self.y + 1 + var.cell_height * j, player)

        if len(self.ships) == 0 and self.game == 'start':
            return 'end_start'
        if self.game == 'next_player':
            return 'end_part'
        if self.destroyed_ships == var.ship_dstr_cells:
            return 'Good game'
        return None

    def next_ship(self):
        """Меняет корабль во время расстановки кораблей"""
        self.ships.append(self.ships.pop(0))

    def previous_ship(self):
        """Меняет корабль во время расстановки кораблей"""
        self.ships.insert(0, self.ships.pop(-1))

    def change_rotation(self):
        """Меняет ротацию корабля во время расстановки кораблей"""
        if self.rotation == 'H':
            self.rotation = 'V'
        else:
            self.rotation = 'H'

    def to_menu(self):
        """Переводит флаг старта игры в состояние Меню"""
        self.start = 0
        pygame.mixer.stop()
        pygame.mixer.music.stop()
        return True

    def to_game(self):
        """Переводит флаг старта игры в состояние Игра"""
        self.start = 1
        pygame.mixer.stop()
        pygame.mixer.music.stop()
        pygame.mixer.music.set_volume(var.volume)
        pygame.mixer.music.load(var.bcg_path)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(var.volume)

    def winner_name(self, name):
        """Возвращает номер победителя"""
        self.winner = name
