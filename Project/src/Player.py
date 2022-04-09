from Game import Game
from Field import Field


class Player(Game):
    def __init__(self, login, password, game):
        Game.__init__(self, game.project_name)
        self.login = login
        self.password = password
        self.stats = {}
        self.ships = []
        self.field = None

    def draw(self):
        pass

