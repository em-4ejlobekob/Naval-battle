from venv.Gggame import Game


class Settings(Game):
    def __init__(self):
        Game.__init__(self)

    def ships(self):
        self.ship_types = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]

    def field(self):
        self.field_size = 10
