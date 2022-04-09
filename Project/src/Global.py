import assets
import pygame
from Game import Game


pygame.init()

BattleShip = pygame.display.set_mode((1600, 800))  # name of the window
game = Game(BattleShip)
pygame.display.set_caption("Battles")  # title of the window

a = []
fild_1_x, fild_1_y = 30, 30
fild_2_x, fild_2_y = 790, 30
width, height, speed = 38, 38, 38
x_def, y_def = 50, 36
