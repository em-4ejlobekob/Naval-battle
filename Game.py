from abc import ABC, abstractmethod
from random import randint


class Game:

    def __init__(self):
        self.project_name = None
        self.status = "setting"
        self.field_size = 10
        self.ship_types = None
        self.turn = None
        self.players = []

    def set_turn(self):
        self.turn = randint(0, 1)

    def add_player(self, player):
        self.players.append(player)

    @abstractmethod
    def draw(self):
        pass
