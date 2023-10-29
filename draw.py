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
    def all():
        for animal in List.animals:
            pygame.draw.rect(Game.window, animal.color, (animal.x * Const.GRID_SIZE, animal.y * Const.GRID_SIZE, Const.GRID_SIZE, Const.GRID_SIZE), Const.GRID_SIZE)
        for obstacle in List.obstacles:
            pygame.draw.rect(Game.window, obstacle.color, (obstacle.x * Const.GRID_SIZE, obstacle.y * Const.GRID_SIZE, Const.GRID_SIZE, Const.GRID_SIZE), Const.GRID_SIZE)
