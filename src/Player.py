from Game import Game
from Field import Field


class Player(Game):
    def __init__(self, login, password):
        Game.__init__(self)
        self.login = login
        self.password = password
        self.stats = {}
        self.ships = []
        self.field = None

    def draw(self):
        pass

