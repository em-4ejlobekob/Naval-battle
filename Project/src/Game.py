from abc import ABC, abstractmethod
from random import randint


class Game:

    def __init__(self, project_name):
        self.project_name = project_name
        self.status = None
        self.field_size = 10
        self.ship_types = None
        self.turn = None
        self.player_status = 1
        self.players = []

    def set_turn(self):
        self.turn = randint(0, 1)

    def add_player(self, player):
        self.players.append(player)

    @abstractmethod
    def draw(self):
        pass
