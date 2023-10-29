import pygame
from game import Game
from vars import *


class Draw:
    @staticmethod
    def grid():
        for y in range(Const.ROWS):
            for x in range(Const.COLUMNS):
                pygame.draw.rect(Game.window, (0, 0, 0), (x * Const.GRID_SIZE, y * Const.GRID_SIZE, Const.GRID_SIZE, Const.GRID_SIZE), 1)

    @staticmethod
    def something(x: int, y: int, color: tuple):
        pygame.draw.rect(Game.window, color, (x * Const.GRID_SIZE, y * Const.GRID_SIZE, Const.GRID_SIZE, Const.GRID_SIZE), Const.GRID_SIZE)
